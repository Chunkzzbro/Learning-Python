from flask import Flask,render_template
app = Flask(__name__)                                              

@app.route ('/')                                                #Website content after entering is sent to this url route.

def home():
    return render_template("home.html")                  #Website content is written in this function


@app.route ('/about/')                                                #Website content after entering is sent to this url route.

def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug = True)

#When script is executed from the python file directly then the __name__ = "__main__" whereas if we import a 
#file then the __name__ = "__thefilename__"

