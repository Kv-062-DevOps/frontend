from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route("/home")
def home():
    # employees=[]
    # # Change this url for get request
    # url_get = 'https://jsonplaceholder.typicode.com/todos/' 
    # response = requests.get(url_get)
    # obj = json.loads(response.text)
    # for i in obj:
    #     employees.append(i)
    # return render_template('home.html', employees=employees)
    # # This is test section
    with open('test.json', 'r') as myfile:
        employees=[]
        data=myfile.read()
        obj = json.loads(data)
        for i in obj:
            employees.append(i)
        return render_template('home.html', employees=employees)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/manager", methods=['GET', 'POST'])
def manager():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.firstname.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('manager.html', title='manager', form=form)

@app.route("/designer", methods=['GET', 'POST'])
def designer():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.firstname.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('designer.html', title='designer', form=form)

@app.route("/developer", methods=['GET', 'POST'])
def developer():
    form = RegistrationForm()
    # # Change this url for post request
    url_post = 'http://localhost:5000'
    if form.validate_on_submit():
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        position = request.form.get('position')
        salary = request.form.get('salary')
        experiance = request.form.get('experiance')
        data = {"firstname":firstname, "lastname":lastname, "position":position, "salary":salary, "experiance":experiance}
        app_json = json.dumps(data, sort_keys=True)
        r = requests.post(url = url_post, data = app_json)
        flash(f'Account created for {form.firstname.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('developer.html', title='developer', form=form)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)