from flask import Flask, request
app = Flask(__name__)

@app.route('/homepage')
def home():
    """View for the Home page of your website."""
    agent = request.user_agent
    return f"<h1>This is your homepage :) - {agent}</h1>"

@app.route('/')
def main():
    return "Hello, world!"

@app.route('/hi/<string:name>')
def greetings(name):
    name = name.upper()
    age = request.args.get("age", 0, type=int)
    return f"Welcome {name=} {age=}"

if __name__ == '__main__':
    app.run(debug = True)