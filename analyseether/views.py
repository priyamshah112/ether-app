from analyseether import app, db
from flask import render_template, redirect, url_for, request, flash, Markup
from models import Subscriber
from forms import Form
from token import generate_confirmation_token, confirm_token, \
                  TOKEN_EXPIRATION_SECONDS
from email import send_email
import datetime

TOKEN_EXPIRATION_MINUTES = TOKEN_EXPIRATION_SECONDS/60
@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    if request.method == 'POST' and form.validate():
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(Subscriber).filter(Subscriber.email == email).count():
            subscriber = Subscriber(email=email, confirmed=False)
            db.session.add(subscriber)
            db.session.commit()

            token = generate_confirmation_token(subscriber.email)
            confirm_url = url_for('confirm_email', token=token, _external=True)
            html = render_template('emails/subscribers.html',
                                   confirm_url=confirm_url,
                                   token_time_limit=TOKEN_EXPIRATION_MINUTES)
            subject = "Please confirm your subscription to analyseether.com"
            send_email(subscriber.email, subject, html)

            message = Markup("Thank you for subscribing")
            flash(message)

            return redirect(url_for('index', _anchor='signUpForm'))

        else:  # The subscriber email exists in the database
            subscriber = Subscriber.query.filter_by(email=email).first_or_404()

            if subscriber.confirmed: # the subscriber has confirmed his email
                message_email_already_verified = Markup('This email has already been verified')
                flash(message_email_already_verified)
            else:  # resent the confirmation email
                token = generate_confirmation_token(subscriber.email)
                confirm_url = url_for('confirm_email', token=token, _external=True)
                html = render_template('emails/subscribers.html',
                                       confirm_url=confirm_url,
                                       token_time_limit=TOKEN_EXPIRATION_MINUTES)
                subject = "Please confirm your subscription to analyseether.com"
                send_email(subscriber.email, subject, html)

                message_token_resent = Markup('Email exists, we have resent you \
                                              a verification email.')
                flash(message_token_resent)
            return redirect(url_for('index', _anchor='signUpForm'))
    elif request.method == 'POST' and not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                message_validation_error = Markup(error)
                flash(message_validation_error)
        return redirect(url_for('index', _anchor='signUpForm'))

    return render_template('index.html', form=form)


@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
        subscriber = Subscriber.query.filter_by(email=email).first_or_404()
        if subscriber.confirmed:
            message_email_already_verified = Markup('This email has already been verified')
            flash(message_email_already_verified)
        else:
            subscriber.confirmed = True
            subscriber.confirmed_on = datetime.datetime.now()
            db.session.add(subscriber)
            db.session.commit()
            message_email_verified = Markup('Your email has been verified')
            flash(message_email_verified)
    except:
        print "reached expect condition in confirn"
        message_expired_token = Markup('The confirmation link is invalid or has expired.')
        flash(message_expired_token)

    return redirect(url_for('index', _anchor='signUpForm'))
