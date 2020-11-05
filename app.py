from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import json
import yaml

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)

app = Flask(__name__)
with open('data.json') as json_file:
    my_json = json.load(json_file)
    print(my_json)

with open('data.yml') as yaml_file:
    my_yaml = yaml.load(yaml_file)
    print(my_yaml)

def mensaje():
    mensaje = 'Hola desde el metodo.'
    return "alert('" + mensaje + "')"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        _name = request.form['string']
        my_json['data'].append({"string":_name})
    image_file = url_for('static', filename = my_yaml['fotografia'])
    template = env.get_template('base.html')
    return template.render(my_data=my_json['data'], headers=my_json['headers'], image_file=image_file)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug = True)