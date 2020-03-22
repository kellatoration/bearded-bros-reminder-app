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
    message_body = ""
    number = request.form['From']
    body = request.form['Body'].lower()
    print(body)
    if 'details' in body:
        message_body = "Details start are $125, depending on severity and care needed " \
                       "Please send us photos so we can provide an accurate estimate. Thank you."
    elif 'hours' in body:
        message_body = 'Our normal hours of operation are 8am - 5pm 7 days a week.'
    elif 'notify' in body:
        notifySMS()
    else:
        message_body = 'Please reply with "hours" ' \
                        'to see our regular business hours, or reply "details" for information on our detailing ' \
                        'services. Thank you.'
    resp = MessagingResponse()
    print(MessagingResponse)
    resp.message('Thank you for contacting Bearded Bros Detailing. {}'.format(message_body))
    return str(resp)


def sendSMS():
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+18286046338',
        to='+18053403833'
    )

    print(message.sid)


def notifySMS():
    notification = client.notify.services('ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
        .notifications.create(
        to_binding='{"binding_type":"sms", "address":"+18053403833"}',
        body='Knok-Knok! This is your first Notify SMS')
    print(notification.sid)

if __name__ == '__main__':
    app.run(debug=True)
