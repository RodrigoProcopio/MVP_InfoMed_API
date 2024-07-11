from pydantic import BaseModel
from typing import List
from model.medicamento import Medicamento


class MedicamentoSchema(BaseModel):
    """ Define como um novo medicamento deve ser representado ao ser inserido.
    """
    id: int = 0
    medicine: str = "Aspirina 100mg"
    posology: str = "Tomar um comprimido após o almoço."
    doctor: str = "Dra. Leiza Hollas"
    specialty: str = "Cirurgia Cardíaca"


class MedicamentoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do medicamento.
    """
    medicine: str = "Aspirina 100Mg"


class MedicamentoIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a exclusão do
    medicamento pelo id.
    """
    id: int = 0


class ListagemMedicamentosSchema(BaseModel):
    """ Define como uma listagem de medicamentos será retornada.
    """
    medicamentos:List[MedicamentoSchema]


def apresenta_medicamentos(medicamentos: List[Medicamento]):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    result = []
    for medicamento in medicamentos:
        result.append({
            "id": medicamento.id,
            "medicine": medicamento.medicine,
            "posology": medicamento.posology,
            "doctor": medicamento.doctor,
            "specialty": medicamento.specialty
        })

    return {"medicamentos": result}


class MedicamentoViewSchema(BaseModel):
    """ Define como um medicamento será retornado.
    """
    id: int = 0
    medicine: str = "Aspirina 100mg"
    posology: str = "Tomar um comprimido após o almoço."
    doctor: str = "Dra. Leiza Hollas"
    specialty: str = "Cirurgia Cardíaca"
   

class MedicamentoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mensagem: str
    medicine: str

class MedicamentoDelIdSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mensagem: str
    id: int

def apresenta_medicamento(medicamento: Medicamento):
    """ Retorna uma representação do medicamento seguindo o schema definido em
        MedicamentoViewSchema.
    """
    return {
        "id": medicamento.id,
        "medicine": medicamento.medicine,
        "posology": medicamento.posology,
        "doctor": medicamento.doctor,
        "specialty": medicamento.specialty
    }
