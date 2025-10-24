import streamlit as st
import requests
import datetime

st.markdown('''
# 🚖 Taxi Fare Prediction
''')

st.markdown('''
## How much will cost your taxi? ''')

date = st.date_input("Date", datetime.date(2014,12,1))
time = st.time_input("Time", datetime.time(14,00))
pickup_datetime = datetime.datetime.combine(date, time)
pickup_latitude = st.number_input("Pickup latitude", value=40.7614327)
pickup_longitude = st.number_input("Pickup longitude", value=-73.9798156)
dropoff_latitude = st.number_input("Dropoff latitude", value=40.6513111)
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.8803331)
passenger_count = st.number_input("Passenger count", min_value=1, max_value=8, value=2)

if st.button("Predict Fare"):
    params = {
        "pickup_datetime": pickup_datetime.isoformat(),
        "pickup_latitude": pickup_latitude,
        "pickup_longitude": pickup_longitude,
        "dropoff_latitude": dropoff_latitude,
        "dropoff_longitude": dropoff_longitude,
        "passenger_count": passenger_count
    }

url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

#    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


params = {
        "pickup_datetime": pickup_datetime.isoformat(),
        "pickup_latitude": pickup_latitude,
        "pickup_longitude": pickup_longitude,
        "dropoff_latitude": dropoff_latitude,
        "dropoff_longitude": dropoff_longitude,
        "passenger_count": passenger_count
        }

response = requests.get(url, params=params)


if response.status_code == 200:
    result = response.json()
    prediction = result.get('prediction')
    st.success(f'Predicted fare: {prediction}')
else:
    st.error(f'Error: {response.status_code}, {response.text}')
