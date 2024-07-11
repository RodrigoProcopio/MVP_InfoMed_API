from pydantic import BaseModel
from typing import List
from model.consulta import Consulta

class ConsultaSchema(BaseModel):
    """ Define como uma nova consulta deve ser representada ao ser inserida.
    """
    id: int = 0
    doctor_name: str = "Dra. Leiza"
    specialty: str = "Cirurgia Cardíaca"
    date: str = "27/08/2017"  
    time: str = "08:00" 

class ConsultaViewSchema(BaseModel):
    """ Define como uma consulta será retornada.
    """
    id: int
    doctor_name: str
    specialty: str
    date: str  
    time: str  

class ConsultaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca de uma consulta.
    """
    doctor_name: str = "Dra. Maria Silva"

class ConsultaIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa o ID de uma consulta para deleção.
    """
    id: int
    
class ListagemConsultasSchema(BaseModel):
    """ Define como uma listagem de consultas será retornada.
    """
    consultas: List[ConsultaViewSchema]

class ConsultaDelIdSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mensagem: str
    id: int

class ConsultaUpdateSchema(BaseModel):  
    id: int = 0
    doctor_name: str = "Dra. Leiza"
    specialty: str = "Cirurgia Cardíaca"
    date: str = "27/08/2017"  
    time: str = "08:00" 

def apresenta_consultas(consultas: List[Consulta]):
    """ Retorna uma representação das consultas seguindo o schema definido em
        ConsultaViewSchema.
    """
    result = []
    for consulta in consultas:
        result.append({
            "id": consulta.id,
            "doctor_name": consulta.doctor_name,
            "specialty": consulta.specialty,
            "date": consulta.date,
            "time": consulta.time
        })

    return {"consultas": result}

def apresenta_consulta(consulta: Consulta):
    """ Retorna uma representação da consulta seguindo o schema definido em
        ConsultaViewSchema.
    """
    return {
        "id": consulta.id,
        "doctor_name": consulta.doctor_name,
        "specialty": consulta.specialty,
        "date": consulta.date,
        "time": consulta.time
    }
