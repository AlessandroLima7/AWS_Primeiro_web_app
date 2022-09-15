from main import db


class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(40), nullable=True)
    descricao = db.Column(db.String(40), nullable=True)
    preco = db.Column(db.Float, nullable=True)
    
    def __repr__(self):
        return '<Name %r>' % self.name
    
    