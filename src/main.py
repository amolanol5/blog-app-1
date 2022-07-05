from flask import Flask, jsonify ,request, redirect
from flask import url_for
from flask import render_template
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr
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
    
    # query data
    # dynamodb = boto3.resource('dynamodb' ,region_name='us-east-1')
    # table = dynamodb.Table('table_blogs')
    # response = table.query(
    # KeyConditionExpression=Key('typeblog').eq(1)
    # )
    #response = response["Items"]
    #print(response)
    return redirect(url_for('blog'))

@app.route("/api/blogs", methods=['GET', 'POST'])
def api_blogs():
    # query data
    if request.method == 'GET':
        
        dynamodb = boto3.resource('dynamodb' ,region_name='us-east-1')
        table = dynamodb.Table('table_blogs')
        response = table.query(
        KeyConditionExpression=Key('typeblog').eq(1)
            )
        #print(response)
        last4_elements = response["Items"][::-1]
        last4_elements = last4_elements[0:3]
        
        print(last4_elements)
        #return render_template('pages.html', last4_elements=last4_elements)
        return response


@app.route("/api/blogs/<string:blog_id>", methods=['GET', 'POST'])
def api_blog_id(blog_id):
    if request.method == 'GET':
        print(blog_id)
        dynamodb = boto3.resource('dynamodb' ,region_name='us-east-1')
        table = dynamodb.Table('table_blogs')
        response = table.query(
        KeyConditionExpression=Key('typeblog').eq(1)
        )
        
        only_one_item = [i for i in response["Items"] if i["timestampp"] ==  int(blog_id)]
        return jsonify({"message": "blog found", "blog" : only_one_item})
        
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)