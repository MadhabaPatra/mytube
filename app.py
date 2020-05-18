import flask
import pafy
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

def Get(url):
    myvid = pafy.new(url)
    best = myvid.getbest()
    response = [
    {'id': url,
     'youtube':"https://www.youtube.com/watch?v="+url,
     'download': best.url,
     },]
    return jsonify(response)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>My Tube Downloader</h1>
<p>An API To Generate Download Link for your youtube link.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/download/<VIDEO_ID>', methods=['GET'])
def download(VIDEO_ID):
    return Get(VIDEO_ID)

if __name__ == "__main__":
    app.run()
