from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('homepage.html')

def is_blank(str):
    if str == []:
        return True

@app.route('/', methods=['POST'])
def validate_input(): 
    username = request.form['username']    
    password = request.form['password']
    verifypass = request.form['verifypass']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verifypass_error = ''
    email_error = ''

    if not is_blank(username):
        username_error = 'Not a valid username'
        username = ''
    else:
        username = ''
        if len(username) > 20 or len(password) <3:
            username_error = 'Username lenth out of range (3-30)'
            uername = ''

    if not is_blank(password):
        password_error = 'Not a valid password'
        password = ''
    else: 
        password = ''
        if len(password) > 20 or len(password) < 3:
            password_error = 'Password length out of range (3-20)'
            password = ''
    
    if verifypass != password:
        verifypass_error = 'Password does not match!'
        verifypass = ''
    else:
        verifypass = ''

    if not is_blank (email):
        if '@' not in email and '.' not in email and '' in email: 
            email_error = 'Not a valid email address'
            email = ''
    
        else: 
            email = ''
            if len(email) > 20 or len(email) < 3:
                email_error = 'email length out of range (3-20)'
                email = ''
    
    if not username_error and not password_error and not verifypass_error and not email_error:
        username = ''
        return redirect('/welcome?username={0}'.format(username))
    
    else:
        return render_template('homepage.html', 
            username_error=username_error, 
            email_error=email_error,
            username=username,
            email=email)
            

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcomepage.html', name=username)

app.run()
