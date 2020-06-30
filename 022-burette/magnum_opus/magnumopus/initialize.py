from . import create_app
from .models import db

if __name__ == "__main__":
    # There are nicer ways around this, but this keeps it clear for an example
    app = create_app()

    with app.app_context():
        db.create_all()
