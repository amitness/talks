# boto3 is SDK provided by AWS for python
import boto3

# Create a rekognition client
client = boto3.client('rekognition')

# Read and pass binary image to rekognition
response = client.detect_labels(
    Image={
           'Bytes': open('pic.jpg', 'rb').read(),
    },
    MaxLabels=3,
    MinConfidence=95
)

for label in response['Labels']:
    print(label['Name'], label['Confidence'])

label_names = [label['Name'] for label in response['Labels']]

# Detect weapon in image
if 'Weapon' in label_names:
    print("Alert Authority")
