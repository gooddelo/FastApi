from typing import List, Union

import datetime as _dt
import pydantic as _pydantic

class IdentificationBase(_pydantic.BaseModel):
    first_name : str
    second_name : str
    third_name : Union[str, None] = None
    date_birh : _dt.datetime#.date
    sign_up_date: _dt.datetime
    gender: str
    

class IdentificationCreate(IdentificationBase):
    pass

class Identification(IdentificationBase):
    id: int
    client_id: int
    
    

    class Config:
        orm_mode = True

        
#----------------------------------------------------------
class NotesBase(_pydantic.BaseModel):
    notes : str
    
    

class NotesCreate(NotesBase):
    pass

class Notes(NotesBase):
    id: int
    client_id: int

    class Config:
        orm_mode = True

        
#----------------------------------------------------------
class SourceBase(_pydantic.BaseModel):
    Source : str
    
    

class SourceCreate(SourceBase):
    pass

class Source(SourceBase):
    id: int
    client_id: int

    class Config:
        orm_mode = True        
        
#----------------------------------------------------------
class ContraidicationsBase(_pydantic.BaseModel):
    contraidications : str
    
    

class ContraidicationsCreate(ContraidicationsBase):
    pass

class Contraidications(ContraidicationsBase):
    id: int
    client_id: int

    class Config:
        orm_mode = True

#----------------------------------------------------------
class TelegramBase(_pydantic.BaseModel):
    isSendable : Union[bool, None] = None
    
    

class TelegramCreate(TelegramBase):
    pass

class Telegram(TelegramBase):
    id: int
    client_id: int
    #telegram_id: int

    class Config:
        orm_mode = True

#----------------------------------------------------------
'''class Phone_numberBase(_pydantic.BaseModel):
    formated_number : str
    
    

class Phone_numberCreate(Phone_numberBase):
    pass

class Phone_number(Phone_numberBase):
    etalon_number: str

    class Config:
        orm_mode = True'''
#----------------------------------------------------------
class ClientBase(_pydantic.BaseModel):
    email : str
    number : str
    advetisment_souce_id : int

class ClientCreate(ClientBase):
    password: str

class Client(ClientBase):
    id: int
    indetification: List[Identification] = []
    notes: List[Notes] = []
    contraidications: List[Contraidications] = []
    source: List[Source] = []
    telegram: List[Telegram] = []
    #phone: List[Phone_number] = []

    class Config:
        orm_mode = True
#----------------------------------------------------------

