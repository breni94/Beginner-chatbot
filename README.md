# Beginner-chatbot
Beginner chatbot created and integrated into Slack.

Requirements:
Python
AWS Lambda
AWS S3
AWS API Gateway
Slack
Postman

Steps:
•	Write the chatbot’s code in Python.
•	Run the chatbot on your local machine.
AWS
•	Log in to the AWS Management Console, go to the Lambda service.
• Create a Lambda service, compress the Python code into a .zip file.
•	Upload this .zip file to the Lambda function's code section.
• If the file is too large, create an S3 bucket and upload the .zip file there.
• Set the Lambda permissions, assign an IAM role to access the services.
• Go to the API Gateway and create a REST API: this will act as an interface for the Lambda service.
• Link the API Gateway to the Lambda function by setting it as the integration target for a specific route (e.g., /slack/events).
• Deploy the API.
•	Copy the endpoint URL provided after deploying the API. This will be the Request URL for Slack.
SLACK
To configure the Chatbot:
Go to Slack API Apps
• Create the app, select the scopes and permissions for the bot (scopes&permissions.doc).
•	Enable event subscriptions for the app.
•	Add the API Gateway endpoint URL to the Request URL field.
•	Slack will send a verification request to the API Gateway endpoint.
•	Ensure the Lambda function responds with the challenge parameter to complete verification.
Postman
•	Send a test POST request to the /slack/events endpoint using a tool like Postman.
Troubleshoot if needed: Inspect logs in AWS CloudWatch (for Lambda) and the Slack Events API (for Slack).
Test the Chatbot in Slack. If you still can't send messages to the Chatbot despite assigning the proper permissions, go to Slack app > Settings > Help > Clear Cache and Restart.
Chatbot is operational.
