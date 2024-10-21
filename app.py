from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_pyfile("config.py")

@app.route('/')
def main():
    return "Hello, world!"

@app.route('/homepage')
def home():
    """View for the Home page of your website."""
    agent = request.user_agent
    return f"<h1>This is your homepage :) - {agent}</h1>"

@app.route('/hi/<string:name>')
def greetings(name):
    name = name.upper()
    age = request.args.get("age", 0, type=int)
    return f"Welcome {name=} {age=}", 200

@app.route('/admin')
def admin():
    to_url = url_for("greetings", name="administrator", _external=True)
    print(to_url)
    return redirect(to_url)

skills = [
        "Java, Spring, Spring Boot, Spring MVC",
        "Spring Data JPA, Hibernate",
        "RESTful API, Spring Security",
        "Thymeleaf, JSP",
        "HTML, CSS, JavaScript",
        "SQL (MySQL, PostgreSQL), MongoDB",
        "JUnit, Mockito",
        "Maven",
        "Git, GitHub, GitLab"
    ]

@app.route('/resume')
def resume():
    return render_template("resume.html", title="Resume", full_name="Дмитро Мельник", age=19, skills=skills)


if __name__ == '__main__':
    app.run(debug = True)