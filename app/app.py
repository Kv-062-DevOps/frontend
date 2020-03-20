from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# url for get requests
# url_get = 'https://jsonplaceholder.typicode.com/todos/' 
# url for post request
url_post = 'http://localhost:5000'

@app.route("/")
@app.route("/home")
def home():
    # employees=[]
    # # Change this url for get request
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
        flash(f'Account created for {form.first_name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('manager.html', title='manager', form=form)

@app.route("/designer", methods=['GET', 'POST'])
def designer():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.first_name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('designer.html', title='designer', form=form)

@app.route("/developer", methods=['GET', 'POST'])
def developer():
    form = RegistrationForm()
    if form.validate_on_submit():
        first_name = request.form.get('first_name')
        second_name = request.form.get('second_name')
        types = request.form.get('types')
        default_salary = request.form.get('default_salary')
        experience = request.form.get('experience')
        data = {"first_name":first_name, "second_name":second_name, "types":types, "default_salary":default_salary, "experience":experience}
        app_json = json.dumps(data, sort_keys=True)
        r = requests.post(url = url_post, data = app_json)
        flash(f'Account created for {form.first_name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('developer.html', title='developer', form=form)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)