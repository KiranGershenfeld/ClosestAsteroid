from flask import Flask, render_template, request, redirect
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')
#Routes-------------------
#Main page redirects to portfolio
@app.route('/')
def start():
    return render_template("ClosestAsteroid.html")

if __name__ == '__main__':
    app.run(debug=True)
