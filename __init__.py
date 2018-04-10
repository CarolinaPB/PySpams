from flask import Flask, render_template, request
import numpy as np
from werkzeug import secure_filename
import os, sys, tempfile

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
count = 1


def counter ():
    global count
    count += 1
    return ('', 204)

@app.route("/", methods=["POST"])
def handle_input():
    if request.form["button"] == "Add matrix":
    #creates a counter for the "add matrix" button
        counter()
        print "count is " + str(count)
        return (str(count), 204)
    elif request.form["button"] == "Save to file":

######## Creates an array ("sections") with the names/id from each field. For each new matr it adds a new group of unique names for the new fields.

        if count == 1:
            sections = np.array([["filename"],["numloci0"], ["sampvector0"], ["inideme0"],["file0"], ["timechange0"],["demesizes0"]],dtype=object)
        elif count >= 2:
            sections = np.array([["filename"],["numloci0"], ["sampvector0"], ["inideme0"],["file0"], ["timechange0"],["demesizes0"]],dtype=object)
            for n in range(1,count):
                part_sections=np.array([["file"], ["timechange"],["demesizes"]],dtype=object)
                part_sections[0] = part_sections[0]+str(n)
                part_sections[1] = part_sections[1]+str(n)
                part_sections[2] = part_sections[2]+str(n)
                sections = np.append([sections], [part_sections])
                sections = np.vstack(sections)

########

        sections_array = np.array([["File name"],["Number of loci"],["Sampling vector"],["Initial deme sizes"]])
        part_sections_arr=np.array([["Initial migration matrix"], ["Time of change"], ["Deme sizes"]])

        part_sections_arr = np.vstack(part_sections_arr)

        if count == 0:
            part_sections_arr = part_sections_arr
        else:
            part_sections_arr = np.tile(part_sections_arr,(count+1,1))

        sections_array2=np.vstack((sections_array,part_sections_arr))
        #print "\n\n\n"
        #print sections_array2

        init_array = np.zeros((6+3*count+1), dtype=object)
        init_array = np.vstack(init_array)
        total_array = np.hstack((sections_array2, init_array))
        #print "\n\n\n"

        #saves the first matrix to the computer
        if request.method =="POST":
            file = request.files["file0"]
            if file:
                filename = secure_filename(file.filename)
                #print filename
                file.save(os.path.join(UPLOAD_FOLDER, filename))

        #for i in range(4):
         #   total_array[i,1] = request.form[sections[i]]

        total_array[5,1] = request.form["timechange0"]
        total_array[6,1] = request.form["demesizes0"]
        #print total_array

        #adds the matrix to total_array
        file_path = ("/home/carolina/flask_app/flask_app/uploads/" + str(filename))
        filehandle = open(file_path,"r")
        filehandle=filehandle.read()
        filehandle=filehandle.replace(","," ")

        total_array[4,1] = filehandle
        #print total_array

        #to reset the count variable to 1
        global count
        count = 1

        os.remove(file_path)

        return "this will be to save doc"
    else:
        return "not working"



if __name__ == "__main__":
    app.run(debug=True)
