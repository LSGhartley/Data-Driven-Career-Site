from flask import Flask
from flask import render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

#Get the homepage and database data
@app.route("/")
def homepage():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, name="HEL")

#Get a dictionary of all the jobs from the database
@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

#Get a single job from the database
@app.route("/job/<id>")
def show_job(id: int):
    job = load_job_from_db(id)
    return jsonify(job)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)