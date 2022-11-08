resource "aws_s3_bucket" "test2" {
  bucket = "test2022-amolanol"
  acl    = "private"
  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["PUT", "POST", "GET"]
    allowed_origins = ["*"]
    max_age_seconds = 3000

  }
}

# resource "aws_s3_bucket_policy" "policytest2" {
#   bucket = aws_s3_bucket.test2.id
#   policy = <<POLICY
# {
#      "Version": "2008-10-17",
#      "Statement": [
#          {
#              "Sid": "AddPatern",
#              "Effect": "Allow",
#              "Principal": "*",
#              "Action": "",
#              "Resource": "${aws_s3_bucket.test2.arn}/*"
#          }
#      ]
# }
# POLICY
# }

# resource "aws_s3_bucket_public_access_block" "block_s3" {
#     bucket = aws_s3_bucket.test2.id

#     block_public_acls = true
#     block_public_policy = true
#     restrict_public_buckets = true
#     ignore_public_acls = true

# }