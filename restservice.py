from flask import Flask, url_for, abort, request, jsonify
import modeling
import json
import csv
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_feed_articles():
    output =[]
    with open('data/nkpg_results.csv') as csvfile: 
        reader = csv.DictReader(csvfile, delimiter='|') 
        data = {}
        for row in reader:
            data = {'title': row['title'], 'summary': row['summary'], 'link': row['link']}
            output.append(data)
        json_data = json.dumps(output) 
    return json_data

@app.route('/update', methods=['POST'])
def api_update():
    content = request.get_json(silent=True)
    return 'updated'

@app.route('/feedback/<roleid>', methods=['POST'])
def api_feedback(roleid):
    role_desc = ''
    if roleid == '1':
        role_desc = 'ice_director'
    if roleid == '2':
        role_desc = 'md_syria'
    if roleid == '3':
        role_desc = 'nkpg'
    content = request.get_json(silent=True)
    modeling.analyze_feedback(content, role_desc)
    output =[]
    with open('data/'+role_desc+'_results.csv') as csvfile: 
        reader = csv.DictReader(csvfile, delimiter='|') 
        data = {}
        for row in reader:
            data = {'title': row['title'], 'summary': row['summary'], 'link': row['link']}
            output.append(data)
        json_data = json.dumps(output) 
    return json_data

@app.route('/roles/<roleid>')
def api_roles(roleid):
    role_desc = ''
    if roleid == '1':
        role_desc = 'ice_director'
    if roleid == '2':
        role_desc = 'md_syria'
    if roleid == '3':
        role_desc = 'nkpg'
    
    modeling.retrieve_news(role_desc)
    output =[]
    with open('data/'+role_desc+'_results.csv') as csvfile: 
        reader = csv.DictReader(csvfile, delimiter='|') 
        data = {}
        for row in reader:
            data = {'title': row['title'], 'summary': row['summary'], 'link': row['link']}
            output.append(data)
        json_data = json.dumps(output) 
    return json_data


if __name__ == '__main__':
    app.run()
