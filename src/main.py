from flask import Flask, jsonify ,request, redirect
from flask import url_for
from flask import render_template
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr
import boto3

app = Flask(__name__)
client = boto3.client('dynamodb')


@app.route("/")
def index():
    return render_template('index.html')


# api definition
@app.route("/api/blogs", methods=['GET'])
def api_get_blogs():
    if request.method == 'GET':
        
        dynamodb = boto3.resource('dynamodb' ,region_name='us-east-1')
        table = dynamodb.Table('table_blogs')
        response = table.query(
        KeyConditionExpression=Key('typeblog').eq(1)
            )

        last4_elements = response["Items"][::-1]
        last4_elements = last4_elements[0:3]
        
        print(last4_elements)
        return jsonify({"Items": response["Items"]})


@app.route("/api/blogs", methods=['POST'])
def api_add_blog():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    timestamp = round(float(timestamp))
    timestampp = str(timestamp)
    
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

    return jsonify({"message": "blog inserted success", "blog" : titleblog })
    

@app.route("/api/blogs/<string:blog_id>", methods=['GET'])
def api_get_blog_id(blog_id):
    if request.method == 'GET':
        print(blog_id)
        dynamodb = boto3.resource('dynamodb' ,region_name='us-east-1')
        table = dynamodb.Table('table_blogs')
        response = table.query(
        KeyConditionExpression=Key('typeblog').eq(1)
        )
        
        only_one_item = [i for i in response["Items"] if i["timestampp"] ==  int(blog_id)]
        return jsonify({"message": "blog found", "blog" : only_one_item})
           

@app.route("/api/blogs/<string:blog_id>", methods=['DELETE'])
def api_delete_blog_id(blog_id):
    if request.method == 'DELETE':
        #print(blog_id)
        #dynamodb = boto3.resource('dynamodb' ,region_name='us-east-1')
        
        response_db = client.delete_item(
         TableName='table_blogs',
         Key={
             "typeblog": {
             "N": "1"
             },
             "timestampp": {
             "N": blog_id
             }
         }
     )
            
    return jsonify({"message": "blog item delete success"})
         
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)