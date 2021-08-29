from flask import Flask, request
import http.client, json
import config
app=Flask(__name__)

@app.route('/')
def main():
    list_of_standings = get_standings()
    return display_standings(list_of_standings)


def get_standings():
    conn = http.client.HTTPSConnection("api-basketball.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "api-basketball.p.rapidapi.com",
        'x-rapidapi-key': config.api_key
        }

    conn.request("GET", "/standings?league=12&season=2019-2020", headers=headers)

    res = conn.getresponse()
    data = res.read()
    newData = json.loads(data)

    return newData['response'][0]

def display_standings(standings):
    West = {

    }
    East = {

    }
    for i in range(30):
        if i < 15:
            West[i+1] = standings[i]['team']['name']
        else:
            East[i-14] = standings[i]['team']['name']
    res = {'West': West,
           'East': East}
    return (res)

if __name__== '__main__':
    app.run(debug=True)