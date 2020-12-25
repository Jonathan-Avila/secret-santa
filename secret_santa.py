
import secret_santa_config
from random import shuffle
import smtplib
import ssl

def set_gift_order():
    list_of_names = secret_santa_config.get_names_of_participants()
    copy_of_names = []
    num_of_participants = len(list_of_names)
    list_of_numbers = list(range(num_of_participants + 1))[1:]
    shuffle(list_of_names)
    shuffle(list_of_numbers)
    gift_order_dict = dict(zip(list_of_numbers,list_of_names))
    return gift_order_dict, num_of_participants

def main():
    personal_info_dict = secret_santa_config.get_personal_info_dict()
    gift_order_dict, num_of_participants = set_gift_order()
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = secret_santa_config.get_sender_email()
    password = input("Please enter your password: ") # Password for email being used
    for key in gift_order_dict:
        giver_name = gift_order_dict[key]
        giver_email = personal_info_dict[giver_name][0]
        if key == num_of_participants:
            recipient_name = gift_order_dict[1]
            recipient_address = personal_info_dict[gift_order_dict[1]][1]
        else:
            recipient_name = gift_order_dict[key + 1]
            recipient_address = personal_info_dict[gift_order_dict[key + 1]][1]
        givers_email = personal_info_dict[gift_order_dict[key]][0]  # Enter receiver address
        message = """\
        Secret Santa

        Greetings {},

        You are {}\'s Secret Santa. Their address is: {}


        This is an automated message sent by Jonathan's script. Jonathan does not know the contents of this email.""".format(giver_name, recipient_name, recipient_address)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, givers_email, message)

main()
