from flask import Flask
from flask import render_template



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/2')
def hello():
    return render_template('about.html')

@app.route('/3')
def hello_worl():
    return render_template('x.html')

@app.route('/4')
def hello_wor():
    return render_template('courses.html')

@app.route('/5')
def hello_wo():
    return render_template('contact.html')

if __name__ == '__main__':
#    db.init_app(app)

    app.run(debug=True)