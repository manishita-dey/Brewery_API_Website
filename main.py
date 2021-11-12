import requests
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

ENDPOINT = 'https://api.openbrewerydb.org/breweries'

response = requests.get(ENDPOINT)
data =response.json()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/brewerylist')
def brewery():
        return render_template('brewery_list.html', list = data)

@app.route('/search', methods=['POST'])
def search():
    search_text = request.form['search_text']
    city_text = request.form['city_text']
    response = requests.get(f'https://api.openbrewerydb.org/breweries/search?query={search_text}')
    data_2 = response.json()
    return render_template('search_result.html', list = data_2 , city = city_text)


if __name__ == "__main__":

    app.run(debug=True)
