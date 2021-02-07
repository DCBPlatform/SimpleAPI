from twilio.rest import Client
from decouple import config

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


def send_verify_sms(number):
    number_in_string = '+' + str(number)
    verification = client.verify \
        .services(config('TWILIO_VERIFY_SERVICE_SID')) \
        .verifications \
        .create(to=number_in_string, channel='sms')

    print(verification.status)
    return verification


def verify_sms(number, code):
    number_in_string = '+' + str(number)
    code_in_string = str(code)
    verification_check = client.verify \
                           .services(config('TWILIO_VERIFY_SERVICE_SID')) \
                           .verification_checks \
                           .create(to=number_in_string, code=code_in_string)

    print(verification_check.status)
    return verification_check