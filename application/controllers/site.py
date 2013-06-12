from application import app
from flask import redirect
from flask import url_for
from flask import flash
from flask import render_template
from flask.ext.login import login_user
from flask import request
from application.forms.login import LoginForm
from application.models.user import User
from flask.ext.login import login_required
from flask.ext.login import logout_user
from flask.ext.login import current_user


@app.route('/')
def site_index():
    if current_user.is_authenticated():
        # redirect, load a different template...
        pass
    return render_template('site/index.html')


@app.route('/login', methods=['GET', 'POST'])
def site_login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.objects.get(email=request.form['email'])

            if user.verify_password(request.form['password']):
                login_user(user)
                flash('Logged in successfully.', 'success')

                return redirect(request.args.get('next') or url_for('site_index'))
            else:
                flash('Username or password is incorrect', 'error')
        except User.DoesNotExist:
            flash('Username or password is incorrect', 'error')
    return render_template('site/login.html', form=form)


@app.route('/logout')
@login_required
def site_logout():
    logout_user()
    return redirect(url_for('site_index'))


@app.route('/register', methods=['GET', 'POST'])
def site_register():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.objects.get(email=request.form['email'])
            if user:
                flash('This email address is already in use.', 'error')
            return render_template('site/login.html', form=form)

        except User.DoesNotExist:
            user = User()
            user.email = request.form['email']
            user.username = request.form['email']
            user.set_password(request.form['password'])
            user.save()

            flash('Successfully registered', 'success')
            return redirect(url_for('site_index'))
    return render_template('site/login.html', form=form)
