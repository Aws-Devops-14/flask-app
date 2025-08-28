from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def admin():
    return "this is admin"

@app.route("/student")
def student():
    return "this is student"

@app.route("/staff")
def staff():
    return "this is staff"
#building URL dynamically#
@app.route("/user/<name>")
def user(name):
    if name == "admin":
        return redirect(url_for("admin"))
    elif name == "student":
        return redirect(url_for("student"))
    elif name == "staff":
        return redirect(url_for("staff"))
    else:
        return "not found"

if __name__ == "__main__":
    app.run(debug=True)
