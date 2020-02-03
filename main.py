from app import app
from models import db, Translation


if __name__ == '__main__':

    # Create the tables.
    db.connect()
    print(db.create_tables([Translation]))
    db.close()
    app.run(debug=True)
