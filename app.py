from csv import DictReader, DictWriter
from flask import Flask, render_template, request

app = Flask(__name__)

BRANDS = [
    "Toyota",
    "BMW",
    "Nissan",
    "Honda"
]

with open("registrants.csv", "w") as file:
        keys = ["name", "brand"]
        writer = DictWriter(file, fieldnames=keys)
        writer.writeheader()

@app.route("/")
def index():
    return render_template("index.html", brands=BRANDS)

@app.route("/register", methods = ["POST"])
def check():
    name, brand = request.form.get("name"), request.form.get("brand")
    
    if not name or brand not in BRANDS:
        return render_template("failure.html")
    
    with open("registrants.csv", "a") as file:
        keys = ["name", "brand"]
        writer = DictWriter(file, fieldnames=keys)
        writer.writerow({'name': name, 'brand': brand})
        
    return render_template("registered.html")

@app.route("/registrants")
def registerd():
    with open("registrants.csv", "r") as file:
        database = DictReader(file)
        
        REGISTRANTS = {}
        for row in database:
            REGISTRANTS[row["name"]] = row["brand"]
        
    return render_template("registrants.html", registrants=REGISTRANTS)