from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    setor = db.Column(db.String(50), nullable=False)
    responsavel = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False)
