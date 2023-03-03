from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alumnos', methods=['GET','POST'])
def alumnos():
    if request.method == 'POST':
        boleta = request.form['txt_boleta']
        nombre = request.form['txt_nombre']
        grupo = request.form['txt_grupo']
        with open('alumnos.csv', 'a', newline='') as file:
            writer = csv.writer(file,delimiter=',')
            writer.writerow([boleta, nombre, grupo])
        return render_template('exito.html', tipo='alumnos')
    else:
        return render_template('alumnos.html')

@app.route("/profesores", methods=['GET','POST'])
def profesores():
    if request.method == 'POST':
        materia = request.form['txt_materia']
        profesor = request.form['txt_profesor']
        salon = request.form['txt_salon']
        with open('profesores.csv', 'a', newline='') as file:
            writer = csv.writer(file,delimiter=',')
            writer.writerow([materia,profesor,salon])
        return render_template('exito.html', tipo='profesores')
    else:
        return render_template('profesores.html')

if __name__ == '__main__':
    app.run(debug=True)