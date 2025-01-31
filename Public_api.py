from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime 

#Public_api.py is the app name
#Public_api is the Virtual environment
# Create Flask app and enable CORS
app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET']) #Response/Request format
def home():
    # To get current UTC time in ISO 8601 format
    current_datetime = datetime.utcnow().isoformat() + "Z" #Append z for utc format
    
    # Response data to display
    response = {
        "email":"captainmarvelhealth@gmail.com",
        "current_datetime": current_datetime,
        "github_url": "https://github.com/VirusEmp/Public_API"
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000, debug=True)
    #the port is for your localmachine
    #the host is for the deployments service
