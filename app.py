from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('coming_soon.html')
    print(html_code)  # Print the HTML code in the console
@app.route('/new')
def new():
    return  render_template('new.html')


if __name__ == '__main__':
    app.run(port=7777)  # Change the port number to 7777 or any available port