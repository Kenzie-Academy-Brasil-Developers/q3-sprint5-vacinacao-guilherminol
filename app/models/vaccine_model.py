from sqlalchemy import Column, DateTime, String
from app.configs.database import db
from dataclasses import dataclass
import datetime


@dataclass
class VaccineRecord(db.Model):
    __tablename__ = "vaccine_cards"

    cpf : str
    name : str
    first_shot_date : str
    second_shot_date : str
    vaccine_name : str
    health_unit_name : str

    cpf = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)

    @classmethod
    def checkdata(cls,data): 
        return all(isinstance(x, str) for x in data)

    @classmethod
    def normalize(cls,data):

        for key,value in data.items():
            data[key] = value.capitalize()

        return data