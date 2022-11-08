resource "aws_iam_user" "user" {
  name = "user2"
  path = "/system/"

  tags = {
    tag-key = "madeinterraform"
  }
}