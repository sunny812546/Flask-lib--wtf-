from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField


app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"


class Form(FlaskForm):
    firstname = StringField("Enter Your Firstname")
    lastname = StringField("Enter Your lastname")
    about = TextField("Enter About You")
    submit = SubmitField("Submit")


@app.route("/", methods=['GET', 'POST'])
def home():
    firstname = False
    lastname = False
    about = False
    form = Form()
    if form.validate_on_submit():
        firstname = form.firstname.data
        form.firstname.data = ''
        lastname = form.lastname.data
        form.lastname.data = ''
        about = form.about.data
        form.about.data = ''
    return render_template("home.html", form=form, firstname=firstname,
                           lastname=lastname, about=about)


app.run(debug=True)
