from flask import Flask, render_template, request
import numpy as np
from werkzeug import secure_filename
import os, sys, tempfile
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecret"



#for wtform#
class form1(FlaskForm):
    numloci = StringField("Number of loci")
    sampvector =StringField("Sampling vector")
    inideme = StringField("Initial deme sizes")
    inimatr = StringField("Initial migration matrix")
    timechange = StringField("Time of change")
    demesizes = StringField("Deme sizes")
    filename2 = StringField("File name")
    submit = SubmitField("Submit")
####

@app.route('/')
def homepage():
    return render_template("main.html")

UPLOAD_FOLDER = 'uploads/'
app.config["UPLOADFOLDER"] = UPLOAD_FOLDER


#for wtform#
@app.route("/test/", methods=["GET", "POST"])
def test_funct():
    form = form1()

    if form.validate_on_submit():
        return "Your input was saved in {}".format(form.filename2.data)
    return render_template("wtf_model1.html", form=form)
####

@app.route('/',methods=['POST',"GET"])
def handle_input3():
    form_1=np.zeros((4,1), dtype="object")
    form_1[0,0]=request.form["filename"]
    form_1[1,0]=request.form["numloci"]
    form_1[2,0]=request.form["sampvector"]
    form_1[3,0]=request.form["inideme"]
    print form_1
    return "ok"

@app.route('/tes', methods=['POST',"GET"])
def handle_input2():
    if request.method =="POST":
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            print filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))

    sections = ("filename2","numloci","sampvector", "inideme","file", "timechange","demesizes")

    sections_array =np.array([["File name"],["Number of loci"],["Sampling vector"],["Initial deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"]])


    init_array = np.zeros((16,1), dtype=object)
    total_array = np.hstack((sections_array,init_array))

    file_path = ("/home/carolina/flask_app/flask_app/uploads/" + str(filename))
    filehandle = open(file_path,"r")
    filehandle=filehandle.read()
    filehandle=filehandle.replace(","," ")


    total_array[0,1]=request.form["filename2"]
    total_array[1,1]=request.form["numloci"]
    total_array[2,1]=request.form["sampvector"]
    total_array[3,1]=request.form["inideme"]
    total_array[4,1] = filehandle
    total_array[5,1]=request.form["timechange"]
    total_array[6,1]=request.form["demesizes"]

    os.remove(file_path)
    print total_array
    return request.form["filename2"]+"\n"+request.form["numloci"]+"\n"+request.form["sampvector"]+"\n"+request.form["inideme"]+"\n"+request.form["timechange"]+"\n"+request.form["demesizes"]+"\n"



@app.route('/', methods=['POST',"GET"])
def handle_input():
    if request.method =="POST":
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            #print filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))

    sections = ("filename2","numloci","sampvector", "inideme","file", "timechange","demesizes")

    sections_array =np.array([["File name"],["Number of loci"],["Sampling vector"],["Initial deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"],["Initial migration matrix"],["Time of change"],["Deme sizes"]])

    init_array = np.zeros((16,1), dtype=object)
    total_array = np.hstack((sections_array,init_array))


    for i in range (0,4):
        total_array[i,1]=request.form[sections[i]]
    for i in range (5,17):
        total_array[i,1]=request.form[sections[i]]

    file_path = ("/home/carolina/flask_app/flask_app/uploads/" + str(filename))
    filehandle = open(file_path,"r")
    filehandle=filehandle.read()
    filehandle=filehandle.replace(","," ")

    total_array[4,1] = filehandle
    print total_array

    #with open(request.form[sections[0]],"w") as f:
     #   for i in range(1,7):
      #      f.write("# " + total_array[i,0])
       #     f.write("\n")
        #    f.write(str(total_array[i,1])+"\n")
         #   f.write("\n")

    os.remove(file_path)
    return render_template("main.html")



if __name__ == "__main__":
    app.run(debug=True)
