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


@app.route('/receive_input', methods=['POST',"GET"])
def handle_input():
    if request.method =="POST":
        file = request.files["file"]
        if file:
            #global filename
            filename = secure_filename(file.filename)
            print filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))

    sections = ("numloci","sampvector", "inideme","inideme", "timechange","demesizes", "filename2")
    sections_array =np.array([["Number of loci"],["Sampling vector"],["Initial deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"], ["File name"]])

    init_array = np.zeros((7,1), dtype=object)
    total_array = np.hstack((sections_array,init_array))


    for i in range (0,3):
        total_array[i,1]=request.form[sections[i]]
    for i in range (4,6):
        total_array[i,1]=request.form[sections[i]]

    file_path = ("/home/carolina/flask_app/flask_app/uploads/" + str(filename))
    filehandle = open(file_path,"r")
    filehandle=filehandle.read()
    filehandle=filehandle.replace(","," ")

    total_array[3,1] = filehandle

    with open(request.form[sections[6]],"w") as f:
        for i in range(0,6):
            f.write("# " + total_array[i,0])
            f.write("\n")
            f.write("# " + str(total_array[i,1])+"\n")
            f.write("\n")

    os.remove(file_path)
    return render_template("main.html")



if __name__ == "__main__":
    app.run(debug=True)
