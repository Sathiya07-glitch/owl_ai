from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/automation')
def automation():
    return render_template('automation.html', title="Automation")

@app.route('/analytics')
def analytics():
    return render_template('analytics.html', title="Analytics")

@app.route('/custom')
def custom():
    return render_template('custom.html', title="Custom Solutions")

if __name__ == '__main__':
    app.run(debug=True)