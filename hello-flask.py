# -*- coding: UTF-8 -*-

from flask import Flask, redirect, url_for, render_template
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def main():
    # return redirect(url_for('hello_username', username = 'peter'))
    return render_template('hello.html')
    
@app.route('/hello/<username>')
def hello_username(username):
    return 'Hello, {}'.format(username)

@app.route('/hello/<int:userid>')
def hello_userid(userid):
    return 'Hello, your Id is: {:d}'.format(userid)

if __name__ == '__main__':
    use_c9_debugger = False
    app.run(use_debugger=not use_c9_debugger, debug=True,
                    use_reloader=not use_c9_debugger, host='0.0.0.0', port=8080)