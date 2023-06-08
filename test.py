import pytest

from flask import template_rendered

from app import app

 



@pytest.fixture

def client():

    with app.test_client() as client:

        yield client

 



def test_index_page(client):

    response = client.get('/')

    assert response.status_code == 200

    assert b"Employees" in response.data

 



def test_add_page(client):

    response = client.get('/add')

    assert response.status_code == 200

    assert b"Add Employee" in response.data

 



def test_add_employee(client):

    data = {

        'name': 'John Doe',

        'gender': 'Male',

        'address': '123 Street',

        'phone': '1234567890',

        'salary': '5000',

        'department': 'IT'

    }

 

    response = client.post('/add', data=data, follow_redirects=True)

    assert response.status_code == 200

    assert b"John Doe" in response.data

 



def test_delete_employee(client):

    # Assuming there's an employee with id=1 in the database

    data = {'emp_id': '1'}

    response = client.post('/delete', data=data, follow_redirects=True)

    assert response.status_code == 200

    assert b"Employee deleted successfully" in response.data

 



def test_edit_page(client):

    # Assuming there's an employee with id=1 in the database

    response = client.get('/edit/1')

    assert response.status_code == 200

    assert b"Edit Employee" in response.data

 



def test_edit_employee(client):

    # Assuming there's an employee with id=1 in the database

    data = {

        'name': 'Jane Doe',

        'gender': 'Female',

        'address': '456 Street',

        'phone': '9876543210',

        'salary': '6000',

        'department': 'HR'

    }

 

    response = client.post('/edit/1', data=data, follow_redirects=True)

    assert response.status_code == 200

    assert b"Jane Doe" in response.data

 



# Custom assertion to check if a template is rendered

def assert_template_rendered(template_name):

    for template, context in template_rendered.send(app):

        if template.name == template_name:

            return

    pytest.fail(f"Template '{template_name}' not rendered")

 



def test_templates():

    with app.test_request_context():

        # Test if the 'index.html' template is rendered

        app.preprocess_request()

        assert_template_rendered('index.html')

 

        # Test if the 'add.html' template is rendered

        app.preprocess_request()

        assert_template_rendered('add.html')

 

        # Test if the 'edit.html' template is rendered

        app.preprocess_request()

        assert_template_rendered('edit.html')
