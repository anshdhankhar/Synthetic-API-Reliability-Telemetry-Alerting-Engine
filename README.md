# Synthetic-API-Reliability-Telemetry-Alerting-Engine (V1)

A beginner-friendly command-line program that checks a single HTTP/HTTPS URL and tells you if it is **UP** or **DOWN**.

## What V1 does

- Prompts you for one URL
- Sends a single GET request (10-second timeout)
- Measures response time in milliseconds
- Treats HTTP status codes **200–399** as UP
- Treats **400–599**, bad URLs, connection errors, and timeouts as DOWN
- Prints clear messages instead of crashing on errors

## Requirements

- Python 3.10 or newer (for built-in type hints like `int | None`)
- The `requests` library (see `requirements.txt`)

## Install dependencies

From the project folder (`api-uptime-monitoring-system`):

```bash
cd api-uptime-monitoring-system
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run the program

```bash
python app/main.py
```

When prompted, enter a full URL, for example:

```text
https://httpbin.org/status/200
```

## Example output (UP)

```text
URL: https://httpbin.org/status/200
Status: UP
HTTP status code: 200
Response time: 523.41 ms
```

## Example output (DOWN)

```text
URL: https://httpbin.org/status/404
Status: DOWN
HTTP status code: 404
Response time: 412.08 ms
```

## Project layout

```text
api-uptime-monitoring-system/
├── app/
│   └── main.py
├── requirements.txt
└── README.md
```
