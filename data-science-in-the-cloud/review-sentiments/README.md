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
