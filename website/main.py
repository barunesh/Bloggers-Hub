from flask import Flask, render_template,flash, flash,redirect,url_for, session,request, logging, make_response, request
from data import Articles
from prediction import Predictions
import random


app = Flask(__name__)


Articles = Articles()
image_list = ['Laptop','Laptop cover','Laptop skins','Mobile','Mobile Covers','Earphone','Ipod Charger','Ipod','Laptop Charger','Mobile Charger']
def select_image(predicted='0', img='None'):
    folder='img/'
    image=[]
    list=[]
    if predicted == '1' and img != 'None':
        list = Predictions(img)
    else:
        list = image_list
    for img in list:
        img = random.choice(list)
        img = folder+img+'.jpg'
        image.append(img)
    return image

@app.route('/')
def index():
    resp = make_response(render_template('home.html',image=select_image()))
    resp.set_cookie('_predict', '0')
    resp.set_cookie('_img','None')
    return resp

@app.route('/dashboard')
def dashboard():
    predicted = request.cookies.get('_predict')
    img = request.cookies.get('_img')
    image=[]
    image = select_image(predicted, img)
    return render_template('dashboard.html', articles=Articles,image=image)

@app.route('/about')
def about():
    predicted = request.cookies.get('_predict')
    img = request.cookies.get('_img')
    image=[]
    image = select_image(predicted, img)
    return render_template('about.html',image=image)

@app.route('/contact')
def contact():
    predicted = request.cookies.get('_predict')
    img = request.cookies.get('_img')
    image=[]
    image = select_image(predicted, img)
    return render_template('contact.html',image=image)

@app.route('/articles')
def articles():
    predicted = request.cookies.get('_predict')
    img = request.cookies.get('_img')
    image=[]
    image = select_image(predicted, img)
    return render_template('articles.html', articles=Articles,image=image)

@app.route('/article/<string:id>/')
def article(id):
    predicted = request.cookies.get('_predict')
    img = request.cookies.get('_img')
    image=[]
    image = select_image(predicted, img)
    return render_template('article.html', id=id , articles=Articles,image=image)

if __name__ == '__main__':
    app.run(debug=True)
