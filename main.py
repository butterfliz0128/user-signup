from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    #--encoded_error = request.args.get("error")
    #return user_form
    return render_template('user-signup.html')

@app.route("/user-validate", methods=['POST'])
def user_validate():
    username_in = request.form['username']
    password_in = request.form['password']
    verify_pswd_in = request.form['verify']
    email_in = request.form['email']
    user_name_error_msg = ""
    password_error_msg = ""
    verify_error_msg = ""
    email_error_msg = ""
    error_flag = False

    if username_in:
        if " " in username_in:
            user_name_error_msg = "User name cannot contain spaces"
            error_flag = True
        else:
            if len(username_in) < 3 or len(username_in) > 20:
                user_name_error_msg = "User name must be greater than 2 characters and less than 20"
    else:
        user_name_error_msg = "You must enter a user name"
        error_flag = True

    if password_in:
        if " " in password_in:
            password_error_msg = "Password cannot contain spaces"
            error_flag = True
            password_in = ""
        else:
            if len(password_in) < 3 or len(password_in) > 20:
                password_error_msg = "Password must be greater than 2 characters and less than 20"
                error_flag = True
                password_in = ""
    else:
        password_error_msg = "You must enter a password"
        error_flag = True
        password_in = ""
    
    if verify_pswd_in:
        if verify_pswd_in != password_in:
            verify_error_msg = "Passwords do not match"
            error_flag = True
            verify_pswd_in = ""
    else:
        verify_error_msg = "You must enter the verification password"
        error_flag = True
        verify_pswd_in = ""

    email_error = False
            
    if email_in:
        count_at = email_in.count("@")
        count_period = email_in.count(".")
        
        if count_at != 1:
            email_error = True
            
        if count_period != 1:
            email_error = True

        if " " in email_in:
            email_error = True
            
        if len(email_in) < 3 or len(email_in) > 20:
            email_error + True

        if email_error == True:
            email_error_msg = "Please enter a valid email address"
            error_flag = True
    

    if error_flag:
        return render_template('user-signup.html', username_p=username_in, 
           email_p=email_in,username_error_p=user_name_error_msg,password_error_p=password_error_msg,
           verify_error_p=verify_error_msg,email_error_p=email_error_msg)
    else:
        return render_template('welcome.html',username_p=username_in,email_p=email_in)
    

app.run()
