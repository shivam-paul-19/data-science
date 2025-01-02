from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new():
    return "This is new page"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name} !"
    return render_template('form.html')
    
@app.route('/profile/<name>')
def profile(name):
    return f"this is the prifle of {name}"

@app.route('/jinja')
def team():
    team = ['Shivam', 'Don', 'Tara']
    return render_template('team.html', team_mem=team)

if __name__ == '__main__':
    app.run(debug=True)