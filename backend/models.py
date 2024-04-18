from config import db


class Contact(db.Model):
    id = db.columm(db.Interger, primary_key=True)
    first_name = db.Collumn(db.String(80), unique=False, nullable=False)
    last_name = db.Collumn(db.String(80), unique=False, nullable=False)
    email = db.Collumn(db.String(120), unique=True, nullable=False)

    ## camel case to work with JSON (firstName)
    ## snake case to work with pthon (first_name)
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
