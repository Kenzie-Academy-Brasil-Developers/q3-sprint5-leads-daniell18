from dataclasses import dataclass
from sqlalchemy import Column,Integer,String,DateTime
from app.config.database import db
@dataclass
class Leads (db.Model):
    __tablename__='Leads'
    id=Column(Integer,primary_key=True)
    name:str=Column(String,nullable=False)
    email:str=Column(String,nullable=False,unique=True)
    phone:str=Column(String,nullable=False,unique=True)
    creation_date:str=Column(DateTime,nullable=True)
    last_visit:str=Column(DateTime,nullable=True)
    visits:int=Column(Integer,nullable=True,default=1)