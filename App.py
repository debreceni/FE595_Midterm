from flask import Flask, render_template, url_for, flash, redirect
from forms import SentimentForm
from functions import get_sentiment, translate, detect


app = Flask(__name__)

app.config['SECRET_KEY'] = '359c1b53dee7a225ec6520a1911b2b4'


### Home Page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

################################ Service 1 ################################
@app.route("/service1", methods=['GET','POST'])
def service1():
    form = SentimentForm()
    if form.validate_on_submit():
        out =get_sentiment(form.text.data)
        flash('Sentiment Score: %s' %out, 'success')
    return render_template('service1.html', title = 'Sentiment', form = form)


################################ Service 2 ################################
@app.route("/service2", methods=['GET','POST'])
def service2():
    form = SentimentForm()
    if form.validate_on_submit():
        out =translate(form.text.data)
        flash('Translated: %s' %out, 'success')
    return render_template('service2.html', title = 'Language Translation', form = form)


################################ Service 3 ################################
@app.route("/service3", methods=['GET','POST'])
def service3():
    form = SentimentForm()
    if form.validate_on_submit():
        out =detect(form.text.data)
        flash('Language: %s' %out, 'success')
    return render_template('service3.html', title = 'Language Detection', form = form)

################################ Service 4 ################################
@app.route("/service4", methods=['GET','POST'])
def service4():
    form = SentimentForm()
    if form.validate_on_submit():
        out =get_sentiment(form.text.data)
        flash('Service 4 Output: %s' %out, 'success')
    return render_template('service4.html', title = 'Sentiment', form = form)


################################ Service 5 ################################
@app.route("/service5", methods=['GET','POST'])
def service5():
    form = SentimentForm()
    if form.validate_on_submit():
        out =get_sentiment(form.text.data)
        flash('Service 5 Output: %s' %out, 'success')
    return render_template('service5.html', title = 'Sentiment', form = form)

################################ Service 6 ################################
@app.route("/service6", methods=['GET','POST'])
def service6():
    form = SentimentForm()
    if form.validate_on_submit():
        out =get_sentiment(form.text.data)
        flash('Service 6 Output: %s' %out, 'success')
    return render_template('service6.html', title = 'Sentiment', form = form)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = 5000)