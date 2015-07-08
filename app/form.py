# coding=utf-8
import sys
reload(sys)  
sys.setdefaultencoding('utf-8')  
from flask import Flask, request, render_template
from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegistrationForm(Form):
    username = TextField('注册帐号', [validators.Length(min=4, max=25)])
    email = TextField('邮箱地址', [validators.Length(min=6, max=35)])
    password = PasswordField('请输入密码', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('确认密码')
    accept_tos = BooleanField('同意协议', [validators.Required()])

app = Flask(__name__)
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.debug = True
    app.run()
