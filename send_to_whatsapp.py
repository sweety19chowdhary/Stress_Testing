from twilio.rest import Client

def send_to_whatsapp(suggestions):
    # Twilio credentials
    account_sid = ''  # Replace with your Twilio Account SID
    auth_token = ''    # Replace with your Twilio Auth Token
    whatsapp_number = 'whatsapp:+14155238886'  # Correct Twilio Sandbox WhatsApp number
    recipient_number = 'whatsapp:+91'  # Your WhatsApp number

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    try:
        # Send the message
        message = client.messages.create(
            from_=whatsapp_number,
            body=f"Suggestions from log analysis:\n{suggestions}",
            to=recipient_number
        )
        print(f"Message sent with SID: {message.sid}")
    except Exception as e:
        print(f"Error sending message: {str(e)}")

# Read the suggestions from 'suggestions.txt'
with open('suggestions.txt', 'r') as file:
    suggestions = file.read()

# Send suggestions to WhatsApp
send_to_whatsapp(suggestions)
