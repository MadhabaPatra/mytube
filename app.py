import flask
import pafy
from flask import request, jsonify,redirect

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
    return jsonify(response)

def download(url):
    myvid = pafy.new(url)
    best = myvid.getbest()
    return redirect(best.url, code=302)

# HOME route
@app.route('/', methods=['GET'])
def home():
    return '''<h1>My Tube Downloader</h1>
<p>An API To Generate Download Link for your youtube link.</p>'''

# DOWNLOAD route
@app.route('/download/<VIDEO_ID>', methods=['GET'])
def download(VIDEO_ID):
    return download(VIDEO_ID)

# DETAILS route
@app.route('/details/<VIDEO_ID>', methods=['GET'])
def details(VIDEO_ID):
    return Get(VIDEO_ID)

# APP RUNNING
if __name__ == "__main__":
    app.run()
