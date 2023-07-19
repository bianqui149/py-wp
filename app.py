from flask import Flask, jsonify

app = Flask(__name__)

from releases import releases
from score import score

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data From Page Speed
@app.route('/score',methods=['GET'])
def google_score():
    return jsonify(score())    
 
# Get Data From Wordpress site
@app.route('/wordpress_stable',methods=['GET'])
def wordpress_stable():
    return jsonify(releases())


if __name__ == '__main__':
    app.run(debug=True, port=4000)
