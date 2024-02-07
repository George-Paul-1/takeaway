from twilio.rest import Client
from keys.keys import account_sid
from keys.keys import auth_token
from keys.keys import twilio_number
import datetime

def sms(target_number): 
    client = Client(account_sid, auth_token)
    client_number = target_number
    delivery_time = datetime.datetime.now() + datetime.timedelta(minutes=45)
    formatted_time = datetime.datetime.strftime(delivery_time, "%H:%M")
    message = client.messages.create(body=f"Thank you! Your order was placed and will be delivered before {formatted_time}", 
                                    to=client_number, 
                                    from_=twilio_number)



