from flask import Blueprint
from flask import render_template, request, redirect, session
from FlaskProj.main import db

app = Blueprint('app', __name__)

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        user = db.flask.find_one({'user': username, 'password': password})
        if user:
            session['user'] = username
            return redirect('home')
        else:
            return render_template('login.html')
    else:
        try:
            if session['user']:
                return redirect('home')
        except:
            pass
        return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        user = db.flask.find_one({'user': username, 'password': password})
        if user:
            return redirect('login')
        else:
            db.flask.insert_one({'user': username, 'password': password})
        return redirect('login')
    else:
        return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('user', default=None)
    return redirect('login')


@app.route('/about-us')
def about():
    return render_template('about.html')


@app.route('/service')
def service():
    service = db.services.find()
    return render_template('service.html', services=service)


@app.route('/contact-us', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        username = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        db.contact.insert_one({'user_name': username, 'email': email, 'message': message})
        return render_template('index.html')
    else:
        return render_template('contact.html')


@app.route('/product')
def product():
    product = db.product.find()
    return render_template('product.html', products=product)


@app.route('/term')
def term():
    return render_template('terms.html')


@app.route('/profile')
def profile():
    user = session['user']
    return render_template('profile.html', user=user)


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     app.run(debug=True)

