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
