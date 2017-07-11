from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def gretting():
    return "No Ninjas Here"

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

# @app.route('/april')
# def april():
#     return render_template("april.html")

@app.route('/ninja/<color>')
def color_ninja(color):
    if color == "red" or color == "blue" or color == "purple" or color == "orange":
        return render_template(color + ".html")
    else:
        return render_template("april.html")
        # return redirect('/april')



app.run(debug=True)



