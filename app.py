import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Ticket, Comment
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Banco de dados
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'database', 'helpdesk.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Upload
UPLOAD_FOLDER = os.path.join(base_dir, 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

db.init_app(app)

# Login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

# Rotas

@app.route('/uploads/<filename>')
@login_required
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
@login_required
def index():
    query = Ticket.query
    status = request.args.get('status')
    setor = request.args.get('setor')
    responsavel = request.args.get('responsavel')
    if status:
        query = query.filter(Ticket.status == status)
    if setor:
        query = query.filter(Ticket.setor.ilike(f'%{setor}%'))
    if responsavel:
        query = query.filter(Ticket.responsavel.ilike(f'%{responsavel}%'))
    tickets = query.order_by(Ticket.data_criacao.desc()).all()
    return render_template('index.html', tickets=tickets)

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        arquivo = request.files.get('arquivo')
        nome_arquivo_salvo = None

        if arquivo and arquivo.filename != '':
            if allowed_file(arquivo.filename):
                filename = secure_filename(arquivo.filename)
                caminho_arquivo = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                arquivo.save(caminho_arquivo)
                nome_arquivo_salvo = filename
            else:
                flash('Arquivo não permitido.', 'danger')
                return redirect(request.url)

        novo = Ticket(
            titulo=request.form['titulo'],
            descricao=request.form['descricao'],
            setor=request.form['setor'],
            responsavel=request.form['responsavel'],
            status=request.form['status'],
            data_criacao=datetime.now(),
            arquivo_nome=nome_arquivo_salvo
        )
        db.session.add(novo)
        db.session.commit()
        flash('Chamado criado com sucesso.', 'success')
        return redirect(url_for('index'))

    return render_template('create_ticket.html')

@app.route('/ticket/<int:id>', methods=['GET', 'POST'])
@login_required
def ticket_detail(id):
    ticket = Ticket.query.get_or_404(id)

    if request.method == 'POST':
        mensagem = request.form.get('mensagem')
        if not mensagem.strip():
            flash('O comentário não pode ser vazio.', 'warning')
        else:
            comentario = Comment(
                ticket_id=ticket.id,
                user_id=current_user.id,
                mensagem=mensagem,
                data_criacao=datetime.utcnow()
            )
            db.session.add(comentario)
            db.session.commit()
            flash('Comentário adicionado com sucesso!', 'success')
            return redirect(url_for('ticket_detail', id=ticket.id))

    comentarios = ticket.comentarios.order_by(Comment.data_criacao.asc()).all()
    return render_template('ticket_detail.html', ticket=ticket, comentarios=comentarios)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    ticket = Ticket.query.get_or_404(id)
    if request.method == 'POST':
        ticket.status = request.form['status']
        db.session.commit()
        flash('Status atualizado.')
        return redirect(url_for('ticket_detail', id=ticket.id))
    return render_template('update_ticket.html', ticket=ticket)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(senha):
            login_user(user)
            return redirect(url_for('index'))
        flash('Usuário ou senha inválidos.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if User.query.filter_by(email=email).first():
            flash('E-mail já registrado.')
            return redirect(url_for('register'))
        user = User(email=email)
        user.set_password(senha)
        db.session.add(user)
        db.session.commit()
        flash('Cadastro realizado com sucesso! Faça login.')
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)



