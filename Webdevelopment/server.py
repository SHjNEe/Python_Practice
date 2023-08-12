from flask import Flask, render_template
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def hello_world():
    return render_template('./index.html')

@app.route('/blog')
def blog():
    return 'Hello World'

@app.route('/blog/2022')
def blog2():
    return 'Hello World 2022'