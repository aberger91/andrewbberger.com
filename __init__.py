from flask import Flask
app = Flask(__name__)

import andrewbberger.views

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')
