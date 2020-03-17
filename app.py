from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

employees = [
    {
        'firstname': 'Ivan',
        'lastname': 'Drago',
        'position': 'manager',
        'experiance': '8',
        'salary': '3000'
    },
     {
        'firstname': 'Ivan',
        'lastname': 'Drogo',
        'position': 'developer',
        'experiance': '10',
        'salary': '2000'
    },
     {
        'firstname': 'Ivan',
        'lastname': 'Drogo',
        'position': 'designer',
        'experiance': '10',
        'salary': '2500'
    }
]



@app.route("/")
@app.route("/home")
def home():
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
    if form.validate_on_submit():
        flash(f'Account created for {form.firstname.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('developer.html', title='developer', form=form)


if __name__ == '__main__':
    app.run(debug=True)