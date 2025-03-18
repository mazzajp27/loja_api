from sqlalchemy import Boolean, Integer, Column, ForeignKey, String
from database import Base

class Cliente(Base):
    __tablename__ = 'cliente2'
    
    id_cliente = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer, index=True)
    sexo = Column(String, index=True)
    email = Column(String, index=True)
    
    