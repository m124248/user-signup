from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('homepage.html')


def is_blank(str):
    if str == []:
        return True

@app.route('/signup', methods=['POST'])
def validate_input():
    username = request.form['username']
    password = request.form['password']
    verifypass = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verifypass_error = ''
    email_error = ''

    if is_blank(username):
        username_error = 'Not a valid username'
        username = ''
    else:
        if len(username) > 20 or len(username) < 3:
            username_error = 'Username lenth out of range (3-30)'
            username = ''

    if is_blank(password):
        password_error = 'Not a valid password'
        password = ''
    else:
        if len(password) > 20 or len(password) < 3:
            password_error = 'Password length out of range (3-20)'
            password = ''

    if verifypass != password:
        verifypass_error = 'Password does not match!'
        verifypass = ''

    if email:
        if email.count("@") < 1 or email.count("@") > 1:
            email_error = 'Not a valid email'
        if email.count(".") < 1 or email.count(".") > 1:
            email_error = 'Not a valid email'
        if " " in email:
            email_error = "Not a valid email"
        if len(email) < 3 or len(email) > 20:
            email_error = "Email length out of range(3-20)"

    if not username_error and not password_error and not verifypass_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('homepage.html',
                               username_error=username_error,
                               email_error=email_error,
                               password_error=password_error,
                               verifypass_error=verifypass_error,
                               username=username,
                               email=email)


@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcomepage.html', name=username)


app.run()
