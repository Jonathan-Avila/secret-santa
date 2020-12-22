from random import shuffle
import smtplib, ssl

def randomized_dict(names_1,names_2):
    shuffle(names_1)
    shuffle(names_2)
    a_dict = dict(zip(names_1,names_2))
    for key in a_dict:
        if key == a_dict[key] or a_dict[a_dict[key]] == key: # person cannot be their own secret santa. Nor can the receiver be the Secret Santa's Secret Santa
            return randomized_dict(names_1,names_2)
    return a_dict

def set_gift_order():
    names_1 = [] # Enter the names of all the paricipants here as comma separated strings in a list i.e. ["Anna", "Beth", "Charlie"]
    names_2 = []
    """
    name = " "

    while name != "":
        name = input("Enter a Name  or Leave Blank and Press Enter If There Are No More Names to Enter: ")
        names_1.append(name)
    names_1.pop(-1)
    """
    for element in names_1:
        names_2.append(element)

    return randomized_dict(names_1,names_2)

def main():
    personal_info_dict = {} # Enter the info of all the paricipants here as a dict with names as keys and a tuple containing an email address and physical address as the value i.e. {"Anna":(anna@email.com, "111 Main st") "Beth":(beth@email.com, "222 Main st") "Charlie":(charlie@email.com, "333 Main st")}

    a_dict = set_gift_order()
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "jonathansraspberrypi@gmail.com"  # Enter your the sender's email address
    password = input("Please enter your password: ")
    for key in a_dict:
        recipient_name = a_dict[key]
        giver_email = personal_info_dict[key][0]
        recipient_address = personal_info_dict[a_dict[key]][1]

        receiver_email = giver_email  # Enter receiver address
        message = """\
        Secret Santa

        Greetings {},

        You are {}\'s Secret Santa. Their address is: {}


        This is an automated message sent by Jonathan's script. Jonathan does not know the contents of this email.""".format(key, recipient_name, recipient_address)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)



main()
