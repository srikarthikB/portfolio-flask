from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name="Sri Karthik", role="Full Stack Developer")

@app.route('/about')
def about():
    return render_template('about.html', bio = "this is a short bio", skills=["Python", "JavaScript", "Flask"])

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=[
        {"name": "Portfolio Website", "description": "this is a basic portfolio website", "tech_stack": ["HTML", "TailwindCSS", "JavaScript", "Flask"]},
        {"name": "Interactive digital library", "description": "this is a digital library website", "tech_stack": ["Python", "Flask", "JavaScript"]},
    ])

if __name__ == "__main__":
    app.run(debug=True)