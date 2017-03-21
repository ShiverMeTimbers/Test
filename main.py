
import os
import re
import requests

from flask import Flask, render_template #renders templates - HTML from within python
app = Flask(__name__)


@app.route('/shopping') #tells decorator to tell Flsk what URL should trigger the function
def shopping():
	food = ["Cheese", "Tuna", "Beef"]
	return render_template("shopping.html", food=food)



if __name__ == '__main__':
    if 'PORT' in os.environ:
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
    else:
        app.run(debug=True, port=80)



