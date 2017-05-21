from flask import Flask, url_for, abort, request, jsonify
import json
import csv
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

'''@app.route('/article', methods = ['POST'])
def api_article():
    if not request.json:
        abort(400)
    print(jsonify(request.json)
    return request.json '''

@app.route('/articles')
def api_feed_articles():
    output =[]
    with open('/Users/jaircastillo/Downloads/training_data.csv') as csvfile: 
        reader = csv.DictReader(csvfile) 
        data = {}
        for row in reader: 
            data = {'title': row['title'], 'summary': row['summary'], 'link': row['link']}
            output.append(data)
        json_data = json.dumps(output) 
    return json_data

@app.route('/ventas/<articleid>')
def api_ventas(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run()