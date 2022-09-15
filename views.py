from flask import Flask, render_template, request, redirect, session, flash, url_for
from main import app, db
from models import Produtos

@app.route('/')
def login():
    return render_template('login.html', titulo="APP AWS")

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario=request.form['usuario']
    if(usuario == 'primeiroServer'):
        if(request.form['senha'] == "ale2022"):
            session['usuario_logado'] = "toaqui"
            return redirect(url_for('consultar'))
        else:
            flash("Usuário ou senha incorretos.")
            return redirect(url_for('login'))
    else:
        flash("Usuário ou senha incorretos.")
        return redirect(url_for('login'))

@app.route('/consultar')                 # ESTA É A TELA PRINCIPAL ONDE SÃO LISTADOS OS PRODUTOS
def consultar():
    if(session['usuario_logado'] == None):
        return redirect(url_for('login'))
    
    produtos = Produtos.query.all()
    return render_template('consultar.html', titulo='Produtos', produtos=produtos)

@app.route('/inserir')                 # TRANSIÇÃO PARA TELA DE INSERIR PRODUTOS
def inserir():
    if(session['usuario_logado'] == None):
        return redirect(url_for('login'))
    
    return render_template('inserir.html', titulo='Inserir Produto')

@app.route("/inserindo", methods=['POST',])
def inserindo():
    if(session['usuario_logado'] == None):
        return redirect(url_for('login'))
    
    produto = Produtos(nome=request.form['nome'], descricao=request.form['descricao'], preco=request.form['preco'])
    db.session.add(produto)
    db.session.commit()
    flash("Produto inserido com sucesso!")
    return redirect(url_for('consultar'))

@app.route("/editar/<int:id>")
def editar(id):
    if(session['usuario_logado'] == None):
        return redirect(url_for('login'))
    produto = Produtos.query.filter_by(id=id).first()
    return render_template('editar.html', titulo='Editar Produto', produto=produto)

@app.route("/confirma_edicao", methods=['POST', ])
def confirma_edicao():
    if(session['usuario_logado'] == None):
        return redirect(url_for('login'))
    produto = Produtos.query.filter_by(id=request.form["id"]).first()
    produto.nome = request.form['nome']
    produto.descricao = request.form['descricao']
    produto.preco = request.form['preco']
    db.session.add(produto)
    db.session.commit()
    flash("Produto editado com sucesso!")
    return redirect(url_for('consultar'))
    
@app.route("/excluir/<int:id>")
def excluir(id):
    if(session['usuario_logado'] == None):
        return redirect(url_for('login'))
    Produtos.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Produto excluído com sucesso!")
    return redirect(url_for("consultar"))
    

@app.route('/logout')                                      # TRANSIÇÃO PARA FAZER LOGOUT DE USUÁRIO 
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))

