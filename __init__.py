from flask import Flask, render_template, request
import numpy as np
from werkzeug import secure_filename
import os


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")
UPLOAD_FOLDER = 'uploads/'
app.config["UPLOADFOLDER"] = UPLOAD_FOLDER

@app.route("/", methods = ["GET", "POST"])
def upload():
    if request.method =="POST":
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
    return "matrix saved"
    

@app.route('/receive_input', methods=['POST',"GET"])
def handle_input():
    sections = ("numloci","sampvector", "inideme","inimatr", "timechange","demesizes", "filename")
    sections_names = ("Number of loci", "Sampling Vector", "Initial deme sizes","Initial migration matrix", "Time of change", "Deme sizes")        
    data =[]
    value = request.form[sections[3]]
    print "value==" + str(value)
    if request.method =="POST":
        for i in range (0,7):
            data.append(request.form[sections[i]])
        print data
    
    with open(request.form[sections[6]],"w") as f:
        for i in range (0,6):
            f.write ("# " + sections_names[i])
            f.write ("\n")
            f.write (request.form[sections[i]])
            f.write ("\n\n")
    return "Your data has been saved in a file"
       



if __name__ == "__main__":
    app.run()
