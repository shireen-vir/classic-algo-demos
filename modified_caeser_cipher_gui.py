import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import string

class ModifiedCaesarDecryptorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Modified Caesar Cipher Decryptor")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Modified Caesar Cipher Decryptor", 
                                font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Encrypted Text Input
        ttk.Label(main_frame, text="Encrypted Text:", font=('Arial', 10, 'bold')).grid(
            row=1, column=0, sticky=tk.W, pady=(0, 5))
        
        self.encrypted_text = scrolledtext.ScrolledText(main_frame, width=70, height=10, 
                                                        wrap=tk.WORD, font=('Courier', 10))
        self.encrypted_text.grid(row=2, column=0, columnspan=2, pady=(0, 15))
        
        # Decrypted Text Output
        ttk.Label(main_frame, text="Decrypted Text:", font=('Arial', 10, 'bold')).grid(
            row=3, column=0, sticky=tk.W, pady=(0, 5))
        
        self.decrypted_text = scrolledtext.ScrolledText(main_frame, width=70, height=10, 
                                                        wrap=tk.WORD, font=('Courier', 10),
                                                        state=tk.DISABLED, bg='#f0f0f0')
        self.decrypted_text.grid(row=4, column=0, columnspan=2, pady=(0, 15))
        
        # Button Frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Decrypt Button
        self.decrypt_btn = ttk.Button(button_frame, text="Decrypt", 
                                      command=self.show_key_dialog, width=15)
        self.decrypt_btn.grid(row=0, column=0, padx=5)
        
        # Clear Button
        self.clear_btn = ttk.Button(button_frame, text="Clear All", 
                                    command=self.clear_all, width=15)
        self.clear_btn.grid(row=0, column=1, padx=5)
        
        # Info label
        info_label = ttk.Label(main_frame, 
                              text="Modified Caesar Cipher shifts each character by (key × position) % 26",
                              font=('Arial', 8), foreground='gray')
        info_label.grid(row=6, column=0, columnspan=2, pady=(10, 0))
        
    def show_key_dialog(self):
        # Validate encrypted text
        encrypted = self.encrypted_text.get("1.0", tk.END).strip()
        if not encrypted:
            messagebox.showerror("Validation Error", "Please enter the encrypted text!")
            return
        
        # Create key input dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Enter Decryption Key")
        dialog.geometry("300x150")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        # Key input frame
        frame = ttk.Frame(dialog, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Enter Decryption Key:", font=('Arial', 10, 'bold')).pack(pady=(0, 10))
        
        key_var = tk.StringVar()
        key_entry = ttk.Entry(frame, textvariable=key_var, width=20, font=('Arial', 12))
        key_entry.pack(pady=(0, 15))
        key_entry.focus()
        
        def validate_and_decrypt():
            key_str = key_var.get().strip()
            
            # Validation: Check if key is empty
            if not key_str:
                messagebox.showerror("Validation Error", "Key cannot be empty!", parent=dialog)
                return
            
            # Validation: Check if key is a valid integer
            try:
                key = int(key_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Key must be a valid integer!", parent=dialog)
                return
            
            # Validation: Check if key is in reasonable range
            if key < 1 or key > 25:
                messagebox.showwarning("Warning", "Key should be between 1 and 25 for best results.", parent=dialog)
            
            # Perform decryption
            self.decrypt_text(encrypted, key)
            dialog.destroy()
        
        # Button frame
        btn_frame = ttk.Frame(frame)
        btn_frame.pack()
        
        ttk.Button(btn_frame, text="Decrypt", command=validate_and_decrypt, width=12).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=dialog.destroy, width=12).pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to decrypt
        key_entry.bind('<Return>', lambda e: validate_and_decrypt())
        
    def decrypt_text(self, encrypted, key):
        """
        Modified Caesar Cipher Decryption:
        Each character is shifted by (key × position) % 26
        """
        decrypted = []
        
        for pos, char in enumerate(encrypted):
            if char.isalpha():
                # Determine if uppercase or lowercase
                is_upper = char.isupper()
                char = char.upper()
                
                # Calculate shift for this position (1-indexed)
                shift = (key * (pos + 1)) % 26
                
                # Decrypt by shifting backwards
                char_index = ord(char) - ord('A')
                decrypted_index = (char_index - shift) % 26
                decrypted_char = chr(decrypted_index + ord('A'))
                
                # Restore original case
                if not is_upper:
                    decrypted_char = decrypted_char.lower()
                
                decrypted.append(decrypted_char)
            else:
                # Keep non-alphabetic characters as-is
                decrypted.append(char)
        
        result = ''.join(decrypted)
        
        # Display result
        self.decrypted_text.config(state=tk.NORMAL)
        self.decrypted_text.delete("1.0", tk.END)
        self.decrypted_text.insert("1.0", result)
        self.decrypted_text.config(state=tk.DISABLED)
        
        messagebox.showinfo("Success", "Text decrypted successfully!")
    
    def clear_all(self):
        self.encrypted_text.delete("1.0", tk.END)
        self.decrypted_text.config(state=tk.NORMAL)
        self.decrypted_text.delete("1.0", tk.END)
        self.decrypted_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = ModifiedCaesarDecryptorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()