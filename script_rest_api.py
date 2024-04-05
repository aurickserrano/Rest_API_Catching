from flask import Flask, request, jsonify
from flask_caching import Cache 

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Simulando uma lista de funcionários em um banco de dados
employees = [
    {'id': 1, 'firstName': 'Jane', 'lastName': 'Smith', 'age': 20},
    {'id': 2, 'firstName': 'John', 'lastName': 'Smith', 'age': 30},
    {'id': 3, 'firstName': 'Mary', 'lastName': 'Green', 'age': 50}
]

@app.route('/employees', methods=['GET'])
@cache.cached(timeout=300)  # Cache por 5 minutos
def get_employees():
    """
    Endpoint para obter todos os funcionários.
    Suporta filtragem por firstName, lastName e age.
    """
    filtered_employees = employees

    # Filtragem por parâmetros de consulta
    for key, value in request.args.items():
        if key in ['firstName', 'lastName']:
            filtered_employees = [emp for emp in filtered_employees if emp[key] == value]
        elif key == 'age':
            filtered_employees = [emp for emp in filtered_employees if emp[key] == int(value)]

    return jsonify(filtered_employees)

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    """
    Endpoint para obter um funcionário por ID.
    """
    employee = next((emp for emp in employees if emp['id'] == employee_id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({'error': 'Employee not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
