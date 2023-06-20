#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

# @app.route('/count/<int:parameter>')
# def count(parameter):
#     output = '\n'.join(str(i) for i in range(parameter + 1))
#     return output

@app.route('/count/<int:parameter>')
def count(parameter):
    count = ''
    for i in range(parameter):
        count += f'{i}\n'
    return count

@app.route('/math/<parameters>')
def math_operation(parameters):
    # Return a 404 status code
    return '', 404

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return str(num1 + num2)
    
    elif operation == '-':
        return str(num1 - num2)

    elif operation == '*':
        return str(num1 * num2)

    elif operation == 'div':
        return str(num1 / num2)

    elif operation == '%':
        return str(num1 % num2)

    return 'Operation not recognized. Please use one of the following: + - * div %'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
