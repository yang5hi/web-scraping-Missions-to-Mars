from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()
    # Return template and data
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scraper():
    # Run the scrape function
    mars_data = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)
    # Redirect back to home page
    return redirect("/") #performing URL redirection

if __name__ == "__main__":
    app.run(debug=True)