from sqlalchemy import Column, String, Integer, DateTime
from model import Base

class Consulta(Base):
    __tablename__ = 'consulta'

    id = Column("pk_consulta", Integer, primary_key=True)  # Define a coluna 'id' como a chave primária.
    doctor_name = Column(String(140))
    specialty = Column(String(140))
    date = Column(String(140))
    time = Column(String(140))

    def __init__(self, doctor_name: str, specialty: str, date: str, time: str = None):
        self.doctor_name = doctor_name
        self.specialty = specialty
        self.date = date
        self.time = time