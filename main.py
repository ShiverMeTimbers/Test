
import os
import re
import requests
import http.client
from flask import Flask, render_template #renders templates - HTML from within python
app = Flask(__name__)


@app.route("/shopping") #tells decorator to tell Flsk what URL should trigger the function
def shopping():
	food = ["Cheese", "Tuna", "Beef"]
	return render_template("shopping.html", food=food)

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/nba-t3/seasontd/2013/REG/rankings.xml?api_key={kut24tmdqv3uwm6u4gbauan2}")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

if __name__ == '__main__':
    if 'PORT' in os.environ:
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
    else:
        app.run(debug=True, port=80)



