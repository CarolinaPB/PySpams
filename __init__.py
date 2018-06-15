from flask import Flask, render_template, request, flash, url_for, send_from_directory, send_file, after_this_request
import numpy as np
from werkzeug import secure_filename
import os, sys
#import re
import matplotlib.pyplot as plt
from ms_IICR_functions import readScenario, createCmd, generate_MS_t2, compute_t_vector, compute_empirical_dist




reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecret"


@app.route('/')
def HOME():
    return render_template("home.html")

@app.route('/IICR')
def IICR():
    return render_template("ms.html")

@app.route('/NSCC')
def NSCC():
    return render_template("model1_form.html")

######## The Upload folder will be the current folder
current_folder_path, current_folder_name = os.path.split(os.getcwd())
UPLOAD_FOLDER = os.path.join(current_folder_path,current_folder_name)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

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

@app.route("/NSCC", methods=["POST"])
def handle_input():

    if request.form["button"] == "Add matrix":
        global btn_OK
        global count

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

        return render_template("model1_form.html", count=count, btn_OK=btn_OK)

    elif request.form["button"] == "Ok":
        if request.form["numdemes"] != "":
            global btn_OK
            btn_OK = "pressed"
        else:
            print "btn ok not working"
        return ("", 204)

    elif request.form["button"] == "Save to file":
        if request.form["numdemes"] == "":
            return ("", 204)
        else:
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


            data_to_save = np.zeros((no_zeros,numdemes+numdemes**2+1), dtype="object")

            for row in range(no_zeros):
                if count == 1:
                    for col in range(len(final_array)):
                        data_to_save[0,col] = request.form[final_array[col]]
                elif count >= 2:
                    for col in range(len(final_array[0])):
                        data_to_save[row,col] = request.form[final_array[row,col]]

                if data_to_save[row,0] == "":
                    return ("", 204)



            c=len(data_to_save)
            r=len(data_to_save[0])
            neg = 0

#if there is a negative number in the fields that will be saved, the variable "neg" will be given the value "neg". If neg = "neg", it means there's a negative number and the page will stay the same and the file won't save
            for i in range (0,c):
                for n in range(0,r):
                    if float(data_to_save[i,n])<0:
                        neg = "neg"

            #global filename
            #filename = request.form["filename"]
            #if os.path.isfile(filename+".txt"): #if there is already a file with the chosen name
             #   return render_template("fileexists.html", filename=filename)
            if data_to_save[0,0] != "0": # if the first timechange if not zero, the page stays the same and the file won't save
                return ("", 204)
            elif neg == "neg":
                return ("", 204)

            else:
                filename = request.form["filename"]
                file=filename+".txt"
                with open(file,"w") as f:
                    for row in range(no_zeros):

                        f.write("# Time")
                        f.write("\n")
                        f.write(data_to_save[row,0])
                        f.write("\n\n")

                        f.write("# Deme sizes")
                        f.write("\n")
                        for col in range(1,numdemes+1):
                            f.write(data_to_save[row,col])
                            if col < numdemes:
                                f.write(" ")
                        f.write("\n\n")

                        f.write("# Migration matrix")
                        f.write("\n")
                        for k in range(1,numdemes+1):
                            for i in range(k*numdemes+1,numdemes*(k+1)+1):
                                f.write(data_to_save[row,i])
                                if i < numdemes*(k+1):
                                    f.write(" ")
                            f.write("\n")
                        if row < no_zeros-1:
                            f.write("\n")

            ######## To reset the count variable to 1
                global count
                count = 1
            ######## To reset input_array
                global input_array
                input_array=np.array((["chk_remove0"],[1]), dtype=object)
                input_array=np.hstack(input_array)

                @after_this_request
                def remove_file(response):
                    os.remove(file)
                    return response
                #@after_this_request
                #def Refresh(response):
                 #   return render_template("model1_form.html")

            ######## Message to let the user know the info has been saved
                flash ("File saved!", "info")

                #use this in the final program.

                return send_from_directory(UPLOAD_FOLDER, file, as_attachment=True)

                #return render_template("model1_form.html")

    else:
        return "not working"



@app.route("/IICR", methods=["POST"])
def handle_ms():
    if request.form["button"] == "Submit":

        if request.method =="POST":
            file = request.files["ms_file0"]
            if file:
                ms_filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, ms_filename))

        ms_filename="./"+ms_filename

        #s = readScenario(ms_filename)
        #cmd = createCmd(s)

        # The variable cmd contains the relative path to the ms software
        # and assumes that the ms software is inside the same folder as the script.

        #T2 = generate_MS_t2(cmd)

        # Generating the time vector
        #start = 0.001
        #end = 10
        #number_of_values = 1000
        #vector_type = 'log'

        #t_vector = compute_t_vector(start, end, number_of_values, vector_type)
        #obs = T2


        #(F_x, f_x) = compute_empirical_dist(obs, t_vector)

        #IICR = np.true_divide(len(obs)-F_x, f_x)

        #fig = plt.figure()
        #ax = fig.add_subplot(111)
        #ax.step(t_vector, IICR, where='post', color="red", ls="-", label="IICR plot")
        #ax.set_xscale("log")
        #plt.legend(loc="best")
        #plt.show()


        os.remove(ms_filename)
        return render_template("ms.html")



if __name__ == "__main__":
    #app.run()
    app.run(debug=True)
