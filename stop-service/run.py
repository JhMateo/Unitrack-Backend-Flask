from aplication import create_app, db
from aplication import models
from flask_migrate import Migrate
from flask_cors import CORS

app = create_app()

CORS(app)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)