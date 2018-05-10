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

######## The Upload folder will be the current folder
current_folder_path, current_folder_name = os.path.split(os.getcwd())
UPLOAD_FOLDER = os.path.join(current_folder_path,current_folder_name)

app.config["UPLOADFOLDER"] = UPLOAD_FOLDER

global count
count = 1


global input_array
input_array=np.array((["chk_remove0"],[1]), dtype=object)

input_array=np.hstack(input_array)

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
    # Adds a new row with the name of the checkbox and state "1" (corresponds to checked)
        new_input=np.array((["chk_remove"+str(count-1)],[1]), dtype=object)
        global input_array
        new_input=np.hstack(new_input)
        input_array=np.vstack((input_array, new_input))
        return (str(count), 204)

    elif request.form["button"] == "Reset form":
        count = 1
        input_array=np.array((["chk_remove0"],[1]), dtype=object)
        input_array=np.hstack(input_array)
        return render_template("main.html", count=count)
    elif request.form["button"] == "Ok":
        return ("", 204)

    elif request.form["button"] == "Save to file":

######## Creates a list ("sections") with the names/id from each field. For each new matr it adds a new group of unique names for the new fields.
######## Creates a list with the section names which will be in the final doc

        if count == 1:
            sections = ["filename", "numloci0", "sampvector0", "inideme0", "file0", "timechange0", "demesizes0"]
            sections_list = ["File name", "Number of loci", "Sampling Vector", "Initial deme sizes", "Initial migration matrix", "Time of change", "Deme sizes"]

        elif count >= 2:
            sections = ["filename", "numloci0", "sampvector0", "inideme0"]
            sections_list = ["File name", "Number of loci", "Sampling Vector", "Initial deme sizes", "Initial migration matrix", "Time of change", "Deme sizes"]
            part_sections_list=[]
######## The state of an uncheked checkbox is changed to "0"
            for i in range(count):
                if request.form[input_array[i,0]] == "Remove":
                    input_array[i,1]=1
                else:
                    input_array[i,1]=0
####### The names are only added if the checkbox is cheked (value = 1)
            for i in range(count):
                if input_array[i,1]==1:
                    sections.append("file"+str(i))
                    sections.append("timechange"+str(i))
                    sections.append("demesizes"+str(i))

                    sections_list.append("Initial migration matrix")
                    sections_list.append("Time of change")
                    sections_list.append("Deme sizes")

######## Creates a list with the input from the web form

        input_data = []
        for i in range(4):
            input_data.append(request.form[sections[i]])

        for n in range(5,len(sections),3):
            if request.method =="POST":
                file = request.files[sections[n-1]]
                if file:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(UPLOAD_FOLDER, filename))

            file_path = (UPLOAD_FOLDER+"/"+str(filename))
            filehandle = open(file_path,"r")
            filehandle = filehandle.read()
            filehandle = filehandle.replace(","," ")
            filehandle = filehandle.strip("\n")

            input_data.append(filehandle)
            input_data.append(request.form[sections[n]])
            input_data.append(request.form[sections[n+1]])

            os.remove(file_path)

######## Saves info to file
        with open(input_data[0],"w") as f:
            for n in range(1,len(sections)):
                f.write("# " + str(sections_list[n]))
                f.write("\n")
                f.write(input_data[n])
                f.write("\n\n")

######## To reset the count variable to 1
        global count
        count = 1
######## To reset input_array
        global input_array
        input_array=np.array((["chk_remove0"],[1]), dtype=object)
        input_array=np.hstack(input_array)

######## Message to let the user know the info has been saved
        flash ("File saved!")

        return render_template("main.html")
    else:
        return "not working"


if __name__ == "__main__":
    #change to app.run()
    app.run(debug=True)
