from sql_alchemy import banco

class CampeonatoModel(banco.Model):
    __tablename__ = 'campeonatos'

    camp_id = banco.Column(banco.String, primary_key=True)
    urlLogo = banco.Column(banco.String(80))
    sdeSlug = banco.Column(banco.String(80))
    categoria= banco.Column(banco.String(80))
    temporada= banco.Column(banco.String(80))
    nomeDaTaca= banco.Column(banco.String(80))
    tipoDeColeta= banco.Column(banco.String(80))
    nome= banco.Column(banco.String(80))
    faseAtual= banco.Column(banco.String(80))
    rodadaAtual= banco.Column(banco.String(80))
    pais= banco.Column(banco.String(80))
    ativo= banco.Column(banco.String(80))
    apelido= banco.Column(banco.String(80))
    campeonato_id= banco.Column(banco.String(80))
    edicao_id= banco.Column(banco.String(80))
    quantidadeDeEquipes= banco.Column(banco.String(80))
    quantidadeDeRodadas= banco.Column(banco.String(80))
    temClassificacaoPorGrupo= banco.Column(banco.String(80))
    temClassificacao= banco.Column(banco.String(80))




    def __init__(self, camp_id,urlLogo,sdeSlug,categoria,temporada,nomeDaTaca,tipoDeColeta,nome,faseAtual,rodadaAtual,pais,ativo,apelido,campeonato_id,edicao_id,quantidadeDeEquipes,quantidadeDeRodadas,temClassificacaoPorGrupo,temClassificacao):
        self.camp_id=camp_id,
        self.urlLogo=urlLogo
        self.sdeSlug=sdeSlug
        self.categoria=categoria
        self.temporada=temporada
        self.nomeDaTaca=nomeDaTaca
        self.tipoDeColeta=tipoDeColeta
        self.nome=nome
        self.faseAtual=faseAtual
        self.rodadaAtual=rodadaAtual
        self.pais=pais
        self.ativo=ativo
        self.apelido=apelido
        self.campeonato_id=campeonato_id,
        self.edicao_id=edicao_id
        self.quantidadeDeEquipes=quantidadeDeEquipes
        self.quantidadeDeRodadas=quantidadeDeRodadas,
        self.temClassificacaoPorGrupo=temClassificacaoPorGrupo
        self.temClassificacao=temClassificacao

    def json(self):
        return {
            'camp_id': self.camp_id,
            'urlLogo': self.url_logo,
            'sdeSlug': self.de_slug,
            'categoria': self.categoria,
            'temporada': self.temporada,
            'nomeDaTaca': self.nomeDaTaca,
            'tipoDeColeta': self.tipoDeColeta,
            'nome': self.nome,
            'faseAtual': self.faseAtual,
            'rodadaAtual': self.rodadaAtual,
            'pais': self.pais,
            'ativo': self.ativo,
            'apelido': self.apelido,
            'campeonato_id': self.campeonato_id,
            'edicao_id': self.edicao_id,
            'quantidadeDeEquipes': self.quantidadeDeEquipes,
            'quantidadeDeRodadas': self.quantidadeDeRodadas,
            'temClassificacaoPorGrupo': self.temClassificacaoPorGrupo,
            'temClassificacao': self.temClassificacao
        }

    @classmethod
    def find_campeonato(cls, camp_id):
        campeonato = cls.query.filter_by(camp_id=camp_id).first()
        if campeonato:
            return campeonato
        return None

    def save_campeonato(self):
        banco.session.add(self)
        banco.session.commit()

    def update_campeonato(self, camp_id,urlLogo,sdeSlug,categoria,temporada,nomeDaTaca,tipoDeColeta,nome,faseAtual,rodadaAtual,pais,ativo,apelido,campeonato_id,edicao_id,quantidadeDeEquipes,quantidadeDeRodadas,temClassificacaoPorGrupo,temClassificacao):
        self.camp_id=camp_id,
        self.urlLogo=urlLogo
        self.sdeSlug=sdeSlug
        self.categoria=categoria
        self.temporada=temporada
        self.nomeDaTaca=nomeDaTaca
        self.tipoDeColeta=tipoDeColeta
        self.nome=nome
        self.faseAtual=faseAtual
        self.rodadaAtual=rodadaAtual
        self.pais=pais
        self.ativo=ativo
        self.apelido=apelido
        self.campeonato_id=campeonato_id,
        self.edicao_id=edicao_id
        self.quantidadeDeEquipes=quantidadeDeEquipes
        self.quantidadeDeRodadas=quantidadeDeRodadas,
        self.temClassificacaoPorGrupo=temClassificacaoPorGrupo
        self.temClassificacao=temClassificacao

    def delete_campeonato(self):
        banco.session.delete(self)
        banco.session.commit()