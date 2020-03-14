from flask import Flask, request
from twilio import twiml
from twilio.rest import Client
from twilio.twiml.messaging_response import Message, MessagingResponse
from Modules.sms import init_func, SMS

account_sid = 'ACdfe59ee99f5540d6532ae2c77265df02'
auth_token = '4cf87d9c40d5962e9d7706e421ac62e9'
client = Client(account_sid, auth_token)


app = Flask(__name__)


@app.route('/', methods=['POST'])
def respondSMS():
    number = request.form['From']
    message_body = "Vroooooom"

    resp = MessagingResponse()
    resp.message('Hello {}, {}'.format(number, message_body))
    return str(resp)

def sendSMS():
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+18286046338',
        to='+18053403833'
    )

    print(message.sid)

if __name__ == '__main__':
    app.run(debug=True)
