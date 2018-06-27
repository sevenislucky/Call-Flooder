''' Basic program to call someone infinite amount of times,
	using the twilio website it is possible to have a programmed
	voice to say what ever you like to the recipient, along with 
	a recording of the conversation/response.
''' 
from twilio.rest import Client
import time

TWILIO_PHONE_NUMBER = ["Your Twilio Number goes here"] 

DIAL_NUMBERS = ["The Number you want to call goes here"] # if you wish you can use multiple numbers ["987654321","123456789"]

TWIML_INSTRUCTIONS_URL = "https://handler.twilio.com/twiml/EHc2796bac3a66e710bef128a917569e43"

client = Client("account SID from twilio","auth token goes here")

def dial_numbers(numbers_list, tnumbers_list):
    for number in numbers_list:
        for tnumber in tnumbers_list:
            print("Flooding twat of a scammer....." + number + " " + "Using Number: " + tnumber)
            client.calls.create(to=number, from_=tnumber, url=TWIML_INSTRUCTIONS_URL, method="GET")
            time.sleep(20)
            
# change below to what ever loop you like this just never ends!! ;)            
if __name__ == "__main__":
    i = 1
    while i > 0:
        dial_numbers(DIAL_NUMBERS,TWILIO_PHONE_NUMBER)