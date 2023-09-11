from app import db
from datetime import date


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), index=True, unique=True)

    reports = db.relationship('Report', backref='count_type', lazy='dynamic')

    def __repr__(self):
        return f"Тип данных: {self.type}"


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    date = db.Column(db.Date, index=True, default=date.today())

    data_type = db.Column(db.String(20), db.ForeignKey('type.type'))

    def __repr__(self):
        return f"Запись: {self.data_type} - {self.value}, Дата: {self.date}"
