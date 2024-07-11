from sqlalchemy import Column, String, Integer
from model import Base

class Medicamento(Base):
    __tablename__ = 'medicamento'

    id = Column("pk_medicamento", Integer, primary_key=True)  # Define a coluna 'id' como a chave primária.
    medicine = Column(String(140), unique=True) # nome do medicamento é único
    posology = Column(String(140))
    doctor = Column(String(140))
    specialty = Column(String(140))

    def __init__(self, medicine:str, posology:str, doctor:str, 
                 specialty:str = None):
        """
        Cria um Medicamento

        Arguments:
            medicine: nome do medicamento.
            posology: como utilizar a medicação.
            doctor: nome do(a) médico(a).
            specialty: especialidade do(a) médico(a).
        """
        self.medicine = medicine
        self.posology = posology
        self.doctor = doctor
        self.specialty = specialty

