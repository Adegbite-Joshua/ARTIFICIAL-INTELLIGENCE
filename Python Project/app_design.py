import tkinter as tk
from tkinter import ttk
from database import Database

database = Database()

class GTABankATM:
    def __init__(self):
        self.window_gui = tk.Tk()
        self.window_gui.geometry("350x550")
        self.window_gui.title("GTA Bank ATM")
        self.window_gui.config(bg="black")        
        
        # State variables
        self.current_screen = "main"
        self.error_after_id = None
        
        # Store input values
        self.signup_data = {}
        self.transfer_data = {}
        self.deposit_data = {}
        self.withdraw_data = {}
        self.airtime_data = {}
        self.bills_data = {}
        self.pin_data = {}
        
        # Main container
        self.main_frame = tk.Frame(self.window_gui, bg="black")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Error message frame (always at the top)
        self.error_frame = tk.Frame(self.main_frame, bg="black")
        self.error_frame.pack(fill="x", pady=(0, 10))
        
        self.error_label = tk.Label(self.error_frame, text="", 
                                  bg="red", fg="white", font=("Arial", 10),
                                  wraplength=300, justify="center")
        self.error_label.pack(fill="x", padx=5, pady=5)
        self.error_label.pack_forget()  # Hide initially
        
        # Content frame for all other widgets
        self.content_frame = tk.Frame(self.main_frame, bg="black")
        self.content_frame.pack(fill="both", expand=True)
        
        # Initial render
        self.render()

    def show_screen(self, screen_name, message=None, account_number=None):
        self.current_screen = screen_name
        self.clear_error()  # Clear error when changing screens
        self.render(account_number=account_number)

    def show_error(self, message, duration=5000):
        """Show error message and clear it after duration (ms)"""
        # Clear any pending error clear
        if self.error_after_id:
            self.window_gui.after_cancel(self.error_after_id)
        
        # Show error message
        self.error_label.config(text=message)
        self.error_label.pack(fill="x", padx=5, pady=5)
        
        # Schedule auto-clear
        self.error_after_id = self.window_gui.after(duration, self.clear_error)

    def clear_error(self):
        """Clear the error message"""
        self.error_label.pack_forget()
        self.error_label.config(text="")
        if self.error_after_id:
            self.window_gui.after_cancel(self.error_after_id)
            self.error_after_id = None

    def setup_input_validation(self, entry_widget):
        """Setup validation to clear error when user starts typing"""
        def clear_on_input(event):
            self.clear_error()
        
        entry_widget.bind('<KeyPress>', clear_on_input)

    def render(self, account_number=None):
        # Clear content frame only (keep error frame)
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Welcome message (always shown)
        message_label = tk.Label(self.content_frame, 
                               text="WELCOME TO GTA BANK ATM", 
                               justify="center", bg="black", foreground="green",
                               font=("Arial", 12, "bold"))
        message_label.pack(pady=10)
        
        # MAIN MENU
        if self.current_screen == "main":
            self.render_main_menu()
        # SIGN UP PAGE
        elif self.current_screen == "signup":
            self.render_signup()
        # SIGN UP SUCCESS
        elif self.current_screen == "signup_success":
            self.render_signup_success(account_number)
        # SIGN IN PAGE
        elif self.current_screen == "signin":
            self.render_signin()
        # BALANCE INQUIRY
        elif self.current_screen == "balance":
            self.render_balance()
        # TRANSFER PAGE
        elif self.current_screen == "transfer":
            self.render_transfer()
        # TRANSFER SUCCESS
        elif self.current_screen == "transfer_success":
            self.render_transfer_success()
        # DEPOSIT PAGE
        elif self.current_screen == "deposit":
            self.render_deposit()
        # DEPOSIT SUCCESS
        elif self.current_screen == "deposit_success":
            self.render_deposit_success()
        # WITHDRAWAL PAGE
        elif self.current_screen == "withdraw":
            self.render_withdraw()
        # WITHDRAWAL SUCCESS
        elif self.current_screen == "withdraw_success":
            self.render_withdraw_success()
        # AIRTIME & DATA PAGE
        elif self.current_screen == "airtime":
            self.render_airtime()
        # BILLS PAYMENT PAGE
        elif self.current_screen == "bills":
            self.render_bills()
        # PURCHASE SUCCESS
        elif self.current_screen == "purchase_success":
            self.render_purchase_success()
        # CHANGE PIN PAGE
        elif self.current_screen == "changepin":
            self.render_changepin()
        # PIN CHANGE SUCCESS
        elif self.current_screen == "pin_success":
            self.render_pin_success()

    def render_main_menu(self):
        actions_button_frame = tk.Frame(self.content_frame, bg="black")
        actions_button_frame.pack(fill="x", padx=10)
        
        actions_button_frame.columnconfigure(0, weight=1)
        actions_button_frame.columnconfigure(1, weight=1)
        
        button_style = {"bg": "gray", "fg": "white", "width": 15, "height": 2}
        
        tk.Button(actions_button_frame, text="BALANCE", 
                 command=lambda: self.show_screen("balance"), **button_style).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        tk.Button(actions_button_frame, text="DEPOSIT", 
                 command=lambda: self.show_screen("deposit"), **button_style).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        tk.Button(actions_button_frame, text="TRANSFER", 
                 command=lambda: self.show_screen("transfer"), **button_style).grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        
        tk.Button(actions_button_frame, text="WITHDRAW", 
                 command=lambda: self.show_screen("withdraw"), **button_style).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        tk.Button(actions_button_frame, text="AIRTIME & DATA", 
                 command=lambda: self.show_screen("airtime"), **button_style).grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        
        tk.Button(actions_button_frame, text="BILLS PAYMENT", 
                 command=lambda: self.show_screen("bills"), **button_style).grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        tk.Button(actions_button_frame, text="SIGN UP", 
                 command=lambda: self.show_screen("signup"), **button_style).grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        
        tk.Button(actions_button_frame, text="SIGN IN", 
                 command=lambda: self.show_screen("signin"), **button_style).grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        tk.Button(actions_button_frame, text="CHANGE PIN", 
                 command=lambda: self.show_screen("changepin"), **button_style).grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    def render_signup(self):
        form_frame = tk.Frame(self.content_frame, bg="black")
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="CREATE ACCOUNT", bg="black", fg="green", 
                font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Form fields
        fields = [
            ("First Name:", "first_name", "text"),
            ("Last Name:", "last_name", "text"), 
            ("Email:", "email", "text"),
            ("Password:", "password", "password"),
            ("PIN (4 digits):", "pin", "password")
        ]
        
        self.signup_entries = {}
        for i, (label, field_key, field_type) in enumerate(fields, 1):
            tk.Label(form_frame, text=label, bg="black", fg="white").grid(row=i, column=0, sticky="w", pady=5)
            if field_type == "password":
                entry = tk.Entry(form_frame, width=20, show="*")
            else:
                entry = tk.Entry(form_frame, width=20)
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.signup_entries[field_key] = entry
            self.setup_input_validation(entry)  # Add input validation
        
        tk.Button(form_frame, text="CREATE ACCOUNT", command=self.submit_signup,
                 bg="green", fg="white", width=15).grid(row=6, column=0, columnspan=2, pady=10)
        
        self.add_back_button()

    def submit_signup(self):
        # Get all input values
        signup_data = {
            "first_name": self.signup_entries["first_name"].get(),
            "last_name": self.signup_entries["last_name"].get(),
            "email": self.signup_entries["email"].get(),
            "password": self.signup_entries["password"].get(),
            "pin": self.signup_entries["pin"].get()
        }
        
        # Validate inputs
        if not all(signup_data.values()):
            self.show_error("Please fill in all fields")
            return
        
        if len(signup_data["pin"]) != 4 or not signup_data["pin"].isdigit():
            self.show_error("PIN must be 4 digits")
            return
        
        is_successful, message, account_number = database.create_account(
            signup_data["first_name"], 
            signup_data["last_name"], 
            signup_data["email"], 
            signup_data["password"], 
            signup_data["pin"]
        )
        
        if is_successful:
            self.signup_data = signup_data
            self.show_screen("signup_success", message=message, account_number=account_number)
        else:
            self.show_error(message)

    def render_signup_success(self, account_number: str):
        success_frame = tk.Frame(self.content_frame, bg="black")
        success_frame.pack(pady=50)
        
        tk.Label(success_frame, text="✓ ACCOUNT CREATED", bg="black", fg="green",
                font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(success_frame, text="Successfully!", bg="black", fg="white",
                font=("Arial", 12)).pack(pady=5)
        tk.Label(success_frame, text=f"Welcome {self.signup_data.get('first_name', '')} {self.signup_data.get('last_name', '')}", 
                bg="black", fg="yellow").pack(pady=5)
        tk.Label(success_frame, text=f"Account Number: {account_number}", bg="black", fg="yellow").pack(pady=5)
        
        tk.Button(success_frame, text="CONTINUE TO LOGIN", command=lambda: self.show_screen("signin"),
                 bg="green", fg="white", width=20).pack(pady=20)

    def render_signin(self):
        form_frame = tk.Frame(self.content_frame, bg="black")
        form_frame.pack(pady=20)
        
        tk.Label(form_frame, text="SIGN IN", bg="black", fg="green", 
                font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(form_frame, text="Account Number:", bg="black", fg="white").pack()
        self.account_entry = tk.Entry(form_frame, width=20)
        self.account_entry.pack(pady=5)
        self.setup_input_validation(self.account_entry)
        
        tk.Label(form_frame, text="PIN:", bg="black", fg="white").pack()
        self.pin_entry = tk.Entry(form_frame, width=20, show="*")
        self.pin_entry.pack(pady=5)
        self.setup_input_validation(self.pin_entry)
        
        tk.Button(form_frame, text="SIGN IN", command=self.submit_login,
                 bg="blue", fg="white", width=15).pack(pady=10)
        
        self.add_back_button()

    def submit_login(self):
        # Get login data
        login_data = {
            "account_number": self.account_entry.get(),
            "pin": self.pin_entry.get()
        }
        
        # Validate inputs
        if not login_data["account_number"]:
            self.show_error("Please enter account number")
            return
        
        if not login_data["pin"]:
            self.show_error("Please enter PIN")
            return
        
        is_successful, message, user_details = database.login(login_data["account_number"], login_data["pin"])
        if is_successful:
            self.user_details = user_details
            self.show_screen("main")
        else:
            self.show_error(message)

    def render_balance(self):
        balance_frame = tk.Frame(self.content_frame, bg="black")
        balance_frame.pack(pady=30)
        
        tk.Label(balance_frame, text="ACCOUNT BALANCE", bg="black", fg="green",
                font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(balance_frame, text="Available Balance:", bg="black", fg="white").pack()
        tk.Label(balance_frame, text=f"£{self.user_details['balance']:2d}", bg="black", fg="yellow",
                font=("Arial", 18, "bold")).pack(pady=10)
        
        tk.Label(balance_frame, text=f"Account: {self.user_details['account_number']}", bg="black", fg="white").pack()
        tk.Label(balance_frame, text=f"{self.user_details['first_name']} {self.user_details['last_name']}", bg="black", fg="white").pack()
        
        self.add_back_button()

    def render_transfer(self):
        form_frame = tk.Frame(self.content_frame, bg="black")
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="MONEY TRANSFER", bg="black", fg="green",
                font=("Arial", 14, "bold")).pack(pady=10)
        
        # Bank selection
        tk.Label(form_frame, text="Select Bank:", bg="black", fg="white").pack()
        banks = ["GTA Bank", "First Bank", "Zenith Bank", "Access Bank", "GT Bank", "UBA"]
        self.bank_var = tk.StringVar(value=banks[0])
        bank_combo = ttk.Combobox(form_frame, textvariable=self.bank_var, values=banks, width=18)
        bank_combo.pack(pady=5)
        
        # Account number
        tk.Label(form_frame, text="Account Number:", bg="black", fg="white").pack()
        self.acc_entry = tk.Entry(form_frame, width=20)
        self.acc_entry.pack(pady=5)
        self.setup_input_validation(self.acc_entry)
        
        # Display account name (dummy)
        self.acc_name_label = tk.Label(form_frame, text="Account Name: -", bg="black", fg="yellow")
        self.acc_name_label.pack()
        
        # Amount
        tk.Label(form_frame, text="Amount:", bg="black", fg="white").pack()
        self.amount_entry = tk.Entry(form_frame, width=20)
        self.amount_entry.pack(pady=5)
        self.setup_input_validation(self.amount_entry)
        
        tk.Button(form_frame, text="VERIFY ACCOUNT", command=self.verify_account,
                 bg="orange", fg="white").pack(pady=5)
        
        tk.Button(form_frame, text="TRANSFER", command=self.process_transfer,
                 bg="green", fg="white", width=15).pack(pady=10)
        
        self.add_back_button()

    def verify_account(self):
        # Simulate account verification
        account_number = self.acc_entry.get()
        if not account_number:
            self.show_error("Please enter account number")
            return
            
        if account_number:
            self.acc_name_label.config(text=f"Account Name: Jane Smith")
            print(f"Verified account: {account_number}")

    def process_transfer(self):
        # Get transfer data
        transfer_data = {
            "bank": self.bank_var.get(),
            "account_number": self.acc_entry.get(),
            "amount": self.amount_entry.get()
        }
        
        # Validate inputs
        if not transfer_data["account_number"]:
            self.show_error("Please enter account number")
            return
            
        if not transfer_data["amount"] or not transfer_data["amount"].isdigit():
            self.show_error("Please enter a valid amount")
            return
        
        self.transfer_data = transfer_data
        
        print("=== TRANSFER DATA ===")
        for key, value in self.transfer_data.items():
            print(f"{key}: {value}")
        print("=====================")
        
        self.show_screen("transfer_success")

    def render_transfer_success(self):
        success_frame = tk.Frame(self.content_frame, bg="black")
        success_frame.pack(pady=50)
        
        tk.Label(success_frame, text="✓ TRANSFER SUCCESSFUL", bg="black", fg="green",
                font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(success_frame, text=f"Amount: ${self.transfer_data.get('amount', '0')}.00", 
                bg="black", fg="white").pack()
        tk.Label(success_frame, text=f"To: Jane Smith ({self.transfer_data.get('account_number', '')})", 
                bg="black", fg="white").pack()
        tk.Label(success_frame, text=f"Bank: {self.transfer_data.get('bank', '')}", 
                bg="black", fg="white").pack()
        tk.Label(success_frame, text="New Balance: $1,950.00", bg="black", fg="yellow").pack(pady=10)
        
        tk.Button(success_frame, text="OK", command=lambda: self.show_screen("main"),
                 bg="green", fg="white", width=15).pack(pady=20)

    def render_deposit(self):
        form_frame = tk.Frame(self.content_frame, bg="black")
        form_frame.pack(pady=20)
        
        tk.Label(form_frame, text="CASH DEPOSIT", bg="black", fg="green",
                font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(form_frame, text="Amount to Deposit:", bg="black", fg="white").pack()
        self.deposit_amount_entry = tk.Entry(form_frame, width=20)
        self.deposit_amount_entry.pack(pady=10)
        self.setup_input_validation(self.deposit_amount_entry)
        
        tk.Button(form_frame, text="DEPOSIT", command=self.process_deposit,
                 bg="green", fg="white", width=15).pack(pady=10)
        
        self.add_back_button()

    def process_deposit(self):
        # Get deposit data
        amount = self.deposit_amount_entry.get()
        
        if not amount or not amount.replace('.', '').isdigit():
            self.show_error("Please enter a valid amount")
            return
            
        self.deposit_data = {"amount": amount}
        
        print("=== DEPOSIT DATA ===")
        print(f"Amount: ${self.deposit_data['amount']}")
        print("====================")
        
        self.show_screen("deposit_success")

    def render_deposit_success(self):
        success_frame = tk.Frame(self.content_frame, bg="black")
        success_frame.pack(pady=50)
        
        tk.Label(success_frame, text="✓ DEPOSIT SUCCESSFUL", bg="black", fg="green",
                font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(success_frame, text=f"Amount: ${self.deposit_data.get('amount', '0')}.00", 
                bg="black", fg="white").pack()
        tk.Label(success_frame, text="New Balance: $2,750.00", bg="black", fg="yellow").pack(pady=10)
        
        tk.Button(success_frame, text="OK", command=lambda: self.show_screen("main"),
                 bg="green", fg="white", width=15).pack(pady=20)

    def render_withdraw(self):
        form_frame = tk.Frame(self.content_frame, bg="black")
        form_frame.pack(pady=20)
        
        tk.Label(form_frame, text="CASH WITHDRAWAL", bg="black", fg="green",
                font=("Arial", 14, "bold")).pack(pady=10)
        
        # Quick amount buttons
        amounts = ["$20", "$40", "$100", "$200", "$500"]
        amount_frame = tk.Frame(form_frame, bg="black")
        amount_frame.pack(pady=10)
        
        for i, amount in enumerate(amounts):
            tk.Button(amount_frame, text=amount, command=lambda a=amount: self.withdraw_amount(a),
                     bg="blue", fg="white", width=8).grid(row=i//3, column=i%3, padx=2, pady=2)
        
        tk.Label(form_frame, text="Or Enter Custom Amount:", bg="black", fg="white").pack(pady=10)
        self.custom_entry = tk.Entry(form_frame, width=20)
        self.custom_entry.pack(pady=5)
        self.setup_input_validation(self.custom_entry)
        
        tk.Button(form_frame, text="WITHDRAW", command=lambda: self.withdraw_amount(self.custom_entry.get()),
                 bg="green", fg="white", width=15).pack(pady=10)
        
        self.add_back_button()

    def withdraw_amount(self, amount):
        if not amount:
            self.show_error("Please enter an amount")
            return
            
        # Get withdraw data
        clean_amount = amount.replace('$', '') if amount.startswith('$') else amount
        if not clean_amount.replace('.', '').isdigit():
            self.show_error("Please enter a valid amount")
            return
            
        self.withdraw_data = {"amount": clean_amount}
        
        print("=== WITHDRAW DATA ===")
        print(f"Amount: ${self.withdraw_data['amount']}")
        print("=====================")
        
        self.show_screen("withdraw_success")

    def render_withdraw_success(self):
        success_frame = tk.Frame(self.content_frame, bg="black")
        success_frame.pack(pady=50)
        
        tk.Label(success_frame, text="✓ WITHDRAWAL SUCCESSFUL", bg="black", fg="green",
                font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(success_frame, text="Please take your cash", bg="black", fg="white").pack()
        tk.Label(success_frame, text=f"Amount: ${self.withdraw_data.get('amount', '0')}.00", 
                bg="black", fg="white").pack()
        tk.Label(success_frame, text="New Balance: $2,350.00", bg="black", fg="yellow").pack(pady=10)
        
        tk.Button(success_frame, text="OK", command=lambda: self.show_screen("main"),
                 bg="green", fg="white", width=15).pack(pady=20)

    def render_airtime(self):
        form_frame = tk.Frame(self.content_frame, bg="black")
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="AIRTIME & DATA", bg="black", fg="green",
                font=("Arial", 14, "bold")).pack(pady=10)
        
        # Network selection
        tk.Label(form_frame, text="Select Network:", bg="black", fg="white").pack()
        networks = ["MTN", "Airtel", "Glo", "9mobile"]
        self.network_var = tk.StringVar(value=networks[0])
        network_combo = ttk.Combobox(form_frame, textvariable=self.network_var, values=networks, width=18)
        network_combo.pack(pady=5)
        
        # Phone number
        tk.Label(form_frame, text="Phone Number:", bg="black", fg="white").pack()
        self.phone_entry = tk.Entry(form_frame, width=20)
        self.phone_entry.pack(pady=5)
        self.setup_input_validation(self.phone_entry)
        
        # Type selection
        tk.Label(form_frame, text="Select Type:", bg="black", fg="white").pack()
        self.type_var = tk.StringVar(value="Airtime")
        tk.Radiobutton(form_frame, text="Airtime", variable=self.type_var, value="Airtime", 
                      bg="black", fg="white", selectcolor="black").pack()
        tk.Radiobutton(form_frame, text="Data", variable=self.type_var, value="Data",
                      bg="black", fg="white", selectcolor="black").pack()
        
        # Amount
        tk.Label(form_frame, text="Amount:", bg="black", fg="white").pack()
        self.airtime_amount_entry = tk.Entry(form_frame, width=20)
        self.airtime_amount_entry.pack(pady=5)
        self.setup_input_validation(self.airtime_amount_entry)
        
        tk.Button(form_frame, text="BUY", command=self.process_airtime,
                 bg="green", fg="white", width=15).pack(pady=10)
        
        self.add_back_button()

    def process_airtime(self):
        # Get airtime data
        airtime_data = {
            "network": self.network_var.get(),
            "phone_number": self.phone_entry.get(),
            "type": self.type_var.get(),
            "amount": self.airtime_amount_entry.get()
        }
        
        # Validate inputs
        if not airtime_data["phone_number"]:
            self.show_error("Please enter phone number")
            return
            
        if not airtime_data["amount"] or not airtime_data["amount"].replace('.', '').isdigit():
            self.show_error("Please enter a valid amount")
            return
        
        self.airtime_data = airtime_data
        
        print("=== AIRTIME/DATA DATA ===")
        for key, value in self.airtime_data.items():
            print(f"{key}: {value}")
        print("========================")
        
        self.show_screen("purchase_success")

    def is_user_authenticated(self):
        if not self.user_details:         
            self.show_error("Please sign in to proceed")
            self.render_signin()
        
    def render_bills(self):
        form_frame = tk.Frame(self.content_frame, bg="black")
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="BILLS PAYMENT", bg="black", fg="green",
                font=("Arial", 14, "bold")).pack(pady=10)
        
        # Bill type selection
        tk.Label(form_frame, text="Select Bill Type:", bg="black", fg="white").pack()
        bills = ["Electricity", "Water", "Internet", "Cable TV", "Tax"]
        self.bill_var = tk.StringVar(value=bills[0])
        bill_combo = ttk.Combobox(form_frame, textvariable=self.bill_var, values=bills, width=18)
        bill_combo.pack(pady=5)
        
        # Account number
        tk.Label(form_frame, text="Account Number:", bg="black", fg="white").pack()
        self.bill_account_entry = tk.Entry(form_frame, width=20)
        self.bill_account_entry.pack(pady=5)
        self.setup_input_validation(self.bill_account_entry)
        
        # Amount
        tk.Label(form_frame, text="Amount:", bg="black", fg="white").pack()
        self.bill_amount_entry = tk.Entry(form_frame, width=20)
        self.bill_amount_entry.pack(pady=5)
        self.setup_input_validation(self.bill_amount_entry)
        
        tk.Button(form_frame, text="PAY BILL", command=self.process_bill,
                 bg="green", fg="white", width=15).pack(pady=10)
        
        self.add_back_button()

    def process_bill(self):
        # Get bill data
        bill_data = {
            "bill_type": self.bill_var.get(),
            "account_number": self.bill_account_entry.get(),
            "amount": self.bill_amount_entry.get()
        }
        
        # Validate inputs
        if not bill_data["account_number"]:
            self.show_error("Please enter account number")
            return
            
        if not bill_data["amount"] or not bill_data["amount"].replace('.', '').isdigit():
            self.show_error("Please enter a valid amount")
            return
        
        self.bills_data = bill_data
        
        print("=== BILL PAYMENT DATA ===")
        for key, value in self.bills_data.items():
            print(f"{key}: {value}")
        print("========================")
        
        self.show_screen("purchase_success")

    def render_purchase_success(self):
        success_frame = tk.Frame(self.content_frame, bg="black")
        success_frame.pack(pady=50)
        
        tk.Label(success_frame, text="✓ TRANSACTION SUCCESSFUL", bg="black", fg="green",
                font=("Arial", 16, "bold")).pack(pady=10)
        
        # Show relevant data based on previous screen
        if hasattr(self, 'airtime_data') and self.airtime_data:
            tk.Label(success_frame, text=f"{self.airtime_data['type']} purchase for {self.airtime_data['phone_number']}", 
                    bg="black", fg="white").pack()
            tk.Label(success_frame, text=f"Amount: ${self.airtime_data['amount']}", 
                    bg="black", fg="white").pack()
        elif hasattr(self, 'bills_data') and self.bills_data:
            tk.Label(success_frame, text=f"{self.bills_data['bill_type']} bill paid", 
                    bg="black", fg="white").pack()
            tk.Label(success_frame, text=f"Amount: ${self.bills_data['amount']}", 
                    bg="black", fg="white").pack()
        
        tk.Label(success_frame, text="Thank you for using GTA Bank", bg="black", fg="yellow").pack(pady=10)
        
        tk.Button(success_frame, text="OK", command=lambda: self.show_screen("main"),
                 bg="green", fg="white", width=15).pack(pady=20)

    def render_changepin(self):
        form_frame = tk.Frame(self.content_frame, bg="black")
        form_frame.pack(pady=20)
        
        tk.Label(form_frame, text="CHANGE PIN", bg="black", fg="green",
                font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(form_frame, text="Current PIN:", bg="black", fg="white").pack()
        self.current_pin_entry = tk.Entry(form_frame, width=20, show="*")
        self.current_pin_entry.pack(pady=5)
        self.setup_input_validation(self.current_pin_entry)
        
        tk.Label(form_frame, text="New PIN (4 digits):", bg="black", fg="white").pack()
        self.new_pin_entry = tk.Entry(form_frame, width=20, show="*")
        self.new_pin_entry.pack(pady=5)
        self.setup_input_validation(self.new_pin_entry)
        
        tk.Label(form_frame, text="Confirm New PIN:", bg="black", fg="white").pack()
        self.confirm_pin_entry = tk.Entry(form_frame, width=20, show="*")
        self.confirm_pin_entry.pack(pady=5)
        self.setup_input_validation(self.confirm_pin_entry)
        
        tk.Button(form_frame, text="CHANGE PIN", command=self.process_pin_change,
                 bg="green", fg="white", width=15).pack(pady=10)
        
        self.add_back_button()

    def process_pin_change(self):
        # Get PIN change data
        pin_data = {
            "current_pin": self.current_pin_entry.get(),
            "new_pin": self.new_pin_entry.get(),
            "confirm_pin": self.confirm_pin_entry.get()
        }
        
        # Validate inputs
        if not all(pin_data.values()):
            self.show_error("Please fill in all fields")
            return
            
        if len(pin_data["new_pin"]) != 4 or not pin_data["new_pin"].isdigit():
            self.show_error("New PIN must be 4 digits")
            return
            
        if pin_data["new_pin"] != pin_data["confirm_pin"]:
            self.show_error("New PIN and confirmation do not match")
            return
        
        self.pin_data = pin_data
        
        print("=== PIN CHANGE DATA ===")
        print(f"Current PIN: {self.pin_data['current_pin']}")
        print(f"New PIN: {self.pin_data['new_pin']}")
        print(f"Confirm PIN: {self.pin_data['confirm_pin']}")
        print("======================")
        
        self.show_screen("pin_success")

    def render_pin_success(self):
        success_frame = tk.Frame(self.content_frame, bg="black")
        success_frame.pack(pady=50)
        
        tk.Label(success_frame, text="✓ PIN CHANGED", bg="black", fg="green",
                font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(success_frame, text="Your PIN has been updated successfully", bg="black", fg="white").pack()
        
        tk.Button(success_frame, text="OK", command=lambda: self.show_screen("main"),
                 bg="green", fg="white", width=15).pack(pady=20)

    def add_back_button(self):
        tk.Button(self.content_frame, text="← BACK", command=lambda: self.show_screen("main"), 
                 bg="darkgray", fg="white").pack(pady=10)

    def run(self):
        self.window_gui.mainloop()