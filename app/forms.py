from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, DateField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):
    datatype = StringField("Вид данных", validators=[DataRequired(message='Выберите значиние из списка')])
    count = DecimalField('Сумма', validators=[DataRequired(message='Введите сумму'),
                                              NumberRange(min=1, message="Значение не может быть отрицательным или равным 0")])
    date = DateField('Дата внесения данных', validators=[DataRequired(message='Выберите дату отправки данных')])
    submit = SubmitField('Отправить данные')
