# -*-coding:UTF-8-*-

#import wtf, wtf fields, and wtf validators
import sys
sys.path.append('/home/ec2-user/environment/test-env2/lib/python3.6/site-packages')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField 
from wtforms.validators import InputRequired, Length 

#create login form class...inherits from FlaskForm
class LoginForm(FlaskForm): 
    username = StringField('User Name:', validators=[InputRequired(), Length(max=20)])
    passwd = PasswordField('Password:', validators=[Length(min=4, max=16)])
