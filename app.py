from flask import *

app=Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    uname=request.form["uname"]
    passwrd=request.form["pass"]
    if uname=="Usha" and passwrd=="qwe":
        return "Welcome to the new World %s" %uname
    else:
          return "inavlid"



if __name__ == "__main__":
    app.run(debug=True)