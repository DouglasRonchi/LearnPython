import sys
sys.path.append("C://Users/900214/Desktop/dc-doidera/HBtechsis")
from flask import Flask, render_template, redirect, request
from classes.dao.funcionario_dao import FuncionarioDao
from classes.dao.equipe_dao import EquipeDao
from classes.dao.linguagens_dao import LinguagensDao
from classes.model.funcionario import Funcionario
from classes.model.equipe import Equipe
from classes.model.linguagens import Linguagens

dao_fun = FuncionarioDao()
dao_lin = LinguagensDao()
dao_equ = EquipeDao()

mod_fun = Funcionario()
mod_lin = Linguagens()
mod_equ = Equipe()

app = Flask(__name__)

#ROTA PRINCIPAL
@app.route('/')
def home():
    title = 'Home'
    return render_template('home.html', title = title)


#ROTAS DE LISTAGEM
@app.route('/funcionarios')
def func():
    title = 'Funcionarios'
    f = FuncionarioDao()
    lista = f.listar()
    return render_template('lista_funcionarios.html', title = title, lista = lista)


@app.route('/equipes')
def equi():
    title = 'Equipes'
    e = EquipeDao()
    lista = e.listar()
    return render_template('lista_equipes.html', title = title, lista = lista)


@app.route('/linguagens')
def ling():
    title = 'Linguagens'
    l = LinguagensDao()
    lista = l.listar()
    return render_template('lista_linguagens.html', title = title, lista = lista)

#ROTAS DE FORMULARIOS

#FUNCIONARIOS
@app.route('/form_funcionario')
def ffunc():
    title = 'Cadastrar/Alterar Funcionario'
    f = FuncionarioDao()
    l = LinguagensDao()
    lista_linguagens = l.listar()
    e = EquipeDao()
    lista_equipes = e.listar()
    if ('id' in request.args.keys()):
        #Edicao
        id = request.args['id']
        funcionario = f.buscar_por_id(id)
        return render_template('form_funcionario.html',title = title, funcionario = funcionario, lista_ling = lista_linguagens, lista_equi = lista_equipes)
    return render_template('form_funcionario.html', title = title, lista_ling = lista_linguagens, lista_equi = lista_equipes)


@app.route('/salvar_funcionario', methods=['POST'])
def sfunc():
    if ('salvar' in request.form.keys()):
        #Cadastra
        mod_fun.set_nome(request.form['nome'])
        mod_fun.set_cpf(request.form['cpf'])
        mod_fun.set_linguagem(request.form['linguagem'])
        mod_fun.set_equipe(request.form['equipe'])
        mod_fun.set_num_registro(request.form['num_registro'])
        dao_fun.inserir(mod_fun)
    elif ('editar' in request.form.keys()):
        #Editar
        mod_fun.set_id(request.form['id'])
        mod_fun.set_nome(request.form['nome'])
        mod_fun.set_cpf(request.form['cpf'])
        mod_fun.set_linguagem(request.form['linguagem'])
        mod_fun.set_equipe(request.form['equipe'])
        mod_fun.set_num_registro(request.form['num_registro'])
        dao_fun.alterar(mod_fun)
    return redirect('/funcionarios')


@app.route('/deletar_funcionario')
def dfunc():
    id = request.args['id']
    dao_fun.deletar(id)
    return redirect('/funcionarios')


#EQUIPES
@app.route('/form_equipe')
def fequi():
    title = 'Cadastrar/Alterar Equipe'
    e = EquipeDao()
    l = LinguagensDao()
    lista_ling = l.listar()
    if ('id' in request.args.keys()):
        #Edicao
        id = request.args['id']
        equipe = e.buscar_por_id(id)
        return render_template('form_equipe.html',title = title, equipe = equipe, lista_ling = lista_ling)
    return render_template('form_equipe.html', title = title, lista_ling = lista_ling)


@app.route('/salvar_equipe', methods=['POST'])
def sequi():
    if ('salvar' in request.form.keys()):
        #Cadastra
        mod_equ.set_nome(request.form['nome'])
        mod_equ.set_linguagem(request.form['linguagem'])
        dao_equ.inserir(mod_equ)
    elif ('editar' in request.form.keys()):
        #Editar
        mod_equ.set_id(request.form['id'])
        mod_equ.set_nome(request.form['nome'])
        mod_equ.set_linguagem(request.form['linguagem'])
        dao_equ.alterar(mod_equ)
    return redirect('/equipes')


@app.route('/deletar_equipe')
def dequi():
    id = request.args['id']
    dao_equ.deletar(id)
    return redirect('/equipes')


#LINGUAGENS
@app.route('/form_linguagem')
def fling():
    title = 'Cadastrar/Alterar Linguagem'
    l = LinguagensDao()
    if ('id' in request.args.keys()):
        #Edicao
        id = request.args['id']
        linguagem = l.buscar_por_id(id)
        return render_template('form_linguagem.html',title = title, linguagem = linguagem)
    return render_template('form_linguagem.html', title = title)


@app.route('/salvar_linguagem', methods=['POST'])
def sling():
    if ('salvar' in request.form.keys()):
        #Cadastra
        mod_lin.set_nome(request.form['nome'])
        mod_lin.set_descricao(request.form['descricao'])
        dao_lin.inserir(mod_lin)
    elif ('editar' in request.form.keys()):
        #Editar
        mod_lin.set_id(request.form['id'])
        mod_lin.set_nome(request.form['nome'])
        mod_lin.set_descricao(request.form['descricao'])
        dao_lin.alterar(mod_lin)
    return redirect('/linguagens')


@app.route('/deletar_linguagem')
def dling():
    id = request.args['id']
    dao_lin.deletar(id)
    return redirect('/linguagens')

app.run(debug=True)