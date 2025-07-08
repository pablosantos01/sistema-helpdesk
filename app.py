from flask import Flask, render_template, request, redirect, url_for
from models import db, Ticket
from datetime import datetime
import os

app = Flask(__name__)

# Caminho absoluto do banco
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'database', 'helpdesk.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Criação do banco
with app.app_context():
    db.create_all()

# Passa current_year para todos templates (para footer dinâmico)
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@app.route('/')
def index():
    tickets = Ticket.query.order_by(Ticket.data_criacao.desc()).all()
    return render_template('index.html', tickets=tickets)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        novo = Ticket(
            titulo=request.form['titulo'],
            descricao=request.form['descricao'],
            setor=request.form['setor'],
            responsavel=request.form['responsavel'],
            status=request.form['status'],
            data_criacao=datetime.now()
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_ticket.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    ticket = Ticket.query.get_or_404(id)
    if request.method == 'POST':
        ticket.status = request.form['status']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_ticket.html', ticket=ticket)

if __name__ == '__main__':
    app.run(debug=True)
