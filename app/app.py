from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# url for get requests
url_get = 'http://localhost:8081'
# url for post request
url_post = 'http://localhost:8084'

@app.route("/")
def _():
    return render_template('home.html')
@app.route("/home")
def home():
    # employees=[]
    # response = requests.get(url_get)
    # obj = json.loads(response.text)
    # if (type(obj) == dict):
    #     employees.append(obj)
    #     return render_template('home.html', employees=employees)
    # else:
    #     return render_template('home.html', employees=obj)
    # This is test section
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

@app.route("/employee", methods=['GET', 'POST'])
def employee():
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
    return render_template('employee.html', title='employee', form=form)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)