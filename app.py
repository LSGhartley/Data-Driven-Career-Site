from flask import Flask
from flask import render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db


app = Flask(__name__)

#Get the homepage and database data
@app.route("/")
def homepage():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

#Get a dictionary of all the jobs from the database
@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

#Get a single job from the database
@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_for_job(id):
    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template('app_submitted.html', application=data, job=job)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)