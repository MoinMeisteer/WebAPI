from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control')
def control_panel():
    return render_template('control_panel.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)