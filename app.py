import subprocess
import os

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "Admin@123"

def run_command(user_input):
    subprocess.call(user_input, shell=True)

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

def main():
    print("Secure Banking Application")
    print("Admin username:", ADMIN_USERNAME)
    print("Admin password:", ADMIN_PASSWORD)

    command = input("Enter command: ")
    run_command(command)

if __name__ == "__main__":
    main()