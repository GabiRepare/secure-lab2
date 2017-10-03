from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC87d93b6e2c9aed16927bf1bae8df9315"
# Your Auth Token from twilio.com/console
auth_token  = "78910343e04aaf92055ab36db426206f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+33646504232", 
    from_="+33757903970",
    body="Hello from Python!")

print(message.sid)