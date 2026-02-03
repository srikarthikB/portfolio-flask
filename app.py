import os
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "message.txt")

@app.route('/')
def home():
    return render_template('home.html', name="Sri Karthik", role="Full Stack Developer")

@app.route('/about')
def about():
    return render_template('about.html', bio = "this is a short bio", skills=["Python", "JavaScript", "Flask"])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        with open(FILE_PATH, 'a') as f:
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Message: {message}\n")
            f.write("-" * 40 + "\n")

        return "Thank you for your message!"

    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=[
        {"name": "Portfolio Website", "description": "this is a basic portfolio website", "tech_stack": ["HTML", "TailwindCSS", "JavaScript", "Flask"]},
        {"name": "Interactive digital library", "description": "this is a digital library website", "tech_stack": ["Python", "Flask", "JavaScript"]},
    ])

if __name__ == "__main__":
    app.run(debug=True)