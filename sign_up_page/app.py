from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        
        # Add your email validation logic here (e.g., sending confirmation email)
        
        return "Registration successful! Check your email for confirmation."
    
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
