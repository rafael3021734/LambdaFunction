# LambdaFunction


Amazon-EventBridge-Scheduler-Execution
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Resource": [
                "arn:aws:lambda:us-east-1:669676830092:function:teste-event-bridge-lambda:*",
                "arn:aws:lambda:us-east-1:669676830092:function:teste-event-bridge-lambda"
            ]
        }
    ]
}


{
  "Effect": "Allow",
  "Action": "lambda:InvokeFunction",
  "Resource": "arn:aws:lambda:region:account-id:function:function-name",
  "Principal": {
    "Service": "events.amazonaws.com"
  },
  "Condition": {
    "ArnLike": {
      "AWS:SourceArn": "arn:aws:events:region:account-id:rule/rule-name"
    }
  },
  "Sid": "InvokeLambdaFunction"
}


https://repost.aws/pt/knowledge-center/eventbridge-lambda-not-triggered