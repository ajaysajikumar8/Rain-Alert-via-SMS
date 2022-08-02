import requests
from twilio.rest import Client


api_key = ""
lat = 21.897400
lng = 83.394966
account_sid = ""
auth_token = ""
twilio_num = None
my_num = None


parameters = {
    "lat" : lat,
    "lon" : lng,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
data_slice = data["hourly"][:12]


will_rain = False
for hour_data in data_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Its going to rain today, Remember to bring an Umbrella ☔",
                     from_= twilio_num,
                     to=my_num
    )
    print(message.status)


