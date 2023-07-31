from flask import Flask , render_template

app = Flask(__name__)

lessons = [{
    'title':'Request Library Course',
    'course': 'Python',
    'author':'Omar'
},
{
    'title':'Request-HTML Library Course',
    'course': 'Python',
    'author':'Ali'
},
{
    'title':'Datetime Module',
    'course': 'Python',
    'author':'Adel'
}    
]
@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',lessons=lessons)

@app.route("/about")
def about():
    return render_template('about.html',title="About")
if __name__ == "__main__" :
     app.run(debug = True)