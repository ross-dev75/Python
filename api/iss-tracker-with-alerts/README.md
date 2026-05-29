# ISS Area 51 Alert

## What it does

Polls the public ISS-position and sunrise/sunset APIs once a minute. When the International Space Station passes over Area 51 during local nighttime, it prints a message — and, if configured, sends an email alert via Gmail SMTP.

## Key concepts

- Consuming JSON HTTP APIs with `requests`
- Bounding-box check on latitude/longitude
- Throttling external calls (sunrise/sunset fetched once per day, not per loop)
- Edge-triggered alerting (a flag prevents repeat emails while the ISS lingers in range)
- Sending email via `smtplib` + `MIMEText` with credentials read from an environment variable

## How it works

`get_sun_times()` hits sunrise-sunset.org for Area 51's coordinates and extracts the UTC hour for each. `is_over_area_51()` hits open-notify.org for the ISS's current position and returns `True` if it falls within a ±5° box around the target. The main loop sleeps 60 seconds between checks, refreshes sunrise/sunset on date rollover, and uses an `alerted` flag so the email only fires on the rising edge of "in range + nighttime."

## How to run

```
$ pip install requests
$ python main.py
```

To enable email alerts:

1. Replace the sender/recipient placeholders in `send_alert()`.
2. Set a Gmail app password in your shell: `export GMAIL_APP_PASSWORD="..."`
3. Uncomment the `send_alert()` call in `main()`.
