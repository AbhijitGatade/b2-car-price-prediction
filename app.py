from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/car-project")
def car_project():
    return render_template("car-project.html")

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

#To Run
#flask --app app run