from flask import Flask
from flask import request
import media
import sys, os

app = Flask(__name__)

@app.route('/upload')
def upload():

    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += '</body>'
    html += '</html>'
    html += '<a href="/">'
    html += '<button class="button"><b>Home</b></button>'
    html += '</a>'
    return html

@app.route('/')
def main():
    html = ''
    html += '<html>\n'
    html += '<head>'
    html += '<link type="text/css" rel="stylesheet" href="{{ url_for("static", filename="style.css") }}" />'
    html += '</head>'
    html += '<body>\n'
    html += '<h1>Welcome!</h1>'
    html += '<a href="/">'
    html += '<button class="button"><b>Home</b></button>'
    html += '</a>'
    html += '<a href="/upload">'
    html += '<button class="button"><b>Upload</b></button>'
    html += '</a>'
    html += '<a href="/collection">'
    html += '<button class="button"><b>Collection</b></button>'
    html += '</a>'
    html += '<a href="/upload">'
    html += '<button class="button"><b>Upload</b></button>'
    html += '</a>'
    html += '</body>\n'
    html += '</html>\n'
    return html

if __name__ == '__main__':
    app.run()
