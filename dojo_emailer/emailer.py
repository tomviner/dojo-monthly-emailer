import re

import boto3


def send_email(from_address, to_address, reply_to, subject, message_html):
    """Sends an email via Amazon SES."""
    # naive tag strip
    message_text = re.sub('<[^>]+?>', '', message_html)

    client = boto3.client('ses')
    response = client.send_email(
        Source=from_address,
        Destination={
            'ToAddresses': [
                to_address,
            ],
        },
        ReplyToAddresses=[
            reply_to
        ],
        Message={
            'Subject': {
                'Data': subject,
            },
            'Body': {
                'Text': {
                    'Data': message_text,
                },
                'Html': {
                    'Data': message_html,
                },
            },
        },
    )
    return response
