com_message = ""

def get_com(stdscr):
    global com_message

    return com_message

def send_com(message):
    global com_message
    com_message = message