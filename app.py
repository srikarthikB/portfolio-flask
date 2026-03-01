import os
from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.secret_key = "supersecretkey"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "sri2006karthik@gmail.com"
app.config['MAIL_PASSWORD'] = "zzvw joxm crdn vowh"
app.config['MAIL_DEFAULT_SENDER'] = "sri2006karthik@gmail.com"

mail = Mail(app)

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

        msg = Message(
            subject=f"Portfolio Contact from {name}",
            sender="sri2006karthik@gmail.com",
            recipients=["sri2006karthik@gmail.com"]
        )
        
        msg.body = f""" Name: {name}
                        Email: {email}
                        Message:{message}"""

        mail.send(msg)

        flash("Message sent successfully!")
        return redirect('/contact')
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=[
        {"name": "Portfolio Website",
         "description": "this is a basic portfolio website",
         "tech_stack": ["HTML", "TailwindCSS", "JavaScript", "Flask","Python"],
         "logo":"images/projects/portfolio_favicon.png",
         "github":"https://github.com/srikarthikB/portfolio-flask.git",
         "live":"https://portfolio-flask-five.vercel.app/"},
        {"name": "Interactive digital library",
         "description": "this is a digital library website",
         "tech_stack": ["Python", "Flask", "JavaScript", "TailwindCSS"],
         "logo":"images/projects/idl_favicon.png",
         "github":"https://github.com/sri16/interactive-digital-library",
         "live":"https://interactive-digital-library.onrender.com/"},
    ])

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)