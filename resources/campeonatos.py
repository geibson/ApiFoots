from flask_restful import Resource, reqparse
from models.campeonato import CampeonatoModel
from models.site import SiteModel
from resources.filtros import normalize_path_params, consulta_com_cidade, consulta_sem_cidade
from flask_jwt_extended import jwt_required
import sqlite3



path_params = reqparse.RequestParser()
path_params.add_argument('camp_id',type = int)
path_params.add_argument('urlLogo', type=str)
path_params.add_argument('sdeSlug', type=str)
path_params.add_argument('categoria', type=str)
path_params.add_argument('temporada', type=int)
path_params.add_argument('nomeDaTaca', type=str)
path_params.add_argument('tipoDeColeta', type=str)
path_params.add_argument('nome', type=str)
path_params.add_argument('faseAtual', type=str)
path_params.add_argument('rodadaAtual', type=str)
path_params.add_argument('pais', type=str)
path_params.add_argument('ativo', type=bool)
path_params.add_argument('apelido', type=str)
path_params.add_argument('campeonato_id', type=int)
path_params.add_argument('edicao_id', type=int)
path_params.add_argument('quantidadeDeEquipes', type=int)
path_params.add_argument('quantidadeDeRodadas', type=int)
path_params.add_argument('temClassificacaoPorGrupo', type=bool)
path_params.add_argument('temClassificacao', type=bool)


class Campeonatos(Resource):
    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()

        dados = path_params.parse_args()
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        parametros = normalize_path_params(**dados_validos)

        if not parametros.get('cidade'):
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_sem_cidade, tupla)
        else:
            tupla = tuple([parametros[chave] for chave in parametros])
            resultado = cursor.execute(consulta_com_cidade, tupla)

        campeonatos = []
        for linha in resultado:
            campeonatos.append({
            'camp_id': linha[0] ,
            'urlLogo': linha[1],
            'sdeSlug': linha [2],
            'categoria': linha [3],
            'temporada': linha [4],
            'nomeDaTaca': linha [5],
            'tipoDeColeta': linha [6],
            'nome': linha [7],
            'faseAtual': linha [8],
            'rodadaAtual': linha [9],
            'pais': linha [10],
            'ativo': linha [11],
            'apelido': linha [12],
            'campeonato_id': linha [13],
            'edicao_id': linha [14],
            'quantidadeDeEquipes': linha [15],
            'quantidadeDeRodadas': linha [16],
            'temClassificacaoPorGrupo': linha [17],
            'temClassificacao': linha [18]
            })

        return {'campeonatos': campeonatos} # SELECT * FROM campeonatos

class Campeonato(Resource):
    atributos = reqparse.RequestParser()
    path_params.add_argument('urlLogo')
    path_params.add_argument('sdeSlug')
    path_params.add_argument('categoria')
    path_params.add_argument('temporada')
    path_params.add_argument('nomeDaTaca')
    path_params.add_argument('tipoDeColeta')
    path_params.add_argument('nome')
    path_params.add_argument('faseAtual')
    path_params.add_argument('rodadaAtual')
    path_params.add_argument('pais')
    path_params.add_argument('ativo')
    path_params.add_argument('apelido')
    path_params.add_argument('campeonato_id')
    path_params.add_argument('edicao_id')
    path_params.add_argument('quantidadeDeEquipes')
    path_params.add_argument('quantidadeDeRodadas')
    path_params.add_argument('temClassificacaoPorGrupo')
    path_params.add_argument('temClassificacao')
    def get(self,camp_id):
        campeonato = CampeonatoModel.find_campeonato(camp_id)
        if campeonato:
            return campeonato.json()
        return {'message': 'Campeonato not found.'}, 404

    @jwt_required
    def post(self, camp_id):
        if CampeonatoModel.find_campeonato(camp_id):
            return {"message": "Campeonato id '{}' already exists.".format(camp_id)}, 400 #Bad Request

        dados = Campeonato.atributos.parse_args()
        campeonato = CampeonatoModel(camp_id, **dados)

        if not SiteModel.find_by_id(dados['site_id']):
            return {'message': 'The campeonato must be associated to a valid site id.'}, 400

        try:
            campeonato.save_campeonato()
        except:
            return {"message": "An error ocurred trying to create campeonato."}, 500 #Internal Server Error
        return campeonato.json(), 201

    @jwt_required
    def put(self, camp_id):
        dados = Campeonato.atributos.parse_args()
        campeonato = CampeonatoModel(camp_id, **dados)

        campeonato_encontrado = CampeonatoModel.find_campeonato(camp_id)
        if campeonato_encontrado:
            campeonato_encontrado.update_hotel(**dados)
            campeonato_encontrado.save_hotel()
            return campeonato_encontrado.json(), 200
        campeonato.save_campeonato()
        return campeonato.json(), 201

    @jwt_required
    def delete(self, camp_id):
        campeonato = CampeonatoModel.find_campeonato(camp_id)
        if campeonato:
            campeonato.delete_campeonato()
            return {'message': 'campeonato deleted.'}
        return {'message': 'campeonato not found.'}, 404