from flask import Flask, render_template, redirect, request, flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os, traceback

app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    projects_data = [
        {
            "name": "Interactive Digital Library",
            "description": "A web-based digital library allowing users to browse and explore books interactively.",
            "ss": "images/projects/digilib-ss.png",
            "github": "https://github.com/srikarthikB/interactive-digital-library",
            "live": "https://interactive-digital-library-production.up.railway.app/",
            "highlights": [
                "Backend logic implemented using Flask",
                "Dynamic content rendering with Jinja2",
                "Modular project structure",
                "Local data handling",
                "Deployed using Render"
            ]
        },
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
        }
    ]

    return render_template('projects.html', projects=projects_data)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

            email_message = Mail(
                from_email='sri2006karthik@gmail.com',
                to_emails='sri2006karthik@gmail.com',
                subject=f'Portfolio Contact from {name}',
                plain_text_content=f"""
Name: {name}
Email: {email}

Message:
{message}
"""
            )

            response = sg.send(email_message)
            print("SENDGRID STATUS:", response.status_code)
            print("SENDGRID BODY:", response.body)
            print("SENDGRID HEADERS:", response.headers)

            flash("Message sent successfully!")
            return redirect('/contact')

        except Exception as e:
            print("SENDGRID ERROR:")
            traceback.print_exc()
            return "Email failed. Check logs."

    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)