# SMS 

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACc8202cb8183c6a547282eace7fc1113a"
auth_token = 'dcc89450b6b87305957ec2f653424443'
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+13613219351",
  to="+13435409920"
)
print(message.sid)