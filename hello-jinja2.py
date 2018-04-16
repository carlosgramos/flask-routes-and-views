# -*-coding:UTF-8-*-

from flask import Flask, render_template, request
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('j2_query.html')

@app.route('/process', methods=['POST'])
def process():
    _username = request.form.get('username')
    
    if _username:
        return render_template('j2_response.html', username=_username)
    else: 
        return 'Please go back and senter your name...', 400

if __name__=='__main__':
    use_c9_debugger = False
    app.run(use_debugger=not use_c9_debugger, debug=True,
                    use_reloader=not use_c9_debugger, host='0.0.0.0', port=8080)
        