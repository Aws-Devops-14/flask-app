from flask import Flask,request,redirect,url_for,render_template
app=Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/")
def home_2():
    return render_template("base3.html")


@app.route("/usha", methods=["POST","GET"])
def home_data():
    total_score=0
    if request.method=="POST":
        science=float(request.form["Science"])
        maths=float(request.form["Maths"])
        c=float(request.form["C"])
        data_science=float(request.form["Data_Science"])
        total_score=(science+maths+c+data_science)/4
    res=" "
    if total_score>50:
        res="Pass"
    else:
        res="Fail"
    return render_template("base3.html",res=res)


if __name__=="__main__":
    app.run(debug=True)
