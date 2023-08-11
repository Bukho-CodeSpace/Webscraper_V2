from flask import Flask, render_template, request

app = Flask(__name__)

# Simulated database of registered users
registered_users = {}

@app.route('/')
def signup_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']

    if email in registered_users:
        return "Email already registered."

    registered_users[email] = {'name': name, 'surname': surname}
    return render_template('signup.html', success=True)

@app.route('/login_page')
def login_page():
    return render_template('log_in_page.html')

if __name__ == '__main__':
    app.run(debug=True)
