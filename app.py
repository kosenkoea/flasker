from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = ['evgenii','ivan','yura','irina']
    return render_template('index.html',users=users)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name = name)

# Error 404. Page not found.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error 500. Internal server error.
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)