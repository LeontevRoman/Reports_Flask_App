from app import app, db
from app.models import Type, Report


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'DataType': Type, 'Report': Report}


if __name__ == '__main__':
    app.run(debug=True)
