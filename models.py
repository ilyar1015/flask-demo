# coding: utf-8
from app import db


class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.String(32, 'utf8_bin'), primary_key=True)
    num = db.Column(db.String(255, 'utf8_bin'))
    password = db.Column(db.String(255, 'utf8_bin'))


class Emp(db.Model):
    __tablename__ = 'emp'

    id = db.Column(db.String(32, 'utf8_bin'), primary_key=True)
    num = db.Column(db.String(255, 'utf8_bin'))
    password = db.Column(db.String(255, 'utf8_bin'))
    name = db.Column(db.String(255, 'utf8_bin'))
    remark = db.Column(db.String(255, 'utf8_bin'))
    specialty = db.Column(db.String(255, 'utf8_bin'))


class RepairOrder(db.Model):
    __tablename__ = 'repair_order'

    id = db.Column(db.String(32, 'utf8_bin'), primary_key=True)
    initiator_id = db.Column(db.String(32, 'utf8_bin'))
    receiver_id = db.Column(db.String(32, 'utf8_bin'))
    avatar = db.Column(db.String(255, 'utf8_bin'))
    start_time = db.Column(db.DateTime)
    recive_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    address = db.Column(db.String(255, 'utf8_bin'))
    maintenance_affairs = db.Column(db.String(255, 'utf8_bin'))
    remark = db.Column(db.String(255, 'utf8_bin'))
    status = db.Column(db.String(2, 'utf8_bin'))


class Stu(db.Model):
    __tablename__ = 'stu'

    id = db.Column(db.String(32, 'utf8_bin'), primary_key=True)
    num = db.Column(db.String(255, 'utf8_bin'), comment='??')
    password = db.Column(db.String(255, 'utf8_bin'))
    name = db.Column(db.String(255, 'utf8_bin'))
    institute = db.Column(db.String(255, 'utf8_bin'))
