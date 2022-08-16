import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", dest="action", help="Action : Encode/Decode")
    parser.add_argument("-f", "--file", dest="file",
                        help="Message file to encode or Secret file to decode.")
    arguments = parser.parse_args()
    if not arguments.action:
        parser.error("[-] Please specify a valid Action.")
    elif not arguments.file:
        parser.error("[-] Please specify a file name.")
    else:
        return arguments


def encode(message_file):
    message = ""
    secret = ""
    try:
        with open(message_file, "r") as f:
            message = f.read().strip()
        for char in message:
            for binary in bin(ord(char))[2:]:
                if binary == "0":
                    secret += " "
                elif binary == "1":
                    secret += "\t"
            secret += "\n"
        with open("SECRET.txt", "w") as f:
            f.write(secret)
            print("[+] Secret stored in SECRET.txt. Make sure to rename this file before encoding another message.")
    except FileNotFoundError:
        print(f"[!] \"{message_file}\" File not found.")


def decode(secret_file):
    secret = ""
    try:
        with open(secret_file, "r") as f:
            for line in f.readlines():
                line_value = ""
                for char in list(line)[:-1]:
                    if char == " ":
                        line_value += "0"
                    elif char == "\t":
                        line_value += "1"
                secret += chr(int(line_value, 2))
        print(f"[+] Uncovered Secret Message :\n{secret}")
    except FileNotFoundError:
        print(f"[!] \"{secret_file}\" File not found.")


if __name__ == "__main__":
    arguments = get_arguments()
    action = arguments.action
    file = arguments.file
    if action.lower() == "encode":
        encode(file)
    elif action.lower() == "decode":
        decode(file)
    else:
        print("[-] Not a valid action. Check -h/--help for more info.")
