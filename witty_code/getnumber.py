# def get_number():
#     """
#     A witty function to ask for a girl's number.
#     """
#     print("Hey there! I've been doing some calculations, and I've come to the conclusion that we'd make a great pair.")
#     print("But I need one more crucial piece of data to complete my equation: your phone number!")
#     print("What do you say? Can you help me solve this mystery?")
#     return input("Enter your number: ")

# # Example usage:
# if __name__ == "__main__":
#     number = get_number()
#     print(f"Thanks! I'll be sure to call you soon. 😉")


def get_contact_info():
    """
    A function to retrieve contact info.
    """
    print("Hey there! I've been doing some calculations, and I've come to the conclusion that we'd make a great pair.")
    print("But I need one more crucial piece of data to complete my equation: your contact info!")
    print("What do you say? Can you help me solve this mystery?")
    
    method = input("How would you like me to contact you? (text/call/address): ")
    if method.lower() == "text":
        return input("Great! I promise not to text you too much. Enter your number: ")
    elif method.lower() == "call":
        return input("Perfect! I've been told I have a great phone voice. Enter your number: ")
    elif method.lower() == "address":
        return input("Fantastic! I make a mean casserole. Enter your address: ")
    else:
        return "Oops! Looks like there was a typo. Let's try that again."

# Example usage:
if __name__ == "__main__":
    contact_info = get_contact_info()
    method = contact_info.split()[0]  # Extract the first word from the contact info
    print(f"Thanks! I'll call you soon. 😉")
