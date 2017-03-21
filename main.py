
import requests

from flask import Flask, render_template #renders templates - HTML from within python
app = Flask(__name__)


@app.route('/shopping') #tells decorator to tell Flsk what URL should trigger the function
def shopping():
	food = ["Cheese", "Tuna", "Beef"]
	return render_template("shopping.html", food=food)



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)



