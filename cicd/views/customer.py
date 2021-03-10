from cicd import app
from flask import request, jsonify
from cicd.models import customer


@app.route('/')
def handler():
    return 'Hello World!!'


@app.route('/customers', methods=['GET', 'POST'])
def customer_handler():

    if request.method == 'GET':
        customers = customer.get_all_customers()
        return jsonify(customers), 200

    elif request.method == 'POST':
        data = request.get_json()

        customer_id = customer.create_customer(
            name=data.get('name'),
            address=data.get('address'),
            email=data.get('email'),
            gender=data.get('gender')
        )

        response = {
            'status_code': 201,
            'message': "Customer created successfully!!",
            'customer_id': customer_id
        }
        return jsonify(response), 201

