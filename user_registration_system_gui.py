import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# Modified Caesar Cipher with internal key
ENCRYPTION_KEY = 7  # Internal key for encryption

def modified_caesar_encrypt(text, key):
    """Encrypt text using modified Caesar cipher"""
    encrypted = ""
    for char in text:
        if char.isalpha():
            # Shift alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + key) % 26 + base)
        elif char.isdigit():
            # Shift digits
            encrypted += str((int(char) + key) % 10)
        else:
            # Shift special characters by ASCII value
            encrypted += chr((ord(char) + key) % 128)
    return encrypted

def modified_caesar_decrypt(text, key):
    """Decrypt text using modified Caesar cipher"""
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - key) % 26 + base)
        elif char.isdigit():
            decrypted += str((int(char) - key) % 10)
        else:
            decrypted += chr((ord(char) - key) % 128)
    return decrypted

def validate_password(password):
    """Validate password meets requirements"""
    if len(password) != 8:
        return False, "Password must be exactly 8 characters long"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one capital letter"
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special symbol"
    return True, "Valid"

class RegistrationLoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("User Registration System")
        self.root.geometry("400x300")
        
        # Initialize database
        self.init_database()
        
        # Show registration screen first
        self.show_registration_screen()
    
    def init_database(self):
        """Initialize SQLite database"""
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    
    def clear_screen(self):
        """Clear all widgets from screen"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_registration_screen(self):
        """Display registration screen"""
        self.clear_screen()
        self.root.title("Register")
        
        # Title
        tk.Label(self.root, text="Register", font=("Arial", 18, "bold")).pack(pady=20)
        
        # Username
        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack()
        self.username_entry = tk.Entry(self.root, width=30, font=("Arial", 11))
        self.username_entry.pack(pady=5)
        
        # Password
        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack()
        self.password_entry = tk.Entry(self.root, width=30, show="*", font=("Arial", 11))
        self.password_entry.pack(pady=5)
        
        # Password requirements
        req_text = "Password must be 8 characters with:\n1 digit, 1 capital letter, 1 special symbol"
        tk.Label(self.root, text=req_text, font=("Arial", 9), fg="gray").pack(pady=5)
        
        # Buttons frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Store", command=self.store_user, 
                 width=10, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Refresh", command=self.refresh_fields, 
                 width=10, bg="#2196F3", fg="white", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Login", command=self.show_login_screen, 
                 width=10, bg="#FF9800", fg="white", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
    
    def refresh_fields(self):
        """Clear all entry fields"""
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
    
    def store_user(self):
        """Store user registration in database"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username:
            messagebox.showerror("Error", "Username cannot be empty")
            return
        
        if not password:
            messagebox.showerror("Error", "Password cannot be empty")
            return
        
        # Validate password
        is_valid, message = validate_password(password)
        if not is_valid:
            messagebox.showerror("Invalid Password", message)
            return
        
        # Encrypt password
        encrypted_password = modified_caesar_encrypt(password, ENCRYPTION_KEY)
        
        # Store in database
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                          (username, encrypted_password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration successful!")
            self.refresh_fields()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed: {str(e)}")
    
    def show_login_screen(self):
        """Display login screen"""
        self.clear_screen()
        self.root.title("Login")
        
        # Title
        tk.Label(self.root, text="Login", font=("Arial", 18, "bold")).pack(pady=20)
        
        # Username
        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack()
        self.login_username_entry = tk.Entry(self.root, width=30, font=("Arial", 11))
        self.login_username_entry.pack(pady=5)
        
        # Password
        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack()
        self.login_password_entry = tk.Entry(self.root, width=30, show="*", font=("Arial", 11))
        self.login_password_entry.pack(pady=5)
        
        # Buttons frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="OK", command=self.check_login, 
                 width=10, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Back", command=self.show_registration_screen, 
                 width=10, bg="#f44336", fg="white", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
    
    def check_login(self):
        """Verify login credentials"""
        username = self.login_username_entry.get().strip()
        password = self.login_password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return
        
        # Encrypt entered password
        encrypted_password = modified_caesar_encrypt(password, ENCRYPTION_KEY)
        
        # Check in database
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            conn.close()
            
            if result and result[0] == encrypted_password:
                messagebox.showinfo("Success", "Login Successful!")
            else:
                messagebox.showerror("Failed", "Login Failed!\nInvalid username or password")
        except Exception as e:
            messagebox.showerror("Error", f"Login error: {str(e)}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationLoginSystem(root)
    root.mainloop()