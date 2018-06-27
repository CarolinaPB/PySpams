# Web Interface

## Get Started

You will need:

 * Python
 * [Flask](http://flask.pocoo.org/docs/0.12/)  -> [installation](http://flask.pocoo.org/docs/dev/installation/)
 * NumPy
 * matplotlib.pyplot
 * ms


 ### Installation
 If you don't have pip, start with this
 ```
 sudo apt install python-pip
 ```
Install **Flask**
```
pip install Flask
```
Install **NumPy**
```
pip install numpy
```
Install **matplotlib**
```
pip install matplotlib
```


## How to use PySpams

#### Files
Your directory should be organized like this:
* Main folder (PySpams)
  * \__init__.py
  * ms_IICR_functions.py
  * using_python_functions.py
  * ms

  * static
    * css
      * bootstrap3.min.css
    * js
      * bootstrap.min.js
      * jquery-3.3.1.min.js
      * new_matrjs_alt.js

  * templates
    * main.html
    * home.html
    * model1_form.html
    * ms.html
    * fileexample.html





#### Open PySpams in the browser


To use the program, open the terminal on the same directory as the python scripts and run **\__init__.py**. Open the link shown in the terminal.
```python
python __init__.py
```

You'll get this message:
```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Follow the link.
This will open PySpams in the browser. **The program is ready to use.**

#### Using PySpams

Add your data (refer to  **[this page](https://github.com/willyrv/nssc-scenario-specification)** or to the **File example** tab for the desired input structure).


You first need to add the **Number of loci** and the **Number of demes**. After you add them, new fields will be available.

The first **Time of change** should be zero.

You can choose to use a **"Custom" Migration matrix** or a matrix populated according to the N-island model (**N-island Migration matrix**). In this case, it is necessary to add the **Migration rate** and the matrix will be automatically populated.

If you don't want to use one of the matrices, "uncheck" the checkbox.
If the box is checked, the matrix will be saved. If it is unchecked, it will not be saved to the file.

There is no limit to how many matrices you can use.

Choose your file's name by writing it on the **File name** field.

When you are done click **Save to file**.

If you want to reset the fields click **Reset form**.
