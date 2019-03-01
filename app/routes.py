from app import app
from flask import render_template, jsonify, request, redirect, url_for
import requests
from app.forms import FlickrForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired




@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # url = 'https://farm' + {farm} + '.staticflickr.com/' + {server} + '/' + {id} + '_' + {secret} + '.jpg'
    form = FlickrForm()


    if form.validate_on_submit():
        key = app.config['API_KEY']
        to_search = form.title.data
        request_url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={}&tags={}&per_page=20&format=json&nojsoncallback=1'.format(key, to_search)
        data = requests.get(request_url).json()

        print(type(data))

        return render_template('index.html', form=form, data=data)

    return render_template('index.html', form=form, data=[])
