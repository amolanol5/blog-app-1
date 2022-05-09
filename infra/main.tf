resource "aws_iam_user" "user" {
  name = "user1"
  path = "/system/"

  tags = {
    tag-key = "tag-test"
  }
}