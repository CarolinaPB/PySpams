from flask import Flask, render_template, request
import numpy as np
from werkzeug import secure_filename
import os, sys, tempfile


reload(sys)
sys.setdefaultencoding('utf-8')


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
            global filename
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
    return "matrix saved"

    

@app.route('/receive_input', methods=['POST',"GET"])
def handle_input():
    sections = ("numloci","sampvector", "inideme","filename", "timechange","demesizes", "filename2")
    sections_array =np.array([["Number of loci"],["Sampling vector"],["Initial deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"], ["File name"]]) 
    
    init_array = np.zeros((7,1), dtype=object)
    total_array = np.hstack((sections_array,init_array))
    global filename
    path = ("/home/carolina/flask_app/flask_app/uploads/" + str(filename))
    matr = open(path,"r")
    matr=matr.read()
    print matr
                
    for i in range(0,7):
        
        total_array[i,1] = request.form[sections[i]]
        
    #not saving properly
        with open(request.form[sections[6]],"w") as f:
            for i in range(0,6):
                f.write("# " + total_array[i,0])
                f.write("\n")
                f.write("# " + str(total_array[i,1]))
                f.write("\n\n")
                
                    
                
    print total_array
  
    return render_template("main.html")



if __name__ == "__main__":
    app.run()
