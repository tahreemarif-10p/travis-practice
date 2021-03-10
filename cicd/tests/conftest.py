import pytest
from cicd import app as flask_app
from cicd import db


@pytest.fixture
def app():
    print('\napp is creating')
    yield flask_app


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client


@pytest.fixture
def empty_db(app):
    print('\ndatabase is creating')
    db.create_all()
    yield db

    # teardown
    db.session.remove()
    db.drop_all()
    print('\ndatabase is destroying')
