from flask import Flask ,request
from flask import url_for
from flask import render_template
from datetime import datetime
import boto3


app = Flask(__name__)
client = boto3.client('dynamodb')

name="andres"


# routes
@app.route("/")
def index():
    return render_template('index.html', name=name)

@app.route("/process", methods=['GET', 'POST'])
def process():
    # current date and time
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    timestamp = round(float(timestamp))
    timestampp = str(timestamp)

    if request.method == 'POST':
        titleblog = request.form['title']
        bodyblog = request.form['bodyblog']
        
        # save the item in database
        response_db = client.put_item(
             TableName='table_blogs',
             Item={
                  "typeblog": {
                 "N": "1"
                 },
                 "timestampp": {
                 "N": timestampp
                 },
                 "tittle_blog": {
                 "S": titleblog
                 },
                  "body_blog": {
                   "S": bodyblog
                 }
             }
         )
        print(timestampp)
        print(response_db)
        
    return render_template('pages.html', titleblog=titleblog,  bodyblog=bodyblog)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)