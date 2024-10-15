from flask import Flask
app = Flask(__name__)

@app.route('/homepage')
def home():
    """View for the Home page of your website."""
    return f"This is your homepage :) "

@app.route('/')
def main():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug = True)