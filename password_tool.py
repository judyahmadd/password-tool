import random
import string
import os
from cryptography.fernet import Fernet


KEY_FILE = "secret.key"


def check_strength(password):
    
    
    score = 0
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.islower():
            has_lower = True
            
        elif char.isupper():
            has_upper = True
            
        elif char.isdigit():
            has_digit = True
            
        else:
            has_special = True
            
    
    if has_lower:
        score += 15
        
    if has_digit:
        score +=15
        
    if has_upper:
        score +=15
        
    if has_special:
        score +=15
    
    if len(password) >= 8:
        score += 20
        
        
    if len(password) >= 12:
        
        score += 20
        
    return score



def get_strength_label(score):
    
    
    
    if score < 40:
        return "Weak"
    elif score < 70:
        return "Medium"
    elif score < 90:
        return "Strong"
    else:
        return "Very Strong"
    




def generate_password(length=12, include_uppercase=True, include_digits=True, include_symbols=True):
    
    pool = string.ascii_lowercase
    
    if include_uppercase:
        pool += string.ascii_uppercase
        
        
    if include_digits:
        pool += string.digits
        
        
    if include_symbols:
        pool += string.punctuation
        
        
    password = ""
    
    for _ in range(length):
        password += random.choice(pool)
        
    return password




def load_or_create_key():
    if os.path.exists(KEY_FILE):
        
        with open(KEY_FILE, "rb") as f:
            return f.read()
        
        
    else:
        key = Fernet.generate_key()
        with open (KEY_FILE, "wb") as f:
            f.write(key)
            
        return key
    
    
    
def save_password(name, password):
    
    key = load_or_create_key()
    
    cipher = Fernet(key)
    
    encrypted = cipher.encrypt(password.encode()).decode()
    
    with open("passwords.txt", "a") as f:
        f.write(f"{name} | {encrypted}\n")
    
    
    

def list_passwords():
    
    if not os.path.exists("passwords.txt"):
        print("No saved passwords yet!")
        return
        
        
    key = load_or_create_key()
    cipher = Fernet(key)

    print("\n --- Saved Passwords ---")
    
    
    with open("passwords.txt", "r") as f:
        for line in f:
            line = line.strip()
            
            if not line:
                continue
            
            name , encrypted = line.split(" | ", 1)
            decrypted = cipher.decrypt(encrypted.encode()).decode()
            
            
            print(f"{name}: {decrypted}")




def interactive_generate():
    print("\n --- Generate New Password ---")
    
    length = int(input("Length: "))
    
    include_uppercase = input("Include Uppercase? (y/n): ").lower() == "y"
    include_digits = input("Include digits? (y/n): ").lower() == "y"
    include_symbols = input("Include symbols? (y/n): ").lower() == "y"
    
    
    password = generate_password(length, include_uppercase, include_digits, include_symbols)
    
    print(f"\nGenerated: {password}")
    
    score = check_strength(password)
    label = get_strength_label(score)
    print(f"Strength: {label} (Score: {score})")
    
    save = input("\nSave this password? (y/n): ").lower() =="y"
    
    if save:
        name = input("Name for this password: ").strip()
        save_password(name, password)
        print(f"✓ Saved as '{name}'")
        
    else:
        print("Not saved.")
        



def main_menu():
    print("=" * 40)
    print("       Password Tool v1.0")
    print("        by Judy Ahmad")
    print("=" * 40)
    
    while True:
        print("\n=== Password Tool ===")
        print("1. Check password strength")
        print("2. Generate new password")
        print("3. List saved passwords")
        print("4. Quit")
        
        choice = input("Choose (1-4): ").strip()
        
        if choice == "1":
            password = input("Enter password to check: ")
            score = check_strength(password)
            label = get_strength_label(score)
            print(f"Score: {score} | Strength: {label}")
        
        elif choice == "2":
            interactive_generate()
        
        elif choice == "3":
            list_passwords()
        
        elif choice == "4":
            print("Goodbye!")
            
            break      
        else:
            print("Invalid choice. Please enter 1-4.")
            
            
main_menu()