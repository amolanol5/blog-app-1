resource "aws_dynamodb_table" "example" {
  name         = "table_blog"
  billing_mode = "PAY_PER_REQUEST"
  hash_key       = "tittle_blog"
  range_key      = "body_blog"


  attribute {
    name = "tittle_blog"
    type = "S"
  }

  attribute {
    name = "body_blog"
    type = "S"
  }
}