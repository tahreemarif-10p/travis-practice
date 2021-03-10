import enum
from datetime import datetime
from cicd import db


class Gender(enum.Enum):
    male = 'male'
    female = 'female'
    other = 'other'


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    gender = db.Column(db.Enum(Gender), default=Gender.male, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())


def create_customer(name, address, email, gender):
    """
    :param name:
    :param address:
    :param email:
    :param gender:
    :return:
    """
    customer = Customer(
        name=name,
        address=address,
        email=email,
        gender=gender
    )

    db.session.add(customer)
    db.session.commit()
    return customer.id


def get_all_customers():

    customers = Customer.query.all()
    response = []
    for customer in customers:
        response.append({
            "id": customer.id,
            "name": customer.name,
            "email": customer.email,
            "address": customer.address
        })

    return response

