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
    return ('', 204)

@app.route("/", methods=["POST"])
def handle_input():
    if request.form["button"] == "Add matrix":
    #creates a counter for the "add matrix" button
        counter()
        return (str(count), 204)
    elif request.form["button"] == "Save to file":
    #will save info to a file

######## not working properly
        sections = np.array([["filename"],["numloci0"], ["sampvector0"], ["inideme0"]])
        part_sections=np.array([["file"], ["timechange"],["demesizes"]])
        sections = np.hstack(sections)
        part_sections = np.hstack(part_sections)

        if count == 0:
            part_sections[0] = part_sections[0]+str(0)
            part_sections[1]= part_sections[1] + str(0)
            part_sections[2]= part_sections[2] + str(0)

            sections = np.hstack((sections, part_sections))

        else:
            part_sections = np.tile(part_sections,(count+1,1))
            part_sections = np.hstack(part_sections)

            sections = np.hstack((sections,part_sections))


        print sections


        for i in range(4,len(sections),3):
            for n in range(0,count+1):
                sections[i] = sections[i]+str(count)
                sections[i+1] = sections[i+1]+str(count)
                sections[i+1] = sections[i+1]+str(count)

            print sections[i]
            print sections[i+1]
            print sections[i+2]

########

        sections_array = np.array([["File name"],["Number of loci"],["Sampling vector"],["Initial deme sizes"]])

        part_sections_arr=("Initial migration matrix", "Time of change", "Deme sizes")
        part_sections_arr = np.vstack(part_sections_arr)

        if count == 0:
            part_sections_arr = part_sections_arr
        else:
            part_sections_arr = np.tile(part_sections_arr,(count+1,1))

        sections_array2=np.vstack((sections_array,part_sections_arr))
        print "\n\n\n"
        print sections_array2

        init_array = np.zeros((6+3*count+1), dtype=object)
        init_array = np.vstack(init_array)
        total_array = np.hstack((sections_array2, init_array))
        print "\n\n\n"

        #saves the first matrix to the computer
        if request.method =="POST":
            file = request.files["file0"]
            if file:
                filename = secure_filename(file.filename)
                #print filename
                file.save(os.path.join(UPLOAD_FOLDER, filename))

        for i in range(4):
            total_array[i,1] = request.form[sections[i]]

        total_array[5,1] = request.form["timechange0"]
        total_array[6,1] = request.form["demesizes0"]
        #print total_array

        #adds the matrix to total_array
        file_path = ("/home/carolina/flask_app/flask_app/uploads/" + str(filename))
        filehandle = open(file_path,"r")
        filehandle=filehandle.read()
        filehandle=filehandle.replace(","," ")

        total_array[4,1] = filehandle
        print total_array

        os.remove(file_path)

        return "this will be to save doc"
    else:
        return "not working"



if __name__ == "__main__":
    app.run(debug=True)
