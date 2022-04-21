from flask import flask ,jsonify,request
import time 
app =flask (__name__)
@app.route("/bot",'/post')
def response():
    query =dict (request.form)['query']
    result =query + "fofofofofo"+time.ctime()
    return jsonify ({"response":result})

    if __name__ =="__main__":
        app.run(host="0.0.0.0",)

