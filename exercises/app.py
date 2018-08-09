from databases import *
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
    if request.method == 'GET':
        return render_template("add.html")
    else:
        name=request.form['student_name']
        year=request.form['student_year']
        finished_lab=request.form['finished_lab']
        add_student(name,year,finished_lab)
        print(query_all())
        return 'thank you for filling out the form!'

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

app.run(debug=True)
