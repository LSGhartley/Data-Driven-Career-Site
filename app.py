from flask import Flask
from flask import render_template, jsonify

app = Flask(__name__)

JOBS = [{'id': 1,
        'title': 'Data Analyst',
        'location': 'Midrand, South Africa',
        'salary': 'FREE'}, {'id': 2,
        'title': 'Front-End Developer',
        'location': 'Midrand, South Africa',
        'salary': 'FREE'}, {'id': 3,
        'title': 'Backend Developer',
        'location': 'Midrand, South Africa',
        'salary': 'FREE'}, {'id': 4,
        'title': 'Site Reliabilty Engineer',
        'location': 'Midrand, South Africa',
        'salary': 'FREE'}]

@app.route("/")
def homepage():
    return render_template('home.html', jobs=JOBS, name="HEL")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)