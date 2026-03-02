from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
import traceback, os

app = Flask(__name__)

# Secret key (required for flash messages)
app.secret_key = "supersecretkey"

# ================= MAIL CONFIGURATION =================
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# IMPORTANT: Remove spaces from app password
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # NO SPACES

mail = Mail(app)
# ======================================================


@app.route('/')
def home():
    return render_template(
        'home.html',
        name="Sri Karthik",
        role="Full Stack Developer"
    )


@app.route('/about')
def about():
    return render_template(
        'about.html',
        bio="this is a short bio",
        skills=["Python", "JavaScript", "Flask"]
    )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            msg = Message(
                subject=f"Portfolio Contact from {name}",
                sender=app.config['MAIL_USERNAME'],   # Explicit sender
                recipients=[app.config['MAIL_USERNAME']]
            )

            msg.body = f"""
Name: {name}
Email: {email}

Message:
{message}
"""

            mail.send(msg)

            flash("Message sent successfully!")
            return redirect('/contact')

        except Exception:
            print("EMAIL ERROR:")
            traceback.print_exc()
            return "Email failed. Check terminal."

    return render_template('contact.html')


@app.route('/projects')
def projects():
    return render_template('projects.html', projects=[
        {
            "name": "Portfolio Website",
            "description": "A personal portfolio website built using Flask to showcase projects and skills.",
            "ss": "images/projects/portfolio-ss.png",
            "github": "https://github.com/srikarthikB/portfolio-flask.git",
            "live": "https://portfolio-flask-production-0058.up.railway.app/",
            "highlights": [
                "Dynamic routing using Flask",
                "Template rendering with Jinja2",
                "Structured multi-page architecture",
                "Static asset management",
                "Deployed using Railway"
            ]
        },
        {
            "name": "Interactive Digital Library",
            "description": "A web-based digital library allowing users to browse and explore books interactively.",
            "ss": "images/projects/digilib-ss.png",
            "github": "https://github.com/srikarthikB/interactive-digital-library",
            "live": "https://interactive-digital-library.onrender.com/",
            "highlights": [
                "Backend logic implemented using Flask",
                "Dynamic content rendering with Jinja2",
                "Modular project structure",
                "Local data handling",
                "Deployed using Render"
            ]
        }
    ])


if __name__ == "__main__":
    app.run(debug=True)