from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/usha" ,methods=["GET"])
def fun():
    uname=request.args.get("uname")
    password=request.args.get("password")
    if uname=="rani" and password=="123":
        return "Believe yourself"
    else:
        return "Try agin"
    

if __name__=="__main__":
    app.run(debug=True)
