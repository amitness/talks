# Case Study: Customer Reviews Sentiment Analysis

1. Create a lambda function with a role attached to allow access to comprehend. 

2. In the lambda handler, extract {'text': '...'} sent by user and find sentiment using comprehend via boto3.

```python
import boto3
import json


def lambda_handler(event, context):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-2')
    result = comprehend.detect_sentiment(Text=event['text'], LanguageCode='en')
    return {
        'statusCode': 200,
        'sentiment': result['Sentiment']
    }
```

3. Use API gateway to create an API to this lambda function
