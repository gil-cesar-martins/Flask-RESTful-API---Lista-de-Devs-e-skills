from flask_restful import Resource

lista_habilidades = ['Python','C++','MySQL','Unreal']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades