from flask import Flask, request
from twilio import twiml
from twilio.rest import Client
from twilio.twiml.messaging_response import Message, MessagingResponse


def init_func(child: str):
    print('Woah loo k the init functionality of: ', child)


class SMS:
    outgoing_num = "+18286046338"
    initial_msg = "Hello there world!"

