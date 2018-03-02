from analyseether import app
from flask import render_template, redirect, url_for, request, flash, Markup

from models import Subscriber
from forms import Form

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        print email
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email=email)
            db.session.add(reg)
            db.session.commit()
            message = Markup("Thank you for subscribing")
            flash(message)
            return redirect(url_for('index'))
    return render_template('index.html', form=form)
