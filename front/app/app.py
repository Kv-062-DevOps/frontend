from flask import Flask, Response
from flask import render_template, url_for, flash, redirect, request
from forms import RegistrationForm

import prometheus_client
import requests
import json
import os
import time

# <PROMETHEUS>

COUNT = prometheus_client.Counter(
    'request_count', 'App Request Count',
    ['app_name', 'method', 'endpoint', 'http_status']
)

LATENCY = prometheus_client.Histogram('request_latency_seconds', 'Request latency',
                                      ['app_name', 'endpoint']
                                      )

content_type_latest = str('text/plain; version=0.0.4; charset=utf-8')


def start_timer():
    request.start_time = time.time()


def stop_timer(response):
    resp_time = time.time() - request.start_time
    LATENCY.labels('front-service', request.path).observe(resp_time)
    return response


def record_request_data(response):
    COUNT.labels('front-service', request.method, request.path,
                 response.status_code).inc()
    return response


def setup_metrics(app):
    app.before_request(start_timer)
    # The order here matters since we want stop_timer
    # to be executed first
    app.after_request(record_request_data)
    app.after_request(stop_timer)

# </PROMETHEUS>


app = Flask(__name__)

setup_metrics(app)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# url for get requests
url_get = os.environ['URL_GET']  # 'http://localhost:8081'
# url for post request
url_post = os.environ['URL_POST']  # http://localhost:8082'


@app.route("/")
@app.route("/home")
def home():
    employees = []
    response = requests.get(url_get)
    obj = json.loads(response.text)
    if (type(obj) == dict):
        employees.append(obj)
        return render_template('home.html', employees=employees)
    else:
        return render_template('home.html', employees=obj)


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
        data = {"first_name": first_name, "second_name": second_name,
                "types": types, "default_salary": default_salary, "experience": experience}
        app_json = json.dumps(data, sort_keys=True)
        r = requests.post(url=url_post, data=app_json)
        flash(f'Account created for {form.first_name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('employee.html', title='employee', form=form)


@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=content_type_latest)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
