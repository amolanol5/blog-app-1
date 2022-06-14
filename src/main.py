from flask import Flask ,request
from flask import url_for
from flask import render_template
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
    if request.method == 'POST':
        titleblog = request.form['title']
        bodyblog = request.form['bodyblog']
        
        #save the item in database
        response_db = client.put_item(
            TableName='table_blog',
            Item={
                "tittle_blog": {
                "S": titleblog
                },
                 "body_blog": {
                  "S": bodyblog
                }
            }
        )
        
        print(response_db)
        
    return render_template('pages.html', titleblog=titleblog,  bodyblog=bodyblog)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)