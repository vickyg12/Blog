# importing flask module
from flask import Flask, render_template

# initializing a variable of Flask
app = Flask(__name__)

# decorating index function with the app.route
@app.route('/')
def index():
    user = {'username': 'Vignesh'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengerss movie was so cool!'
        }]
    return render_template('index.html', title = 'Home', user=user, posts = posts)

if __name__ == "__main__":
   app.run()