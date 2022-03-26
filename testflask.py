from turtle import pd
from flask import Flask, make_response, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/name")
def hellomoltira():
    return "Hello, Moltira!"

##api
@app.route('/request',methods=['POST'])
def request_detail():

    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)
    
    print(inmessage)

    json_data = json.dumps({'y':'received!'})
    return json_data
    
##webapp
@app.route("/home",methods=['POST','GET'])
def home():
    if request.method == "POST":
        dbpd = pd.read_csv('dtb.csv')
       # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
        last_name = request.form.get("lname") 
        dbpd = dbpd.append({'fname': first_name,'lname' : last_name}, ignore_index=True)
        dbpd.to_csv('dtb.csv',index=False)

        resp=make_response(render_template("index.html", name = f"{first_name} {last_name}", fav=""))
        resp.set_cookie('fname', first_name)
        resp.set_cookie('lname', last_name)
        return resp
    
    if request.method == "GET":
        getval = request.args
        print(getval)
        print(getval.get('fname'))
        print(getval.get('lname'))
    
    return render_template("index.html",name='Moltira', fav="")

@app.route("/home1",methods=['POST','GET'])
def home1():
    if request.method == "POST":
        dbpd = pd.read_csv('dtb.csv')
       # getting input with name = fname in HTML form
        fav = request.form.get("fav_language")
       # getting input with name = lname in HTML form  
        dbpd = dbpd.append({'fav_language': fav}, ignore_index=True)
        dbpd.to_csv('dtb.csv',index=False)

        resp=make_response(render_template("index.html", name='Moltira', fav=fav))
        resp.set_cookie('fav_language', fav)

        return resp

    if request.method == "GET":
        getval = request.args
        print(getval)
        print(getval.get('fav_language'))

    return render_template("index.html",name='Moltira', fav=fav)

if __name__ == "__main__":
    app.run() #host='0.0.0.0'host='0.0.0.0', port='5001