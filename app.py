from flask_openapi3 import OpenAPI, Info, Tag
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from urllib.parse import unquote
from model import *
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API InfoMed", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags
home_tag = Tag(name="Documentação Swagger", description="Documentação estilo Swagger.")
medicamento_tag = Tag(name="Medicações", description="Adição, visualização e remoção de medicamentos na base de dados.")
consulta_tag = Tag(name="Consultas Médicas", description="Adição, visualização e remoção de Consultas Médicas na base de dados.")

def home():
    """Redireciona para documentação da API no estilo Swagger."""
    return redirect('/openapi/swagger')

@app.post('/add_medicamento', tags=[medicamento_tag],
          responses={"200": MedicamentoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_medicamento(form: MedicamentoSchema):
    """Adiciona um novo Medicamento à base de dados.

    Retorna uma representação dos medicamentos cadastrados.
    """
    # Capitaliza a primeira letra de cada palavra no nome do medicamento
    medicine_name = form.medicine.title()

    medicamento = Medicamento(
        medicine=medicine_name,
        posology=form.posology,
        doctor=form.doctor,
        specialty=form.specialty
    )
    
    logger.debug(f"Adicionando medicamento: '{medicamento.medicine}'")
    try:
        # Criando conexão com a base
        session = Session()
        # Adicionando medicamento
        session.add(medicamento)
        # Efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado medicamento: '{medicamento.medicine}'")
        return apresenta_medicamento(medicamento), 200

    except IntegrityError as e:
        # A duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Um medicamento com o mesmo nome já existe."
        logger.warning(f"Erro ao adicionar medicamento '{medicamento.medicine}', {error_msg}")
        return {"mensagem": error_msg}, 409

    except Exception as e:
        # Caso ocorra um erro fora do previsto
        error_msg = "Não foi possível salvar um novo medicamento."
        logger.warning(f"Erro ao adicionar medicamento '{medicamento.medicine}', {error_msg}")
        return {"mensagem": error_msg}, 400
    
@app.get('/get_medicamentos', tags=[medicamento_tag],
         responses={"200": ListagemMedicamentosSchema, "404": ErrorSchema})
def get_medicamentos():
    """Faz a busca por todos os Medicamentos cadastrados.

    Retorna uma representação da listagem de medicamentos.
    """
    logger.debug(f"Coletando medicamentos ")

    session = Session()
    medicamentos = session.query(Medicamento).all()

    if not medicamentos:
        return {"medicamentos": []}, 200
    else:
        logger.debug(f"%d medicamentos encontrados" % len(medicamentos))
        return apresenta_medicamentos(medicamentos), 200


@app.get('/get_medicamento', tags=[medicamento_tag],
         responses={"200": MedicamentoViewSchema, "404": ErrorSchema})
def get_produto(query: MedicamentoBuscaSchema):
    """Faz a busca por um Medicamento a partir do nome do medicamento.

    Retorna uma representação dos medicamentos cadastrados.
    """
    medicamento_medicine = query.medicine.strip().lower()  # Remove espaços e converte para minúsculas
    logger.debug(f"Coletando dados sobre medicamento #{medicamento_medicine}")

    session = Session()

    # Fazendo a busca, usando ilike para busca insensível a maiúsculas/minúsculas
    medicamento = session.query(Medicamento).filter(func.lower(Medicamento.medicine).ilike(f"%{medicamento_medicine}%")).first()

    if not medicamento:
        error_msg = "Medicamento não encontrado."
        logger.warning(f"Erro ao buscar medicamento '{medicamento_medicine}', {error_msg}")
        return {"mensagem": error_msg}, 404
    else:
        logger.debug(f"Medicamento encontrado: '{medicamento.medicine}'")
        return apresenta_medicamento(medicamento), 200

@app.delete('/del_medicamento', tags=[medicamento_tag],
            responses={"200": MedicamentoDelSchema, "404": ErrorSchema})
def del_medicamento(query: MedicamentoBuscaSchema):
    """Deleta um Medicamento a partir do nome do medicamento informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    medicamento_medicine = unquote(query.medicine.strip())
    logger.debug(f"Deletando dados do medicamento #{medicamento_medicine}")

    session = Session()

    count = session.query(Medicamento).filter(Medicamento.medicine == medicamento_medicine).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado medicamento #{medicamento_medicine}")
        return {"message": "Medicamento removido", "id": medicamento_medicine}
    else:
        error_msg = "Medicamento não encontrado."
        logger.warning(f"Erro ao deletar medicamento '{medicamento_medicine}', {error_msg}")
        return {"mensagem": error_msg}, 404

@app.delete('/del_medicamento_id', tags=[medicamento_tag],
            responses={"200": MedicamentoDelIdSchema, "404": ErrorSchema})
def del_medicamento_id(query: MedicamentoIdSchema):
    """Deleta um Medicamento a partir do id do medicamento informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    medicamento_id = query.id
    logger.debug(f"Deletando dados sobre medicamento #{medicamento_id}")

    session = Session()

    count = session.query(Medicamento).filter(Medicamento.id == medicamento_id).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado medicamento #{medicamento_id}")
        return {"mensagem": "Medicamento removido", "id": medicamento_id}
    else:
        error_msg = "Medicamento não encontrado."
        logger.warning(f"Erro ao deletar medicamento '{medicamento_id}', {error_msg}")
        return {"mensagem": error_msg}, 404

# Rotas da Agenda de Consultas Médicas:

@app.post('/add_consulta', tags=[consulta_tag],
          responses={"200": ConsultaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_consulta(form: ConsultaSchema):
    """Adiciona uma nova Consulta Médica à base de dados.

    Retorna uma representação das Consultas Médicas cadastradas.
    """
    consulta = Consulta(
        doctor_name=form.doctor_name,
        specialty=form.specialty,
        date=form.date,
        time=form.time
    )
        
    logger.debug(f"Adicionando consulta médica: '{consulta.doctor_name}'")
    try:
        # Criando conexão com a base
        session = Session()
        # Adicionando consulta
        session.add(consulta)
        # Efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionada consulta médica: '{consulta.doctor_name}'")
        return apresenta_consulta(consulta), 200

    except Exception as e:
        # Caso ocorra um erro fora do previsto
        error_msg = "Não foi possível salvar uma nova consulta médica."
        logger.warning(f"Erro ao adicionar consulta médica '{consulta.doctor_name}', {error_msg}")
        return {"mensagem": error_msg}, 400  

@app.put('/update_consulta', tags=[consulta_tag])
def update_consulta(query: ConsultaIdSchema, form: ConsultaUpdateSchema):
    """Atualiza uma Consulta Médica existente na base de dados.

    Retorna uma representação da Consulta Médica atualizada.
    """
    consulta_id = query.id
    logger.debug(f"Atualizando consulta Médica: ID '{consulta_id}'")

    session = Session()
    consulta = session.query(Consulta).filter(Consulta.id == consulta_id).first()

    if not consulta:
        error_msg = "Consulta Médica não encontrada."
        logger.warning(f"Erro ao atualizar Consulta Médica #{consulta_id}: {error_msg}")
        raise HTTPException(status_code=404, detail=error_msg)

    try:
        consulta.doctor_name = form.doctor_name
        consulta.specialty = form.specialty
        consulta.date = form.date
        consulta.time = form.time
        
        session.commit()
        logger.debug(f"Consulta Médica atualizada: ID '{consulta_id}'")

        # Retorna um dicionário que pode ser convertido em JSON
        return apresenta_consulta(consulta)

    except Exception as e:
        error_msg = "Não foi possível atualizar a Consulta Médica."
        logger.warning(f"Erro ao atualizar Consulta Médica #{consulta_id}: {error_msg}")
        raise HTTPException(status_code=400, detail=error_msg)

@app.get('/get_consultas', tags=[consulta_tag],
         responses={"200": ListagemConsultasSchema, "404": ErrorSchema})
def get_consultas():
    """Faz a busca por todas as Consultas Médicas cadastradas.

    Retorna uma representação da listagem de Consultas Médicas.
    """
    logger.debug(f"Coletando Consultas Médicas ")

    session = Session()
    consultas = session.query(Consulta).all()

    if not consultas:
        return {"consultas": []}, 200
    else:
        logger.debug(f"%d Consultas Médicas encontradas" % len(consultas))
        return apresenta_consultas(consultas), 200
    
@app.delete('/del_consulta_id', tags=[consulta_tag],
            responses={"200": ConsultaDelIdSchema, "404": ErrorSchema})
def del_consulta_id(query: ConsultaIdSchema):
    """Deleta uma Consulta Médica a partir do id da Consulta Médica informada.

    Retorna uma mensagem de confirmação da remoção.
    """
    consulta_id = query.id
    logger.debug(f"Deletando dados sobre Consulta Médica #{consulta_id}")

    session = Session()

    count = session.query(Consulta).filter(Consulta.id == consulta_id).delete()
    session.commit()

    if count:
        logger.debug(f"Deletada consulta Médica #{consulta_id}")
        return {"mensagem": "Consulta Médica removida", "id": consulta_id}
    else:
        error_msg = "Consulta Médica não encontrada."
        logger.warning(f"Erro ao deletar Consulta Médica #{consulta_id}, {error_msg}")
        return {"mensagem": error_msg}, 404
