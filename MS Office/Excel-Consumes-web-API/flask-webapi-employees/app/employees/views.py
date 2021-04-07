from flask import jsonify, request
from . import empbp
from app import db
from .models import EmpMaster


def emp2dict(emp):
    return dict(
        EMP_ID=emp.EMP_ID,
        FIRST_NAME = emp.FIRST_NAME,
        LAST_NAME = emp.LAST_NAME,
        GENDER=emp.GENDER,
        AGE=emp.AGE,
        EMAIL=emp.EMAIL,
        EDUCATION=emp.EDUCATION,
        PHONE_NR=emp.PHONE_NR,
        MARITAL_STAT=emp.MARITAL_STAT,
        NR_OF_CHILDREN=emp.NR_OF_CHILDREN
    )


@empbp.route('/', methods=['GET'])
def list_employees():
    emps = EmpMaster.query.all()
    return jsonify({'rows': list(map(emp2dict, emps))})


@empbp.route('/<empid>', methods=['GET'])
def find_employee_by_id(empid):
    emp = EmpMaster.query.get(empid)
    return jsonify(emp2dict(emp))


@empbp.route('/create', methods=['POST'])
def create_employee():
    payload = request.get_json()
    if payload is None:
        return jsonify({
            'success': 'false',
            'message': 'Request is empty.'
        }), 400

    emp_check = EmpMaster.query.get(payload['EMP_ID'])
    if not emp_check is None:
        return jsonify({
            'success': 'false',
            'message': 'Employee already exists.'
        }), 400

    emp = EmpMaster(
        EMP_ID=payload['EMP_ID'],
        FIRST_NAME = payload['FIRST_NAME'],
        LAST_NAME = payload['LAST_NAME'],
        GENDER=payload['GENDER'],
        AGE=payload['AGE'],
        EMAIL=payload['EMAIL'],
        PHONE_NR=payload['PHONE_NR'],
        EDUCATION=payload['EDUCATION'],
        MARITAL_STAT=payload['MARITAL_STAT'],
        NR_OF_CHILDREN=payload['NR_OF_CHILDREN']
    )

    db.session.add(emp)
    db.session.commit()

    return jsonify({
        'success': 'true',
        'message': 'Employee was created successfully.'
    }), 201


@empbp.route('/<empid>', methods=['PUT'])
def modfiy_employee(empid):
    payload = request.get_json()
    if payload is None:
        return jsonify({
            'success': 'false',
            'message': 'Request is empty.'
        }), 400

    emp = EmpMaster.query.get(empid)
    if emp is None:
        return jsonify({
            'success': 'false',
            'message': 'Employee does not exist.'
        }), 400

    emp.GENDER = payload['GENDER']
    emp.FIRST_NAME = payload['FIRST_NAME']
    emp.LAST_NAME = payload['LAST_NAME']
    emp.AGE = payload['AGE']
    emp.EMAIL = payload['EMAIL']
    emp.PHONE_NR = payload['PHONE_NR']
    emp.EDUCATION = payload['EDUCATION']
    emp.MARITAL_STAT = payload['MARITAL_STAT']
    emp.NR_OF_CHILDREN = payload['NR_OF_CHILDREN']

    db.session.commit()

    return jsonify({
        'success': 'true',
        'message': 'Employee was updated succesfully.'
    }), 200


@empbp.route('/<empid>', methods=['DELETE'])
def delete_employee(empid):
    emp = EmpMaster.query.get(empid)
    if emp is None:
        return jsonify({
            'success': 'false',
            'message': 'Employee does not exist.'
        }), 400

    db.session.delete(emp)
    db.session.commit()

    return jsonify({
        'success': 'true',
        'message': 'Employee was deleted successfully.'
    }), 204
