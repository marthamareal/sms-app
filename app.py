import json

# Third party imports
from chalice import Chalice, Response
from twilio.base.exceptions import TwilioRestException

from utilities import sms

app = Chalice(app_name='sms-app')

@app.route('/service/sms/send', methods=['POST'])
def send_sms():
    request_body = app.current_request.json_body

    if request_body:
        contact_list = [json.dumps(contact) for contact in request_body.get('contact_list', None)]
        message = request_body.get('message', None)

        if contact_list and message:
            try:
                response = sms.send(message, contact_list)

                if response:
                    return Response(status_code=201,
                                    headers={'Content-Type': 'application/json'},
                                    body={'status': 'success',
                                        'data': response.sid,
                                        'message': 'SMS successfully sent'})
                else:
                    return Response(status_code=400,
                                    headers={'Content-Type': 'application/json'},
                                    body={'status': 'failure',
                                        'message': 'Please try again!!!'})
            except TwilioRestException as exc:
                return Response(status_code=400,
                                headers={'Content-Type': 'application/json'},
                                body={'status': 'failure',
                                    'message': exc.msg})
        
        return Response(status_code=400,
                                headers={'Content-Type': 'application/json'},
                                body={'status': 'failure',
                                    'message': 'Please provide the `contact_list` and `message` parameters'})

@app.lambda_function()
def run(event, context):
    print(event)
    return{'lambda function executed'}