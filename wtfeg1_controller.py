import os, binascii
from flask import Flask, render_template
from wtfeg1_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24)) #flask-WTF: needed for CSRF

@app.route('/')
def main():
    _form = LoginForm() #private variable
    return render_template('wtfeg1_login.html', form=_form) #pass in the form instance as an arg to render_template
    
if __name__=='__main__':
    use_c9_debugger = False
    app.run(use_debugger=not use_c9_debugger, debug=True,
                    use_reloader=not use_c9_debugger, host='0.0.0.0', port=8080)