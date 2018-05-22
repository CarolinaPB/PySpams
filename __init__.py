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
global btn_OK
btn_OK= "not pressed"

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
        global btn_OK
        if btn_OK == "pressed":
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
        btn_OK = "not pressed"
        input_array=np.array((["chk_remove0"],[1]), dtype=object)
        input_array=np.hstack(input_array)
        return render_template("main.html", count=count, btn_OK=btn_OK)
    elif request.form["button"] == "Ok":
        global btn_OK
        btn_OK = "pressed"
        return ("", 204)

    elif request.form["button"] == "Save to file":
        print "count is "+str(count)
        mainDoc_names = ["timechange0"]
        numdemes = int(request.form["numdemes"])

        secondDoc_names = ["numloci", "numdemes"]
        for i in range(numdemes):
            secondDoc_names.append("sampcell"+str(i))
        #print secondDoc_names

        if count == 1:

            for i in range(numdemes):
                mainDoc_names.append("demesizes_cell0_"+str(i))
            for i in range(numdemes):
                for n in range(numdemes):
                    mainDoc_names.append("matr_cell0_"+str(i)+"_"+str(n))
            #print mainDoc_names


        elif count >= 2:
            mainDoc_names = []
            for i in range(count):
                if request.form[input_array[i,0]] == "Remove":
                    input_array[i,1]=1
                else:
                    input_array[i,1]=0

            for c in range(count):
                if input_array[c,1] == 1:
                    mainDoc_names.append("timechange"+str(c))
                    for i in range(numdemes):
                        mainDoc_names.append("demesizes_cell"+str(c)+"_"+str(i))
                    for i in range(numdemes):
                        for n in range(numdemes):
                            mainDoc_names.append("matr_cell"+str(c)+"_"+str(i)+"_"+str(n))

        print mainDoc_names




        data_to_save = []
        headers = ["Time", "Deme sizes", "Migration matrix"]

        data_to_save.append(request.form[mainDoc_names[0]])

        for i in range(1,numdemes+1):
            data_to_save.append(request.form[mainDoc_names[i]])

        print data_to_save





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
