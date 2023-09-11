from app import app, db
from flask import render_template, redirect, flash, url_for
from app.forms import DataForm
from app.models import Type, Report


@app.route('/')
@app.route('/index')
def index():
    return render_template(f"{url_for('index')}.html", title='Начальная страница')


@app.route('/views')
def views():
    result = {'accrued': 0.0, 'payment': 0.0}

    dataset = Report.query.order_by(Report.date).all()
    for data in dataset:
        if data.data_type == 'Начислено':
            result['accrued'] += data.value
        else:
            result['payment'] += data.value

    result = round(result['accrued'] - result['payment'], 2)


    return render_template(f"{url_for('views')}.html", title='Сверка', dataset=dataset, result=result)


@app.route('/add', methods=['GET', 'POST'])
def add():
    select = ['', 'Начислено', 'Оплачено']
    form = DataForm()

    if form.validate_on_submit():
        d = form.date.data
        date_view = f"{d.day}.{d.month}.{d.year}"
        count = float(round(form.count.data, 2))

        try:
            t = Type.query.filter_by(type=form.datatype.data).first()
            r = Report(value=count, date=form.date.data, count_type=t)
            db.session.add(r)
            db.session.commit()
            flash('Даные записаны: {} {} - {} руб.'.format(form.datatype.data, date_view, count))
            return redirect(url_for('index'))

        except Exception as ex:
            flash(f'Даные не записаны - {ex}')

    return render_template(f"{url_for('add')}.html", title='Добавить данные', select=select, form=form)


@app.errorhandler(404)
def error_404(error):
    return render_template('error_404.html')