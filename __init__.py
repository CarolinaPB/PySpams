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
        numdemes = int(request.form["numdemes"])

        secondDoc_names = ["numloci", "numdemes"]
        for i in range(numdemes):
            secondDoc_names.append("sampcell"+str(i))

        if count == 1:
            final_array = np.zeros((numdemes+numdemes**2+1), dtype="object")
            final_array[0] = "timechange0"
            for i in range(numdemes):
                final_array[i+1] = ("demesizes_cell0_"+str(i))
            matr_names=[]
            for i in range(numdemes):
                for n in range(numdemes):
                    matr_names.append("matr_cell0_"+str(i)+"_"+str(n))

            a = 0
            while a < numdemes**2:
                for f in range(numdemes +1,len(final_array)):
                    final_array[f] = matr_names[a]
                    a += 1

            no_zeros=1
            print final_array

        elif count >= 2:

            for i in range(count):
                if request.form[input_array[i,0]] == "Remove":
                    input_array[i,1]=1
                else:
                    input_array[i,1]=0

            no_zeros = np.count_nonzero(input_array[:,1])
            final_array = np.zeros((no_zeros,numdemes+numdemes**2+1), dtype="object")

            a=0
            for c in range(count):
                if input_array[c,1] == 1:
                    final_array[a,0] = ("timechange"+str(c))
                    for i in range(numdemes):
                        final_array[a,i+1] = ("demesizes_cell"+str(c)+"_"+str(i))

                    matr_names = []
                    for i in range(numdemes):
                        for n in range(numdemes):
                            matr_names.append("matr_cell"+str(c)+"_"+str(i)+"_"+str(n))
                    b = 0
                    while b < numdemes**2:
                        for f in range(numdemes+1,len(final_array[0])):
                            final_array [a,f] = matr_names[b]
                            b +=1
                    a += 1


            print final_array


        data_to_save = np.zeros((no_zeros,numdemes+numdemes**2+1), dtype="object")

        for row in range(no_zeros):
            for col in range(len(final_array[0])):
                data_to_save[row,col] = request.form[final_array[row,col]]



        print "\n"
        print data_to_save

        with open(request.form["filename"],"w") as f:
            for row in range(no_zeros):
                f.write("# Time")
                f.write("\n")
                f.write(data_to_save[row,0])
                f.write("\n\n")
                f.write("# Deme sizes")
                f.write("\n")
                for col in range(1,numdemes+1):
                    f.write(data_to_save[row,col])
                    f.write(" ")
                f.write("\n\n")
                f.write("# Migration matrix")
                f.write("\n")
                #for r in range(numdemes):
                num = numdemes
                for col in range(1,num+1):
                    f.write(data_to_save[0,col+num]+" ")
                f.write("\n")





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
