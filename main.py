from flask import Flask, render_template #renders templates - HTML from within python
app = Flask(__name__)



@app.route("/") #tells decorator to tell Flsk what URL should trigger the function
@app.route("/<user>") 
def index(user=None): 
	return render_template("user.html", user=user)

@app.route("/shopping") #tells decorator to tell Flsk what URL should trigger the function
def shopping():
	food = ["Cheese", "Tuna", "Beef"]
	return render_template("shopping.html", food=food)


