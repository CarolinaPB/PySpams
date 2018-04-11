from flask import Flask, render_template, request, flash
import numpy as np
from werkzeug import secure_filename
import os, sys

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
            sections = ("filename", "numloci0", "sampvector0", "inideme0", "file0", "timechange0", "demesizes0")
        if count >= 2:
            sections = ("filename", "numloci0", "sampvector0", "inideme0", "file0", "timechange0", "demesizes0")
            new_sections=[]

            for i in range(1,count):
                new_sections.append("file"+str(i))
                new_sections.append("timechange"+str(i))
                new_sections.append("demesizes"+str(i))

            for name in new_sections:
                name=(name,)
                sections = sections + name

######## Creates an array with the section names which will be in the final doc

        sections_array = np.array([["File name"],["Number of loci"],["Sampling vector"],["Initial deme sizes"]])
        part_sections_arr=np.array([["Initial migration matrix"], ["Time of change"], ["Deme sizes"]])

        part_sections_arr = np.vstack(part_sections_arr)

        if count == 1:
            part_sections_arr = part_sections_arr
        elif count >= 2:
            part_sections_arr = np.tile(part_sections_arr,(count,1))

        sections_array2=np.vstack((sections_array,part_sections_arr))

######## Creates and array with the same size as the sections_array2 but each field is "0"

        init_array = np.zeros((7+3*(count-1)), dtype=object)
        init_array = np.vstack(init_array)

######## Joins sections_array2 and init_array to form an array where the input will be stored

        total_array = np.hstack((sections_array2, init_array))

######## Saves the fields input (except matrices) to the array

        for i in range (4):
            total_array[i,1] = request.form[sections[i]]
        for i in range(5,len(total_array),3):
            total_array[i,1] = request.form[sections[i]]
            total_array[i+1,1] = request.form[sections[i+1]]

######## Saves the matrices to the array
        for i in range(4,len(total_array),3):
            if request.method =="POST":
                file = request.files[sections[i]]
                if file:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(UPLOAD_FOLDER, filename))

            file_path = ("/home/carolina/flask_app/flask_app/uploads/" + str(filename))
            filehandle = open(file_path,"r")
            filehandle=filehandle.read()
            filehandle=filehandle.replace(","," ")

            total_array[i,1] = filehandle
            print filehandle
            os.remove(file_path)

######## Saves info from matrix to file

        with open (total_array[0,1], "w") as f:
            for n in range(1,len(total_array)):
                f.write("# " + total_array[n,0])
                f.write("\n")
                f.write(total_array[n,1])
                f.write("\n\n")

######## To reset the count variable to 1
        global count
        count = 1


######## Message to let the user know the info has been saved
        flash ("File saved!")

        return render_template("main.html")
    else:
        return "not working"

if __name__ == "__main__":
    app.run(debug=True)
