resource "aws_dynamodb_table" "table_blog" {
  name         = "table_blogs"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "typeblog"
  range_key    = "timestampp"

  attribute {
    name = "typeblog"
    type = "N"
  }

  attribute {
    name = "timestampp"
    type = "N"
  }
}
