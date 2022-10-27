import datetime as _dt
from email.policy import default
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import database as _database

class Client(_database.Base):
    __tablename__ = "client"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=False, index=True)
    hashed_password = _sql.Column(_sql.String)
    number = _sql.Column(_sql.String, index=True)
    advetisment_souce_id = _sql.Column(_sql.Integer, index=True)
    last_active_date = _sql.Column(_sql.String, index=True)

    indetification = _orm.relationship("Identification", back_populates="client_data")
    notes = _orm.relationship("Notes", back_populates="client_notes")
    contraidications = _orm.relationship("Contraidications", back_populates="client_contraidications")
    source = _orm.relationship("Source", back_populates="client_Source")
    telegram = _orm.relationship("Telegram", back_populates="client_telegram")
    #number = _orm.relationship("Phone_number", back_populates="client_number")

class Identification(_database.Base):
    __tablename__ = "indetification_data"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    first_name = _sql.Column(_sql.String, index=True)
    second_name = _sql.Column(_sql.String, index=True)
    third_name = _sql.Column(_sql.String, index=True)
    date_birh = _sql.Column(_sql.DateTime)
    sign_up_date = _sql.Column(_sql.DateTime)
    gender = _sql.Column(_sql.String, index=True)
    client_id = _sql.Column(_sql.Integer, _sql.ForeignKey("client.id"))

    client_data = _orm.relationship("Client", back_populates="indetification")

class Notes(_database.Base):
    __tablename__ = "notes"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    notes = _sql.Column(_sql.String, index=True)
    client_id = _sql.Column(_sql.Integer, _sql.ForeignKey("client.id"))

    client_notes = _orm.relationship("Client", back_populates="notes")


class Contraidications(_database.Base):
    __tablename__ = "contraidications"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    contraidications = _sql.Column(_sql.String, index=True)
    client_id = _sql.Column(_sql.Integer, _sql.ForeignKey("client.id"))

    client_contraidications = _orm.relationship("Client", back_populates="contraidications")

class Source(_database.Base):
    __tablename__ = "source"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    client_id = _sql.Column(_sql.Integer, _sql.ForeignKey("client.id"))#, primary_key=True,)
    Source = _sql.Column(_sql.String, index=True)
    

    client_Source = _orm.relationship("Client", back_populates="source")


class Telegram(_database.Base):
    __tablename__ = "telegram"
    id = _sql.Column(_sql.Integer, primary_key=True, index = True)
    client_id = _sql.Column(_sql.Integer, _sql.ForeignKey("client.id"))
    #telegram_id = _sql.Column(_sql.Integer, index = True)
    isSendable = _sql.Column(_sql.Boolean, default=None)

    client_telegram = _orm.relationship("Client", back_populates="telegram")

    
'''class Phone_number(_database.Base):
    __tablename__ = "phone_number"
    id = _sql.Column(_sql.Integer, primary_key=True, index = True)
    etalon_number = _sql.Column(_sql.Integer, _sql.ForeignKey("client.id"))
    formated_number = _sql.Column(_sql.String, index=True)

    client_number = _orm.relationship("Client", back_populates="number")'''
    