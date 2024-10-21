from colorama import Fore, Back, Style
import sqlite3
import os
import re

# Colors
DEFAULT = '\033[0m'
GREEN = '\033[1;32m'
RED = '\033[1;31m'
YELLOW = '\033[3m\033[1;33m'
YELLOW2 = '\033[1;93m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
BOLD = '\033[1m'
BLINK = '\033[5m'

# Styles
BRIGHT = Style.BRIGHT
DIM = Style.DIM
NORMAL = Style.NORMAL
RESET_ALL = Style.RESET_ALL

# Background Colors
BACK_BLACK = Back.BLACK
BACK_RED = Back.RED
BACK_GREEN = Back.GREEN
BACK_YELLOW = Back.YELLOW
BACK_BLUE = Back.BLUE
BACK_MAGENTA = Back.MAGENTA
BACK_CYAN = Back.CYAN
BACK_WHITE = Back.WHITE

class UserRegister:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def user_exists(self, name):
        self.conect_db()
        try:
            self.cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
            user = self.cursor.fetchone()
            if user:
                return True
            return False
        except sqlite3.Error as e:
            print(f"{RED}Error checking if user exists: {e}{DEFAULT}")

    def conect_db(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        
    def desconect_db(self):
        self.conn.close()
        
    def create_table(self):
        self.conect_db()
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users 
            (id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            email TEXT, 
            age INTEGER NOT NULL);""")
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"{RED}Error creating table: {e}{DEFAULT}")
        finally:
            self.desconect_db()
    
    def insert_user(self, name, email, age):
        self.conect_db()
        if self.user_exists(name):
            print(f"{RED}User already exists!{DEFAULT}")
            return
        
        try:
            self.cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
            self.conn.commit()
            print(f"{GREEN}User registered successfully!{DEFAULT}")
           
        except sqlite3.Error as e:
            print(f"{RED}Error inserting user: {e}{DEFAULT}")
        finally:
            self.desconect_db()

    def list_users(self):
        self.conect_db()
        try:
            self.cursor.execute("SELECT * FROM users")
            users = self.cursor.fetchall()
            
            if not users:
                print(f"{RED}No users found.{DEFAULT}")
                return

            print(f"{CYAN}{BOLD}Users Registered: {MAGENTA}{len(users)}{DEFAULT}")
            print('')
            print(f"{CYAN}{'-' * 70}{DEFAULT}      {CYAN}{'-' * 15}{DEFAULT}")
            print(f"{BOLD}{'ID':<5}{'Name':<35}{'Email':<40}{'Age':<5}{DEFAULT}")
            print(f"{CYAN}{'-' * 70}{DEFAULT}      {CYAN}{'-' * 15}{DEFAULT}")
        
            for user in users:
                user_id, name, email, age = user
                email = email if email else f"{RED}{'Not informed':<40}{DEFAULT}"
                print(f"{MAGENTA}{user_id:<5}{DEFAULT}{GREEN}{name:<35}{DEFAULT}{CYAN}{email:<40}{DEFAULT}{YELLOW2}{age:<5}{DEFAULT}")

                

            print(f"{CYAN}{'-' * 70}{DEFAULT}      {CYAN}{'-' * 15}{DEFAULT}")
        except sqlite3.Error as e:
            print(f"{RED}Error listing users: {e}{DEFAULT}")
        finally:
            self.desconect_db()

    def delete_user(self, id):
        self.conect_db()
        try:
            self.cursor.execute("DELETE FROM users WHERE id = ?", (id,))
            self.conn.commit()
            print(f"{RED}User deleted successfully!{DEFAULT}")
        except sqlite3.Error as e:
            print(f"{RED}Error deleting user: {e}{DEFAULT}")
        finally:
            self.desconect_db()

    def update_user(self, id, name, email, age):
        self.conect_db()
        try:
            self.cursor.execute("UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?", (name, email, age, id))
            self.conn.commit()
            print(f"{GREEN}User updated successfully!{DEFAULT}")
        except sqlite3.Error as e:
            print(f"{RED}Error updating user: {e}{DEFAULT}")
        finally:
            self.desconect_db()

def print_title():
    print("""
                         ──────▄▀▄─────▄▀▄
                         ─────▄█░░▀▀▀▀▀░░█▄
                         ─▄▄──█░░░░░░░░░░░█──▄▄
                         █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
          ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
          ▐░█░█░█▀▀░█▀▀░█▀▄░░░█▀▄░█▀▀░█▀▀░▀█▀░█▀▀░▀█▀░█▀▀░█▀▄▌
          ▐░█░█░▀▀█░█▀▀░█▀▄░░░█▀▄░█▀▀░█░█░░█░░▀▀█░░█░░█▀▀░█▀▄▌
          ▐░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀▌
          ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
          """.format(YELLOW2, YELLOW, RED, GREEN, CYAN, MAGENTA, BLUE, DEFAULT))
    
def validate_name(name):
    return bool(name.strip()) and not name.isdigit()

def validate_age(age):
    return age.isdigit()

def validate_email(email):
    return re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email)

def main():
    print_title()
    user = UserRegister()
    user.create_table()
    while True:
        print('')
        print(f"{CYAN}{'1 - Register User':<50}{DEFAULT}")
        print(f"{CYAN}{'2 - List Users':<50}{DEFAULT}")
        print(f"{CYAN}{'3 - Delete User':<50}{DEFAULT}")
        print(f"{CYAN}{'4 - Update User':<50}{DEFAULT}")
        print(f"{CYAN}{'5 - Exit':<50}{DEFAULT}")
        print('')
        option = input(f"{YELLOW2}Choose an option: {DEFAULT}")
        print('')

        if option == '1':
            os.system('clear') if os.name == 'posix' else os.system('cls')
            print_title()
            while True:
                print('')
                print(f"{YELLOW2}Register User{DEFAULT}")
                print('')
                name = input(f"{YELLOW2}Name: {DEFAULT}")
                email = input(f"{YELLOW2}Email: {DEFAULT}")
                age = input(f"{YELLOW2}Age: {DEFAULT}")
                print('')

                if not validate_name(name):
                    print(f"{RED}Name is required and must be text!{DEFAULT}")
                    print('')
                    continue

                if not validate_email(email):
                    print(f"{RED}Email is required and must be valid!{DEFAULT}")
                    print('')
                    continue

                if not validate_age(age):
                    print(f"{RED}Age is required and must be a number!{DEFAULT}")
                    print('')
                    continue

                user = UserRegister()
                user.insert_user(name, email, age)
                break
        elif option == '2':
            os.system('clear') if os.name == 'posix' else os.system('cls')
            print_title()
            user = UserRegister()
            user.list_users()
        elif option == '3':
            os.system('clear') if os.name == 'posix' else os.system('cls')
            id = input(f"{YELLOW2}ID: {DEFAULT}")
            if not id.isdigit():
                print(f"{RED}ID is required and must be a number!{DEFAULT}")
                continue
            user = UserRegister()
            user.delete_user(id)
        elif option == '4':
            id = input(f"{YELLOW2}ID: {DEFAULT}")
            if not id.isdigit():
                print(f"{RED}ID is required and must be a number!{DEFAULT}")
                continue

            name = input(f"{YELLOW2}Name: {DEFAULT}")
            if not validate_name(name):
                print(f"{RED}Name is required and must be text!{DEFAULT}")
                continue

            email = input(f"{YELLOW2}Email: {DEFAULT}")

            if email and not validate_email(email):
                print(f"{RED}Email is required and must be valid!{DEFAULT}")
                continue
            age = input(f"{YELLOW2}Age: {DEFAULT}")

            if not validate_age(age):
                print(f"{RED}Age is required and must be a number!{DEFAULT}")
                continue

            user = UserRegister()
            user.update_user(id, name, email, age)
        elif option == '5':
            break
        else:
            print(f"{RED}Invalid option!{DEFAULT}")

if __name__ == '__main__':
    main()