from flask import Flask, render_template, request
import numpy as np
from werkzeug import secure_filename
import os, sys, tempfile
#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField


reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecret"


@app.route('/')
def homepage():
    return render_template("main.html")

UPLOAD_FOLDER = 'uploads/'
app.config["UPLOADFOLDER"] = UPLOAD_FOLDER


@app.route('/',methods=['POST',"GET"])
def handle_input3():

    # if count = number of clicks ont the add matrix button
    #for i in range(0,count):
        #if request.method =="POST":
         #   file = request.files["file"+i]
          #  if file:
           #     filename = secure_filename(file.filename)
            #    print filename
             #   file.save(os.path.join(UPLOAD_FOLDER, filename))
    sections = ("filename","numloci","sampvector", "inideme","file", "timechange","demesizes")
    part_sections_arr=("Initial migration matrix", "Time of change", "Deme sizes")
    sections_array = np.array([["File name"],["Number of loci"],["Sampling vector"],["Initial deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"]])
    #sections_array2= np.append(sections_array,count*part_sections_arr)
    #print sections_array2

    #init_array = np.zeros((6+3*count), dtype=object)
    #total_array = np.hstack((sections_array, init_array))

    #for i in range(0,4):
     #   total_array[i,1]=request.form[sections[i]+count]


    return "ok"


if __name__ == "__main__":
    app.run(debug=True)
