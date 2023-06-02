provider "aws" {
  region = "us-west-2"
}

resource "aws_iam_role" "eventbridge_role" {
  name = "eventbridge-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_policy" "eventbridge_policy" {
  name        = "eventbridge-policy"
  description = "Permissions for EventBridge"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "events:CreateEventBus",
        "events:Put*",
        "events:Remove*",
        "events:Delete*",
        "events:TagResource"
      ],
      "Resource": "*"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "eventbridge_policy_attachment" {
  role       = aws_iam_role.eventbridge_role.name
  policy_arn = aws_iam_policy.eventbridge_policy.arn
}

resource "aws_cloudwatch_event_bus" "my_event_bus" {
  name = "my-event-bus"
}
