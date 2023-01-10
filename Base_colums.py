from sqlalchemy import Column, Integer, String, Date, Boolean, Time, ForeignKey, create_engine
from sqlalchemy.orm import relationship, Session
from datetime import date, time
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import create_engine

Base = declarative_base()

class Boss(Base):
    __tablename__ = 'bosses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    midname = Column(String)
    birthday = Column(Date)
    mail = Column(String)
    password = Column(String)
    phone = Column(String)
    site_link = Column(String)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    inn = Column(String)
    name = Column(String)
    legal_address = Column(String)
    actual_address = Column(String)
    contact_information = Column(String)

class TradePoint(Base):
    __tablename__ = 'trade_points'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    phone = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))
    employees = relationship('Employee', backref='trade_point')
    admins = relationship('Admin', backref='trade_point')
    devices = relationship('Device', backref='trade_point')

class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    serial_number = Column(String)
    trade_point_id = Column(Integer, ForeignKey('trade_points.id'))

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    midname = Column(String)
    birthday = Column(Date)
    mail = Column(String)
    password = Column(String)
    phone = Column(String)
    trade_point_id = Column(Integer, ForeignKey('trade_points.id'))
    ratings = relationship('Rating', backref='employee')
    admin_id = Column(Integer, ForeignKey('admins.id'))

class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    midname = Column(String)
    birthday = Column(Date)
    mail = Column(String)
    password = Column(String)
    phone = Column(String)
    trade_point_id = Column(Integer, ForeignKey('trade_points.id'))
    employees = relationship('Employee', backref='admin')
    ratings = relationship('Rating', backref='admin')

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    time = Column(Time)
    name = Column(String)
    geocode = Column(String)
    set_contact = Column(Boolean)
    identification_of_needs = Column(Boolean)
    product_presentation = Column(Boolean)
    bonus_program = Column(Boolean)
    completion = Column(Boolean)
    thanks_for_purchase = Column(Boolean)
    suggestion_add = Column(Boolean)
    final_value = Column(Boolean)
    suggested_actions = Column(Boolean)
    undesirable_phrases = Column(Boolean)
    presence_of_a_match = Column(Boolean)
    percent_execution = Column(Boolean)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    admin_id = Column(Integer, ForeignKey('admins.id'))

#engine = create_engine("sqlite://", echo=True, future=True)
engine = create_engine('sqlite:///sample_db.sqlite')
Base.metadata.create_all(engine)

# Insert some sample data
session = Session(bind=engine)

boss = Boss(name='Ваня', surname='Смертельная', midname='Борода', birthday=date(1488,12,18), mail='killerpussies@example.com', password='Я_КРУТОЕ_ИМЯ_БЛЯТЬ')
session.add(boss)

company = Company(inn='1234567890', name='Gooddelo', legal_address='1234 adress', actual_address='1234 adress', contact_information='9992929929292')
session.add(company)

tp1 = TradePoint(address='Биба', phone='228', company_id=1)
session.add(tp1)

tp2 = TradePoint(address='Боба', phone='4445', company_id=1)
session.add(tp2)

employee1 = Employee(name='Серёга', surname='Шоманский', midname='Дух', birthday=date(1228,3,12), mail='SuperPidor@example.com', password='Assasas', trade_point_id=1, admin_id=1)
session.add(employee1)

employee2 = Employee(name='Паша', surname='Повелитель', midname='Фронтенда', birthday=date(5552,4,9), mail='PashaKrut@example.com', password='psssasd', trade_point_id=1, admin_id=1)
session.add(employee2)

admin1 = Admin(name='Ваня', surname='Смертельная', midname='Борода', birthday=date(1488,12,18), mail='killerpussies@example.com', password='Я КРУТОЕ ИМЯ БЛЯТЬ', trade_point_id=1)
session.add(admin1)

admin2 = Admin(name='Полина', surname='Око', midname='Мангуста', birthday=date(1220,2,2), mail='POLINKA_PIPKA@example.com', password='aaaaaaaaaaaaaaA', trade_point_id=2)
session.add(admin2)

device1 = Device(serial_number='12345', trade_point_id=1)
session.add(device1)

device2 = Device(serial_number='67890', trade_point_id=2)
session.add(device2)

rating1 = Rating(date=date(2023,10,1), time=time(17,27,53), name='Серёга', geocode='1234 adress', set_contact=True, identification_of_needs=True, product_presentation=True, bonus_program=True, completion=True, thanks_for_purchase=True, suggestion_add=True, final_value=True, suggested_actions=True, undesirable_phrases=True, presence_of_a_match=True, percent_execution=True, employee_id=1, admin_id=1)
session.add(rating1)


session.commit()

# Querying data

# Get all Bosses
bosses = session.query(Boss).all()
for boss in bosses:
    print(boss.id, boss.name, boss.surname, boss.midname)
    
# Get all Companys
companies = session.query(Company).all()
for company in companies:
    print(company.id, company.inn, company.name)
    
# Get all TradePoints by company id
trade_points = session.query(TradePoint).filter_by(company_id=1).all()
for tp in trade_points:
    print(tp.id, tp.address, tp.phone)
    
# Get all Employees by TradePoint id
employees = session.query(Employee).filter_by(trade_point_id=1).all()
for emp in employees:
    print(emp.id, emp.name, emp.surname, emp.midname)
    
# Get an Admin by id
admin = session.query(Admin).get(1)
print(admin.id, admin.name, admin.surname, admin.midname)

# Get the ratings related to an employee
employee = session.query(Employee).get(1)
for rating in employee.ratings:
    print(rating.id, rating.name)