from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    name = 'David'
    course = 'Python web'
    is_premium = False
    courses = ['Python', 'Ruby', 'Java', 'Elixir']

    return render_template('index.html', username=name, course_name=course, is_premium=is_premium, courses=courses)

# @app.route('/usuario/<username>')
# def usuario(username):
    return 'Hola ' + username


@app.route('/usuario/<last_name>/<name>/<int:age>')
def usuario(last_name, name, age):
    return 'Hola ' + last_name + ' ' + name + ' ' + str(age)


@app.route('/datos')
def datos():
    nombre = request.args.get('nombre', '') #Dic
    curso = request.args.get('curso', '')
    return 'Listado de datos: ' + nombre + ' ' + curso

if __name__ == '__main__':
    app.run(debug=True, port=9000)
