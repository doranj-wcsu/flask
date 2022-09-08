from flask import Flask
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World CS298- Jim!"

  
@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Modules" : 15,
            "Subject" : "Data Structures and Algorithms",
        }
  
        return jsonify(data)



if __name__ == '__main__':
     app.run()   
#     app.run(host="localhost",  port=8080 ,debug=True)

    
