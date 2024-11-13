from faker import Faker
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from app import create_app, db
from app.models import user_credentials

fake = Faker()
app = create_app()
app.app_context().push()

db.create_all()


def generate_fake_data(count=5):
    for _ in range(count):
        user_in_company = fake.boolean()
        u = user_credentials(
            user_firstname=fake.first_name(),
            user_lastname=fake.last_name(),
            user_email=fake.email(),
            user_password=generate_password_hash("password"),
            user_in_company=user_in_company,
            user_company=fake.company() if user_in_company else None,
        )
        db.session.add(u)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


generate_fake_data()
