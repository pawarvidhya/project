from flask import Flask
## WSGI Application This WSGI is Standard which actually used to communicate webserver and web applicaiton to communciate
app = Flask(__name__) #wsgi applicaiton

@app.route("/")
def welcome():
    return "Welcome Msdhoni Cool"

@app.route("/result/<int:score>")
def welcome1(score):
    res=""
    if score>50:
        res="pass"
    else:
        res="fail"
    return res

if __name__=='__main__':
    app.run(debug=True)
