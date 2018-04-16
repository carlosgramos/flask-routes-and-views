import os, binascii
from flask import Flask, render_template, flash, redirect, url_for
from wtfeg2_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24)) #flask-WTF: needed for CSRF

@app.route('/', methods=['GET', 'POST'])
def main():
    _form = LoginForm() #private variable
    if _form.validate_on_submit():
        if (_form.username.data == 'Peter' and _form.passwd.data == 'xxxx'):
            return redirect(url_for('startapp'))
        else: 
            #This branch executes regardless on the first time, you either request the '/' with 'GET', in which case you get 
            #redirected to login form, or you entered the wrong username and password, wich also returns the login form
            flash('Wrong username or password')
    return render_template('wtfeg2_login.html', form=_form) #pass in the form instance as an arg to render_template
            
@app.route('/startapp')
def startapp():
    return 'The app starts here!'
            
if __name__=='__main__':
    use_c9_debugger = False
    app.run(use_debugger=not use_c9_debugger, debug=True,
                    use_reloader=not use_c9_debugger, host='0.0.0.0', port=8080)