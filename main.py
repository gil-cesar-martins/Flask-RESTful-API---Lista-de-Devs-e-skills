from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

devs = [
    {
    'id':'0',
    'nome':'gil',
    'habilidades':['Python','MySQL']
    },
    
    {
    'id':'1',
    'nome':'Edward',
    'habilidades':['C++','Unreal']
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = devs[id]
        except IndexError:
            message = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro' , 'mensagem':message}
        except Exception:
            message = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status':'erro' , 'mensagem':message}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        return dados
        

    def delete(self, id):
        devs.pop(id)
        return {'status':'sucesso','mensagem':'Registro excluído'}
    

#Lista todos s desenvolvedores e permite registrar um novo desenvolvidor
class Lista_Desenvolvedores(Resource):
    def get(self):
        return devs

    def post(self):
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return devs[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_Desenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)