import os
from flask import Flask
from buzz import generator

app = Flask(__name__)

@app.route('/')
def generateBuzz():
    page = '<html><body><h1>'
    page += generator.generateBuzz()
    page += '</h1></body></html>'
    return page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 7000)))
