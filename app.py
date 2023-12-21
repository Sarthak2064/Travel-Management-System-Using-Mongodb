from flask import Flask, render_template, request, redirect, url_for
import pymongo
from flask import Flask, jsonify

server = pymongo.MongoClient("mongodb://localhost:27017")

app = Flask(__name__)


@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/')
def landing():
    return render_template("landing.html")


@app.route('/booking')
def booking_update():
    return render_template("booking.html")


# Database
db = server["Travel"]


# login-Signup Collection

user_info = db['user_info']


@app.route('/SignUp.html', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        datab = {"username": username, "email": email, "password": password}
        user_info.insert_one(datab)
        return render_template("LogIn.html")
    return render_template("SignUp.html")


@app.route("/LogIn.html", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        datab = user_info.find_one({"email": email})
        if datab['password'] == password:
            return render_template("index.html")

    return render_template("LogIn.html")


# Customer Details
collection1 = db["customer"]


@app.route('/form1.html', methods=["GET", "POST"])
def customer():
    if request.method == "POST":
        f_name = request.form['firstName']
        l_name = request.form['lastName']
        cust_id = request.form['username']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        country = request.form['country']
        city = request.form['city']
        zip = request.form['zip']
        timestamp1 = request.form['timestamp1']

        d = {"firstname": f_name, "lastname": l_name, "username": cust_id, "contact": contact,
             "email": email, "address": address, "country": country, "city": city, "zip": zip, "timestamp1": timestamp1}
        collection1.insert_one(d)

        return redirect(url_for("bus"))
    return render_template("form1.html")


# Bus Details
collection2 = db["bus"]


@app.route('/form2.html', methods=["GET", "POST"])
def bus():
    if request.method == "POST":
        busnumber = request.form['busnumber']
        arriveal_time = request.form['arrivalTime']
        dept_time = request.form['deptTime']
        source = request.form['source']
        destination = request.form['destination']
        cost = request.form['cost']
        timestamp = request.form['timestamp']
        b = {"busnumber": busnumber, "arrivalTime": arriveal_time,
             "deptTime": dept_time, "source": source, "destination": destination, "cost": cost, "timestamp": timestamp}
        collection2.insert_one(b)
        return redirect(url_for("bill"))
    return render_template("form2.html")


# Bus Details
collection3 = db["bill"]


@app.route('/checkout.html', methods=["GET", "POST"])
def bill():
    # Fetching required data from collections
    data = collection1.find({}, {"firstname": 1, "lastname": 1, "_id": 0})
    latest_cost = collection2.find({}, {"cost": 1, "timestamp": 1, "_id": 0}).sort(
        "timestamp", pymongo.DESCENDING).limit(1)
    user = collection1.find({}, {"username": 1, "_id": 0})

    # Extracting the latest cost value
    for doc in latest_cost:
        cost = doc.get("cost")
        break  # Get the first value and break

    if request.method == 'POST':
        # Handling form submission
        paymentmethod = request.form['paymentmethod']
        seats = request.form['seats']
        fullname = request.form['fullname']
        timestamp3 = request.form['timestamp3']

        # Creating a dictionary to store billing information
        billing_info = {
            "paymentmethod": paymentmethod,
            "seats": seats,
            "fullname": fullname,
            "cost": cost,
            "timestamp3": timestamp3  # Include the latest cost in the billing info
            # You can include more fields or modify the structure as needed
        }

        # Storing billing information in collection3
        collection3.insert_one(billing_info)

        # Redirecting to the booking page after successful submission
        return redirect(url_for("booking"))

    return render_template("checkout.html", data=data, cost=cost, user=user)


# Booking Page
collection4 = db["booking"]


@app.route('/booking.html')
def booking():
    data = collection1.find()
    bus = collection2.find()
    return render_template("booking.html", data=data, bus=bus)


def route():
    return redirect(url_for("/ticket.html"))


@app.route('/ticket.html', methods=["GET", "POST"])
def ticket():
    newdata = collection1.find_one({}, {
        "firstname": 1,
        "lastname": 1,
        "username": 1,
        "contact": 1,
        "email": 1,
        "timestamp1": 1,
        "_id": 0
    }, sort=[("timestamp1", pymongo.DESCENDING)])

    newbus = collection2.find_one({}, {
        "busnumber": 1,
        "arrivalTime": 1,
        "deptTime": 1,
        "source": 1,
        "destination": 1,
        "cost": 1,
        "timestamp": 1,
        "_id": 0
    }, sort=[("timestamp", pymongo.DESCENDING)])

    newbill = collection3.find_one({}, {
        "seats": 1,
        "paymentmethod": 1,
        "timestamp3": 1,
        "cost": 1,
        "_id": 0
    }, sort=[("timestamp3", pymongo.DESCENDING)])
    return render_template("ticket.html", newdata=newdata, newbus=newbus, newbill=newbill)


# Cities
@app.route('/cities.json')
def get_cities():
    cities = {
        "cities": [
            "Mumbai",
            "Delhi",
            "Banglore",
            "Hyderabad",
            "Chennai",
            "Kolkata",
            "Pune",
            "Ahmedabad"
        ]
    }
    return jsonify(cities)


@app.route('/update.html', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':

        username = request.form['username']
        attr = request.form['attr']
        value = request.form['val']
        result = collection1.update_one({'username': username}, {
            "$set": {attr: value}})
    return render_template("update.html")


@app.route('/delete.html', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':

        username = request.form['username']
        result = collection1.delete_one({'username': username})

    return render_template("delete.html")


app.run(debug=True)
