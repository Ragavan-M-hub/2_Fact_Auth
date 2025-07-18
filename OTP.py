import random
from twilio.rest import Client

password = "rag_m@7823105"
max_attempts = 5

account_sid = ""
auth_token = ""
twilio_num = ""
user_num = ""

user_input = ""
attempt = 0

while user_input != password and attempt < max_attempts:
    try:
        user_input = input("Enter the password : ")
        attempt += 1

        if user_input == password:
            print("Generating OTP")

            otp = str(random.randint(10000,99999))

            try:
                client = Client(account_sid,auth_token)
                message = client.messages.create(
                    body = f"Your OTP is {otp}",
                    from_ = twilio_num,
                    to = user_num
                )
                print("OTP sent")
            
            except Exception as e:
                print(f"Failed to send OTP : {e}")
                break

            try:
                user_otp = input("Enter the otp : ")

                if user_otp == otp:
                    print("Logged in")
                else:
                    print("Incorrect otp")
                break

            except Exception as e:
                print(f"Error occured : {e}")
                break
        
        elif attempt == max_attempts:
            print("Too many failed attempts. Locked out.")
            break
        else:
            print(f"Incorrect password. You have {max_attempts - attempt} attempt(s) left")
    
    except Exception as e:
        print(f"Error occured: {e}")
        break

