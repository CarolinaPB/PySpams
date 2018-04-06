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

global count
count = 0


def counter ():
    global count
    count += 1
    print "count is " + str(count)
    return ('', 204)
    #return str(count)

@app.route("/", methods=["POST"])
def handle_input():
    if request.form["button"] == "Add matrix":
    #creates a counter for the "add matrix" button
        counter()
        print count
        return (str(count), 204)
    elif request.form["button"] == "Save to file":
    #will save info to a file
        #print "test "+str(count)
        files_to_open = []
        #print count
        for i in range(count+1):
            files_to_open.append("file" + str(i))
            #print files_to_open[i]
            if request.method =="POST":
                #file = request.files["file" +str(i)]
                print "need to add the save matrix process"

             #   if i == 0:
              #      print type(files_to_open)
               #     file = request.files[files_to_open[i]]
                #else:
                 #   print "not"
                    #if file:
                     #   filename = secure_filename(file.filename)
                      #  print filename
                       # file.save(os.path.join(UPLOAD_FOLDER, filename))
                    #else:
                     #   return "please choose matrix"
                #else:
                 #   print files_to_open[i]
                  #  file = request.files[files_to_open[i]]
                    #if file:
                     #   filename = secure_filename(file.filename)
                      #  print filename
                       # file.save(os.path.join(UPLOAD_FOLDER, filename))
                    #else:
                     #   return "please choose matrix"
        sections = ("filename","numloci","sampvector", "inideme","file", "timechange","demesizes")

        part_sections_arr=("Initial migration matrix", "Time of change", "Deme sizes")
        part_sections_arr = np.vstack(part_sections_arr)

        if count == 0:
            part_sections_arr = part_sections_arr
        else:
            for i in range(count-1):
                part_sections_arr = np.vstack((part_sections_arr,part_sections_arr))

        sections_array = np.array([["File name"],["Number of loci"],["Sampling vector"],["Initial deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"]])

        print "\n\n"
        sections_array2=np.vstack((sections_array,part_sections_arr))
        print sections_array2

        init_array = np.zeros((6+3*count+1), dtype=object)
        init_array = np.vstack(init_array)
        total_array = np.hstack((sections_array2, init_array))
        print "\n\n\n"
        #print init_array
        print total_array

        return "this will be to save doc"
    else:
        return "not working"



if __name__ == "__main__":
    app.run(debug=True)
