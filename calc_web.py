from flask import Flask
from flask import render_template

# creates a Flask application
app = Flask(__name__, template_folder='templates/')

@app.route("/")
       :

           def tipcalc_web():
    return render_template('index.html')

# run the application
app.run(debug=True)
