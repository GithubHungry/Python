from flask import Flask, session
from checker import check_logged_in

app = Flask(__name__)
app.secret_key = '322228'


@app.route('/')
def hello() -> str:
    """Start page"""
    return 'Hello from the simple webapp.'


@app.route('/login')
def do_login() -> str:
    """login in system"""
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/page1')
@check_logged_in  # Подключаем новый декоратор
def page1() -> str:
    """Page one"""
    return 'This is page 1'


@app.route('/page2')
@check_logged_in
def page2() -> str:
    """Page two"""
    return 'This is page 2'


@app.route('/page3')
@check_logged_in
def page3() -> str:
    """Page three"""
    return 'This is page 3'


@app.route('/logout')
def do_logout() -> str:
    """logout from system"""
    session.pop('logged_in')  # also we can`t to change value to false == error
    return 'You are now logged out from system'


@app.route('/status')
def show_status() -> str:
    """Show user status"""
    if 'logged_in' in session:  # there we can`t to check value true or false to identify ==error
        return 'You are currently logged in'
    else:
        return 'You are NOT logged IN system'


if __name__ == '__main__':
    app.run(debug=True)
