from datetime import date, datetime
from dataclasses import dataclass
from app.configs.database import db

from sqlalchemy import Column
from sqlalchemy.sql import sqltypes as sql

@dataclass
class LeadsModel(db.Model):
    id  : int
    name: str
    email: str
    phone: str
    last_visit: datetime
    visits: int
    creation_data: datetime

    __tablename__ = 'leads'
    id =            Column(sql.Integer, autoincrement=True, primary_key=True)
    name =          Column(sql.String, nullable=False)
    email =         Column(sql.String, unique=True ,nullable=False)
    phone =         Column(sql.String, unique=True ,nullable=False)
    creation_data = Column(sql.DateTime, default=datetime.utcnow())
    last_visit =    Column(sql.DateTime, default=datetime.utcnow())
    visits =        Column(sql.Integer, default=1)
    
    @staticmethod
    def serializer(leads: list["LeadsModel"])->list[dict]:
        serializer = [{
            'id': lead.id,
            'name': lead.name,
            'email': lead.email ,
            'prhone': lead.phone ,
            'creation_data': lead.creation_data ,
            'last_visit': lead.last_visit ,
            'visits': lead.visits 
        } for lead in leads
        ]
        return serializer