#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

#class Ticket(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    titulo = db.Column(db.String(100), nullable=False)
#    descricao = db.Column(db.Text, nullable=False)
#    setor = db.Column(db.String(50), nullable=False)
#    responsavel = db.Column(db.String(50), nullable=False)
#    status = db.Column(db.String(20), nullable=False)
#    data_criacao = db.Column(db.DateTime, nullable=False)

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    setor = db.Column(db.String(50), nullable=False)
    responsavel = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    arquivo_nome = db.Column(db.String(255), nullable=True)

    comentarios = db.relationship('Comment', back_populates='ticket', cascade='all, delete-orphan', lazy='dynamic')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    ticket = db.relationship('Ticket', back_populates='comentarios')
    user = db.relationship('User')

