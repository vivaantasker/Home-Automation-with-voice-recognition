import json
import os
import serial
import time
from generate_voice import * # to call all functions from other file
from co_relation import *
from security_gui import *

def add_command_to_json(command_name, binary_string, audio_path):
    file_path=r"D:\vivaan tasker\SPIT\sem 3\sns_project\command_list.json" #literal string to prevent backspace from affecting things
    
    # Create the JSON file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump({"commands": []}, file)

    # Now read the existing commands
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = {"commands": []}  # Handle the case of a corrupt JSON file
        
    new_command = {
        "name": command_name,
        "audio_path": audio_path,
        "binary": binary_string
    }
    data["commands"].append(new_command)
    
    # Save back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def display_menu():
    print("Press: ")
    print("1. Give Command")
    print("2. Add Command")
    print("3. Delete Command")
    print("4. View Commands")
    print("5. Exit")

def give_command():
    try:
        # Open the serial port
        ser = serial.Serial('COM3', 115200)
        time.sleep(2)  # Wait for the connection to establish
        print("Port opened successfully.")
        binarydata=locate_command()
        # Remove spaces from the binary string
        binarydata = binarydata.replace(" ", "")
        
        # Convert binary string to bytes
        data = int(binarydata, 2).to_bytes((len(binarydata) + 7) // 8, byteorder='big')
        
        # Send the byte sequence
        ser.write(data)
        print(f"Sent binary data: {binarydata}")

    except serial.SerialException as e:
        print(f"Error: {e}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    finally:
        # Ensure the serial port is closed
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial connection closed.")

def add_command():
   name=input("name the command: ")
   binary=input('give the binary string: ')
   wav_file_path=audiostore(name) 
   add_command_to_json(name,binary,wav_file_path)

def delete_command():
    file_path=r"file path here" #put the file path to your json here
    todelete=input("enter the name of the command: ")
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Error reading the command list. It may be corrupted.")
        return
    commands = data.get("commands", [])
    updated_commands = [cmd for cmd in commands if cmd['name'] !=todelete]  #loop mechanism to find errors
    data["commands"] = updated_commands
        # Write back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        print(todelete+" has been deleted.")

def view_commands():
    file_path=r"file path here" #put the file path to your json here
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = {"commands": []}  # Handle the case of a corrupt JSON file
    for command in data.get("commands", []):
        print(f"Name: {command['name']}, Audio Path: {command['audio_path']}, Binary: {command['binary']}")

   
def main():
        interface()
        while True:
            display_menu()
            choice = input("Enter your choice (1-5): ")  

            if choice == '1':
                give_command()
            elif choice == '2':
                add_command()
            elif choice == '3':
                delete_command()
            elif choice == '4':
                view_commands()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
   

if __name__ == "__main__":   #ensures main runs
    main()
