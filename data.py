import requests

PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}
data = requests.get("https://opentdb.com/api.php", params=PARAMETERS)
data.raise_for_status()
questions = data.json()

question_data = questions["results"]
