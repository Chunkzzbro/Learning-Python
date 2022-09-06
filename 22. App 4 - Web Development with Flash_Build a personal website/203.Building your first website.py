from flask import Flask
app = Flask(__name__)                                              

@app.route ('/')                                                #Website content after entering is sent to this url route.

def home():
    return "Home Page"                          #Website content is written in this function


@app.route ('/about/')                                                #Website content after entering is sent to this url route.

def about():
    return "About Page" 


if __name__ == '__main__':
    app.run(debug = True)

#When script is executed from the python file directly then the __name__ = "__main__" whereas if we import a 
#file then the __name__ = "__thefilename__"

