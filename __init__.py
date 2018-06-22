from flask import Flask, render_template, request, flash, url_for, send_from_directory, send_file, after_this_request
import numpy as np
from werkzeug import secure_filename
import os, sys
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

@app.route('/NSSC')
def NSSC():
    return render_template("model1_form.html")

@app.route('/FileExample')
def FileExample():
    return render_template("fileexample.html")


######## The Upload folder will be the current folder
current_folder_path, current_folder_name = os.path.split(os.getcwd())
UPLOAD_FOLDER = os.path.join(current_folder_path,current_folder_name)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/NSSC", methods=["POST"])
def handle_input():

    if request.form["button"] == "Reset form":
        return render_template("model1_form.html")

    elif request.form["button"] == "Add matrix":
        return ("", 204)

    elif request.form["button"] == "Ok":
        return ("", 204)

    elif request.form["button"] == "Save to file":
        return ("", 204)
            #return render_template("model1_form.html")



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
