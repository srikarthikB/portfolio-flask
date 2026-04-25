from flask import Flask, render_template, redirect, request, flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os, traceback

app = Flask(__name__)
app.secret_key = "supersecretkey"

projects_data = [
    {
        "name": "Pitwall F1 Analytics Platform",
        "description": "A data-driven Formula 1 analytics platform to analyze driver performance, race pace, and strategy using real telemetry data.",
        "ss": "images/projects/pitwall-ss.png",
        "github": "https://github.com/srikarthikB/f1-analytics",
        "live": "https://pitwall-kar.vercel.app/",        
        "highlights": [
            "REST APIs built using FastAPI for sessions, laps, and race data",
            "Real-time telemetry analysis for driver performance insights",
            "Implemented consistency ranking, pace comparison, and stint analysis",
            "Interactive frontend for visualizing race strategies and trends",
            "Integrated external F1 data APIs for real-world datasets"
        ]
    },
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
    }
]


@app.route('/')
def home():
    return render_template('index.html', projects=projects_data)


@app.route('/contact', methods=['POST'])
def contact():
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

    except Exception as e:
        print("SENDGRID ERROR:")
        traceback.print_exc()
        flash("Email failed. Please try again.")

    return redirect('/#contact')


if __name__ == "__main__":
    app.run(debug=True)