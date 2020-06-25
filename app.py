import flask
import pafy
import json
from flask import request, jsonify,redirect,render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Get Details of Youtube VIDEO ID
# ex: VIDEO_URL=TQSaPsKHPqs

def Get(url):
    myvid = pafy.new(url)
    best = myvid.getbest()
    response = [
    {'id': url,
     'youtube':"https://www.youtube.com/watch?v="+url,
     'download': best.url,
     },]
     
    return render_template('details.html',download=best.url,name=myvid.title)

def download(url):
    myvid = pafy.new(url)
    best = myvid.getbest()
    return redirect(best.url, code=302)

# HOME route
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def getvalue():
    try:
        link=request.form['link']
        myvid = pafy.new(link)
        best = myvid.getbest()
        audiostreams = myvid.audiostreams
        return render_template('details.html',link=link,name=myvid.title,thumb=myvid.thumb,streams=myvid.streams,audiostreams=audiostreams,rating=myvid.rating,author=myvid.author,duration=myvid.duration,likes=myvid.likes,dislikes=myvid.dislikes)
    except:
            return render_template('home.html',invalid="invalid video url")
# DOWNLOAD route
@app.route('/download/<VIDEO_ID>', methods=['GET'])
def getdownloadlink(VIDEO_ID):
    return download(VIDEO_ID)

# DETAILS route
@app.route('/details/<VIDEO_ID>', methods=['GET'])
def details(VIDEO_ID):
    return Get(VIDEO_ID)

# APP RUNNING
if __name__ == "__main__":
    app.run()
