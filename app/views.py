__author__ = 'stclaus'

from flask import render_template, flash, redirect

from app.forms import LoginForm
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {'nickname': 'stclaus'}
    posts = [
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, title='Hello', posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID=%s, remebmer_me=%s' % (form.openid.data, form.remember_me.data))
        return redirect('/index')
    return render_template("login.html", form=form, title='Sign In', providers=app.config['OPENID_PROVIDERS'])
