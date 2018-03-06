from analyseether import app, db
from flask import render_template, redirect, url_for, request, flash, Markup
from models import Subscriber
from forms import Form
from token import generate_confirmation_token, confirm_token
from email import send_email
import datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(Subscriber).filter(Subscriber.email == email).count():
            subscriber = Subscriber(email=email, confirmed=False)
            db.session.add(subscriber)
            db.session.commit()

            token = generate_confirmation_token(subscriber.email)
            confirm_url = url_for('confirm_email', token=token, _external=True)
            html = render_template('emails/subscribers.html', confirm_url=confirm_url)
            subject = "Please confirm your subscription to analyseether.com"

            send_email(subscriber.email, subject, html)
            message = Markup("Thank you for subscribing, you will receive a \
                             verification email soon")
            flash(message)

            return redirect(url_for('index', _anchor='signUpForm'))
    return render_template('index.html', form=form)


@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')

    subscriber = Subscriber.query.filter_by(email=email).first_or_404()
    if subscriber.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        subscriber.confirmed = True
        subscriber.confirmed_on = datetime.datetime.now()
        db.session.add(subscriber)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('index', _anchor='signUpForm'))
