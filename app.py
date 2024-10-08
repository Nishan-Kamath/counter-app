from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/handle_click_index', methods=['POST'])
def handle_click_index():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)