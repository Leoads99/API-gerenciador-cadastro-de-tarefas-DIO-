from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [

    {
        'id': 0,
        'responsavel': 'Leonardo',
        'tarefa': 'Criar tabela no hive setada no s3',
        'status': 'Em progresso'},

    {
        'id': 1,
        'responsavel': 'Magno',
        'tarefa': 'Desenvolvimento do CRUD de responsáveis',
        'status': 'Em progresso'}
]


# Devolve(GET) uma tarefa, Altera(PUT) uma tarefa e também deleta(DELETE)
@app.route('/task/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = 'Tarefa de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    if request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})


@app.route('/task/change/<int:id>/<status>/', methods=['PUT'])
def alterar_status(id ,status):
    if request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id]['status'] = status
        dados = tarefas[id]
        return jsonify(dados)


# Lista as tarefas(GET) e insere uma nova tarefa(POST)
@app.route('/task/', methods=['POST', 'GET'])
def lista_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])
    elif request.method == 'GET':
        return jsonify(tarefas)


if __name__ == '__main__':
    app.run(debug=True)
