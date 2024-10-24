from workout_api_dio.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Definir chave primária corretamente
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    proprietario: Mapped[str] = mapped_column(String(60), nullable=False)
    endereco: Mapped[str] = mapped_column(String(30), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship("AtletaModel", back_populates='centro_treinamento')