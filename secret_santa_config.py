sender_email = "sender@email.com"  # Enter the sending email address

names_of_participants = ["Anna", "Beth", "Charlie", "Daphne", "Evan", "Frank", "George"] # Enter the names of all the paricipants here as comma separated strings in a list i.e. ["Anna", "Beth", "Charlie"]
personal_info_dict = {"Anna": ("jonathanavila900@gmail.com", "1 Central Park Ave, Penthouse Suite 1"), "Beth": ("jonathanavila900@gmail.com", "2 Central Park Ave, Penthouse Suite 1"), "Charlie": ("jonathanavila900@gmail.com", "3 Central Park Ave, Penthouse Suite 1"), "Daphne": ("jonathanavila900@gmail.com", "4 Central Park Ave, Penthouse Suite 4"), "Evan": ("jonathanavila900@gmail.com", "5 Central Park Ave, Penthouse Suite 5"), "Frank": ("jonathanavila900@gmail.com", "6 Central Park Ave, Penthouse Suite 6"), "George": ("jonathanavila900@gmail.com", "7 Central Park Ave, Penthouse Suite 1")} # Enter the info of all the paricipants here as a dict with names as keys and a tuple containing an email address and physical address as the value i.e. {"Anna":(anna@email.com, "111 Main st") "Beth":(beth@email.com, "222 Main st") "Charlie":(charlie@email.com, "333 Main st")}


def get_sender_email():
    return sender_email

def get_names_of_participants():
    return names_of_participants

def get_personal_info_dict():
    return personal_info_dict
