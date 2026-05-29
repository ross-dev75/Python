import requests
from datetime import datetime, date
import time
import smtplib
import os
from email.mime.text import MIMEText

# 'Naruto runner battalions' once tried to take this hill. . .
A51_LAT = 37.235000
A51_LONG = -115.811111


def get_sun_times():
    parameters = {
        "lat": A51_LAT,
        "lng": A51_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunrise, sunset


def is_over_area_51():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return A51_LAT-5 <= iss_latitude <= A51_LAT+5 and A51_LONG-5 <= iss_longitude <= A51_LONG+5

def is_night(sunrise, sunset):
    hour = datetime.now().hour

    if hour < sunrise or hour > sunset:
        return True
    else:
        return False


def send_alert():
    sender = "you@gmail.com" # Anonymized for github - replace with your own email
    recipient = "you@gmail.com" # Anonymized for github - replace with a receiving email of your choice

    msg = MIMEText("The ISS is currently over Area 51!")
    msg["Subject"] = "ISS Alert"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        # Set app password as an env var in terminal prior to running this code
        server.login(sender, os.environ["GMAIL_APP_PASSWORD"])
        server.sendmail(sender, recipient, msg.as_string())


def main():
    sunrise, sunset = get_sun_times()
    last_fetched = date.today()
    alerted = False

    while True:
        try:
            # Refresh sunrise/sunset once a day instead of every loop to avoid hammering the API
            if date.today() != last_fetched:
                sunrise, sunset = get_sun_times()
                last_fetched = date.today()

            if is_over_area_51() and is_night(sunrise, sunset):
                if not alerted:
                    print("The ISS is currently over Area 51.")
                    # send_alert() <- uncomment this line after plugging in sender/recipient emails and settings env password variable.
                    alerted = True
            else:
                print("The ISS is currently NOT over Area 51.")
                alerted = False  # Reset so the next pass triggers a new alert

        except requests.RequestException as e:
            print(f"Network error, retrying next cycle: {e}")

        time.sleep(60)

# 'if guard' to avoid running an infinite loop if someone imports this code - still wrapping my head around this
if __name__ == "__main__":
    main()