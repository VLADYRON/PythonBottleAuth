from bottle import get, post, template, run, request, redirect, response
from Authentication import User

@get("/")
def index_get():
    context = {"title": "Welcome to User Login Website!"}
    
    user = request.get_cookie("account", secret="some-secret-key")
    if user:
        context["username"] = user.name 
    else:
        context["username"] = "Guest"
    
    return template("./Templates/index.html", **context)

@post("/signup")
def signup_post():
    username = request.forms.get('username')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')
    email = request.forms.get('email')
    User.sign_up(username, password, password2, email)

@post("/login")
def login_post():
    username = request.forms.get('username')
    password = request.forms.get('password')
    user = User.login(username, password)
    if (user != None):
        response.set_cookie("account", user, secret="some-secret-key")
        redirect("profile/{}".format(user.name))
    else:
        redirect("login/failed")

@post("/logout")
def logout_post():
    response.delete_cookie("account")
    redirect("/")

run(host='localhost', port=8080, debug=True)