# WordPress Alexa Example Skill
In this example, we're going to create a custom WordPress option and show how it can be made voice-accessible. We'll create a "Quote of the Day" that can be updated in WordPress and create a sample skill that will allow users to access this Quote of the Day via voice.

## WordPress Custom Endpoint
Find the necessary customizations to WordPress in `functions.php`.

## Alexa Skill
Find the Lambda code in `lambda.py`. This Lambda function is invoked through an Alexa skill which passes a request through AWS API Gateway.
