from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model safely
try:
    with open("pickle_file.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
@cross_origin()
def predict():
    try:
        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        date_arr = request.form["Arrival_Time"]

        Journey_day = int(pd.to_datetime(date_dep).day)
        Journey_month = int(pd.to_datetime(date_dep).month)

        # Departure & Arrival Times
        Dep_hour = int(pd.to_datetime(date_dep).hour)
        Dep_min = int(pd.to_datetime(date_dep).minute)
        Arrival_hour = int(pd.to_datetime(date_arr).hour)
        Arrival_min = int(pd.to_datetime(date_arr).minute)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)

        # Total Stops
        Total_stops = int(request.form["stops"])

        # Encode Airlines
        airlines = [
            'Jet Airways', 'IndiGo', 'Air India', 'Multiple carriers',
            'SpiceJet', 'Vistara', 'GoAir', 'Multiple carriers Premium economy',
            'Jet Airways Business', 'Vistara Premium economy', 'Trujet'
        ]
        airline_input = request.form['airline']
        airline_encoding = {airline: 1 if airline == airline_input else 0 for airline in airlines}

        # Encode Source
        sources = ['Delhi', 'Kolkata', 'Mumbai', 'Chennai']
        source_input = request.form["Source"]
        source_encoding = {f"s_{src}": 1 if source_input == src else 0 for src in sources}

        # Encode Destination
        destinations = ['Cochin', 'Delhi', 'New Delhi', 'Hyderabad', 'Kolkata']
        destination_input = request.form["Destination"]
        destination_encoding = {f"d_{dest}": 1 if destination_input == dest else 0 for dest in destinations}

        # Prepare Features
        feature_list = [
            Total_stops, Journey_day, Journey_month, Dep_hour, Dep_min,
            Arrival_hour, Arrival_min, dur_hour, dur_min
        ]
        feature_list += list(airline_encoding.values())
        feature_list += list(source_encoding.values())
        feature_list += list(destination_encoding.values())

        # Make Prediction
        if model:
            prediction = model.predict([feature_list])
            output = round(prediction[0], 2)
            return render_template('home.html', prediction_text=f"Your Flight price is Rs. {output}")
        else:
            return render_template('home.html', prediction_text="Model is not loaded properly.")

    except Exception as e:
        return render_template('home.html', prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
