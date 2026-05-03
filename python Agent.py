product_name = input("Please enter the product name: ")
service_type = input("Please enter the type of service (e.g., Content Writing, Video Editing): ")
print(f"Thank you! Your order for '{product_name}' ({service_type}) has been received.")
# New logic for Video Editing
if "Video" in service_type or "video" in service_type:
    video_style = input("What style of video do you need? (e.g., TikTok, Product Branding, YouTube): ")
    print(f"Perfect! We have received your order for {video_style} editing for '{product_name}'.")
else:
    # This covers Content Writing or any other service
    print(f"Thank you! Your order for {service_type} regarding '{product_name}' has been received.")

print("Program finished.")
# --- AI Agent Order Management System ---

# Step 1: Get basic info
product_name = input("Please enter the product name: ")
service_type = input("What service do you need? (e.g., Content Writing, Video Editing, Graphic Design): ")

# Step 2: Logic for different services
if "Video" in service_type or "video" in service_type:
    # Video Editing Section
    video_style = input("What style of video do you need? (e.g., TikTok, YouTube, Reels): ")
    print(f"\n--- Order Summary ---")
    print(f"Product: {product_name}")
    print(f"Service: Video Editing ({video_style})")
    print(f"Status: Recording and Editing process started!")

elif "Graphic" in service_type or "Design" in service_type:
    # Graphic Designing Section
    design_type = input("What do you need? (e.g., Logo, Poster, Thumbnail): ")
    print(f"\n--- Order Summary ---")
    print(f"Product: {product_name}")
    print(f"Service: Graphic Design ({design_type})")
    print(f"Status: Design team is notified!")

elif "Content" in service_type or "writing" in service_type.lower():
    # Content Writing Section
    print(f"\n--- Order Summary ---")
    print(f"Product: {product_name}")
    print(f"Service: Content Writing")
    print(f"Status: Writers are working on your content.")

else:
    # Any other service
    print(f"\nThank you! Your order for {service_type} regarding '{product_name}' has been received.")

# Step 3: End of Program
print("\n--- Program Finished ---")
# --- AI Agent: Professional Business Assistant ---

product_name = input("Enter Product Name: ")
service_type = input("Service (Video / Design / Content): ").lower()

# Pricing Logic
price = 0
delivery_days = ""

if "video" in service_type:
    style = input("Style (TikTok/YouTube): ")
    price = 50  # فرض کریں 50 ڈالر
    delivery_days = "3 Days"
    print(f"\nOrder: {style} Video for {product_name}")

elif "design" in service_type:
    style = input("Type (Logo/Poster): ")
    price = 30
    delivery_days = "2 Days"
    print(f"\nOrder: {style} Design for {product_name}")

elif "content" in service_type:
    price = 20
    delivery_days = "1 Day"
    print(f"\nOrder: Content Writing for {product_name}")

else:
    print("Service not recognized.")

# Final Bill Summary
if price > 0:
    print(f"--- Invoice ---")
    print(f"Total Cost: ${price}")
    print(f"Estimated Delivery: {delivery_days}")
    print(f"Thank you for choosing our AI Service!")

print("\n--- Program Finished ---")
import random # Order ID جنریٹ کرنے کے لیے

# --- AI Agent: Order Management System ---

print("Welcome to AI Service Center!")
customer_email = input("Please enter your email: ")
product_name = input("Enter Product Name: ")
service_type = input("Service (Video / Design / Content): ").lower()

# Pricing and Details
price = 0
delivery_time = ""
order_id = random.randint(1000, 9999) # 1000 سے 9999 کے درمیان کوئی بھی نمبر

if "video" in service_type:
    style = input("Style (TikTok/YouTube/Reels): ")
    price = 50
    delivery_time = "3 Business Days"
    service_info = f"Video Editing ({style})"

elif "design" in service_type:
    style = input("Type (Logo/Poster/Thumbnail): ")
    price = 30
    delivery_time = "2 Business Days"
    service_info = f"Graphic Design ({style})"

elif "content" in service_type:
    price = 20
    delivery_time = "24 Hours"
    service_info = "Content Writing"

else:
    service_info = "Unknown Service"

# Final Output (Receipt)
if price > 0:
    print("\n" + "="*30)
    print(f"       ORDER CONFIRMED      ")
    print("="*30)
    print(f"Order ID:      #{order_id}")
    print(f"Customer:      {customer_email}")
    print(f"Product:       {product_name}")
    print(f"Service:       {service_info}")
    print(f"Total Bill:    ${price}")
    print(f"Delivery:      {delivery_time}")
    print("="*30)
    print(f"A confirmation email has been sent to {customer_email}")
else:
    print("\nSorry, we don't provide that service yet.")

print("\n--- Program Finished ---")
import random

# --- AI Agent: Professional Order System with Database ---

print("--- Welcome to Your Business AI Agent ---")

# Step 1: Collecting User Info
customer_email = input("Please enter your email: ")
product_name = input("Enter Product Name: ")
service_type = input("Service (Video / Design / Content): ").lower()

# Step 2: Pricing and Order Logic
price = 0
delivery_time = ""
order_id = random.randint(1000, 9999)

if "video" in service_type:
    style = input("Style (TikTok/YouTube): ")
    price = 50
    delivery_time = "3 Days"
    service_detail = f"Video Editing ({style})"
elif "design" in service_type:
    style = input("Type (Logo/Poster): ")
    price = 30
    delivery_time = "2 Days"
    service_detail = f"Graphic Design ({style})"
elif "content" in service_type:
    price = 20
    delivery_time = "1 Day"
    service_detail = "Content Writing"
else:
    price = 0

# Step 3: Saving Order to a File (The "Database")
if price > 0:
    # 'a' stands for 'append' - it adds new data without deleting old data
    with open("orders.txt", "a") as file:
        file.write(f"Order ID: {order_id} | Email: {customer_email} | Product: {product_name} | Service: {service_detail} | Bill: ${price}\n")
    
    # Printing Receipt for Customer
    print("\n" + "="*40)
    print(f"       ORDER SUCCESSFUL!      ")
    print("="*40)
    print(f"Order ID:    #{order_id}")
    print(f"Service:     {service_detail}")
    print(f"Total Bill:  ${price}")
    print(f"Delivery:    {delivery_time}")
    print("="*40)
    print(f"Order details saved to 'orders.txt'.")
else:
    print("\nInvalid service. Please try again.")

print("\n--- Program Finished ---")
import random

# --- AI Agent: Professional Multi-Order System ---

def start_agent():
    print("--- Business AI Agent is now ONLINE ---")
    
    while True: # یہ لوپ پروگرام کو چلتا رکھے گا
        print("\n[New Order Entry]")
        customer_email = input("Customer Email (or type 'exit' to close): ")
        
        if customer_email.lower() == 'exit':
            print("Shutting down the agent. Goodbye!")
            break # پروگرام یہاں بند ہوگا
            
        product_name = input("Enter Product Name: ")
        service_type = input("Service (Video / Design / Content): ").lower()

        # Pricing and Logic
        price = 0
        if "video" in service_type:
            price, delivery, detail = 50, "3 Days", "Video Editing"
        elif "design" in service_type:
            price, delivery, detail = 30, "2 Days", "Graphic Design"
        elif "content" in service_type:
            price, delivery, detail = 20, "1 Day", "Content Writing"
        else:
            print("❌ Invalid service! Please try again.")
            continue # غلط انٹری پر دوبارہ شروع کرے گا

        order_id = random.randint(1000, 9999)

        # File Handling (Saving the data)
        try:
            with open("orders.txt", "a") as file:
                file.write(f"ID: {order_id} | Email: {customer_email} | Product: {product_name} | Service: {detail} | Price: ${price}\n")
            
            print(f"\n✅ SUCCESS: Order #{order_id} saved for {customer_email}")
            print(f"Total: ${price} | Delivery: {delivery}")
        except Exception as e:
            print(f"An error occurred while saving: {e}")

# پروگرام شروع کرنے کے لیے فنکشن کال کریں
start_agent()
import random

def start_agent():
    print("--- 🚀 Advanced Business AI Agent ---")
    
    while True:
        print("\n[MAIN MENU]")
        print("1. Create New Order")
        print("2. View All Orders")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            # --- آرڈر بنانے کا حصہ ---
            email = input("Customer Email: ")
            product = input("Product Name: ")
            service = input("Service (Video/Design/Content): ").lower()
            
            # Simple Pricing
            rates = {"video": 50, "design": 30, "content": 20}
            if service in rates:
                price = rates[service]
                order_id = random.randint(1000, 9999)
                
                # فائل میں سیو کرنا
                with open("orders.txt", "a") as file:
                    file.write(f"ID:{order_id} | Email:{email} | Product:{product} | Price:${price}\n")
                
                print(f"✅ Order #{order_id} saved successfully!")
            else:
                print("❌ Invalid Service!")

        elif choice == '2':
            # --- آرڈرز دیکھنے کا حصہ ---
            print("\n--- 📜 ALL SAVED ORDERS ---")
            try:
                with open("orders.txt", "r") as file:
                    orders = file.readlines()
                    if not orders:
                        print("No orders found.")
                    for line in orders:
                        print(line.strip())
            except FileNotFoundError:
                print("No database file found yet.")

        elif choice == '3':
            print("Shutting down... Goodbye!")
            break
        else:
            print("Invalid Choice!")

# پروگرام شروع کریں
start_agent()
import random

def start_agent():
    print("--- 🚀 Pro Business AI Management System ---")
    
    while True:
        print("\n--- MENU ---")
        print("1. New Order Entry")
        print("2. View All Orders")
        print("3. Search Order by ID")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            # Create Order
            email = input("Email: ")
            product = input("Product: ")
            service = input("Service (Video/Design/Content): ").lower()
            rates = {"video": 50, "design": 30, "content": 20}
            
            if service in rates:
                order_id = str(random.randint(1000, 9999))
                data = f"ID:{order_id} | Email:{email} | Product:{product} | Price:${rates[service]}"
                with open("orders.txt", "a") as file:
                    file.write(data + "\n")
                print(f"✅ Order #{order_id} Created!")
            else:
                print("❌ Invalid Service")

        elif choice == '2':
            # View All
            print("\n--- ALL ORDERS ---")
            try:
                with open("orders.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("No records found.")

        elif choice == '3':
            # Search Feature
            search_id = input("Enter Order ID to search: ")
            found = False
            try:
                with open("orders.txt", "r") as file:
                    for line in file:
                        if f"ID:{search_id}" in line:
                            print("\n🔍 Order Found:")
                            print(line.strip())
                            found = True
                            break
                if not found:
                    print("❌ Order ID not found.")
            except FileNotFoundError:
                print("No records found.")

        elif choice == '4':
            print("System Closing...")
            break

# Run System
start_agent()
import random

def start_agent():
    print("--- 🚀 Elite Business AI & Finance System ---")
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. New Order Entry")
        print("2. View All Orders")
        print("3. Search Order by ID")
        print("4. Calculate Total Earnings")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            # --- آرڈر بنانے کا حصہ ---
            email = input("Customer Email: ")
            product = input("Product Name: ")
            service = input("Service (Video/Design/Content): ").lower()
            rates = {"video": 50, "design": 30, "content": 20}
            
            if service in rates:
                order_id = str(random.randint(1000, 9999))
                price = rates[service]
                data = f"ID:{order_id} | Email:{email} | Product:{product} | Price:${price}"
                with open("orders.txt", "a") as file:
                    file.write(data + "\n")
                print(f"✅ Order #{order_id} Saved! (Bill: ${price})")
            else:
                print("❌ Invalid Service!")

        elif choice == '2':
            # --- تمام آرڈرز دیکھنا ---
            print("\n--- ALL ORDERS ---")
            try:
                with open("orders.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("No records yet.")

        elif choice == '3':
            # --- آرڈر سرچ کرنا ---
            search_id = input("Enter Order ID: ")
            found = False
            try:
                with open("orders.txt", "r") as file:
                    for line in file:
                        if f"ID:{search_id}" in line:
                            print(f"\n🔍 Result: {line.strip()}")
                            found = True
                            break
                if not found: print("❌ Not Found.")
            except FileNotFoundError:
                print("No records yet.")

        elif choice == '4':
            # --- کمائی کا حساب لگانا ---
            print("\n--- 💰 FINANCIAL REPORT ---")
            total = 0
            try:
                with open("orders.txt", "r") as file:
                    for line in file:
                        if "Price:$" in line:
                            # لائن میں سے قیمت نکالنا
                            parts = line.split("Price:$")
                            amount = int(parts[1].strip())
                            total += amount
                print(f"Total Revenue Generated: ${total}")
                print(f"Keep up the good work!")
            except FileNotFoundError:
                print("No sales recorded yet.")

        elif choice == '5':
            print("System Offline. Goodbye!")
            break

# سسٹم اسٹارٹ کریں
start_agent()
import random

# --- AI Agent: Secure Business Management System ---

def login():
    print("--- 🔒 Login Required ---")
    password = input("Enter Admin Password: ")
    if password == "saqib123": # آپ اپنا پاس ورڈ یہاں بدل سکتے ہیں
        print("✅ Access Granted!")
        return True
    else:
        print("❌ Access Denied! Incorrect Password.")
        return False

def start_agent():
    # لاگ ان چیک
    if not login():
        return

    print("\n--- 🚀 Elite Business AI & Finance System ---")
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. New Order Entry")
        print("2. View All Orders")
        print("3. Search Order by ID")
        print("4. Calculate Total Earnings")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            email = input("Customer Email: ")
            product = input("Product Name: ")
            service = input("Service (Video/Design/Content): ").lower()
            rates = {"video": 50, "design": 30, "content": 20}
            
            if service in rates:
                order_id = str(random.randint(1000, 9999))
                price = rates[service]
                data = f"ID:{order_id} | Email:{email} | Product:{product} | Price:${price}"
                with open("orders.txt", "a") as file:
                    file.write(data + "\n")
                print(f"✅ Order #{order_id} Saved!")
            else:
                print("❌ Invalid Service!")

        elif choice == '2':
            print("\n--- ALL ORDERS ---")
            try:
                with open("orders.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("No records yet.")

        elif choice == '3':
            search_id = input("Enter Order ID: ")
            found = False
            try:
                with open("orders.txt", "r") as file:
                    for line in file:
                        if f"ID:{search_id}" in line:
                            print(f"\n🔍 Result: {line.strip()}")
                            found = True
                            break
                if not found: print("❌ Not Found.")
            except FileNotFoundError:
                print("No records yet.")

        elif choice == '4':
            total = 0
            try:
                with open("orders.txt", "r") as file:
                    for line in file:
                        if "Price:$" in line:
                            amount = int(line.split("Price:$")[1].strip())
                            total += amount
                print(f"\n💰 Total Revenue: ${total}")
            except FileNotFoundError:
                print("No sales recorded.")

        elif choice == '5':
            print("System Offline. Goodbye!")
            break

# سسٹم چلائیں
start_agent()
import random

# --- AI Agent: Order Management & Status Tracking ---

def login():
    password = input("Enter Admin Password: ")
    return password == "saqib123"

def start_agent():
    if not login():
        print("❌ Access Denied!")
        return

    while True:
        print("\n--- 🚀 BUSINESS COMMAND CENTER ---")
        print("1. New Order | 2. View All | 3. Update Status | 4. Finance | 5. Exit")
        
        choice = input("Action (1-5): ")

        if choice == '1':
            # نیا آرڈر اور ڈیفالٹ سٹیٹس 'Pending'
            email = input("Email: ")
            service = input("Service (Video/Design/Content): ").lower()
            order_id = str(random.randint(1000, 9999))
            price = {"video": 50, "design": 30, "content": 20}.get(service, 0)
            
            if price > 0:
                data = f"ID:{order_id} | Email:{email} | Status
import random

# --- AI Agent: Pro Business Analytics & Management ---

def login():
    password = input("Enter Admin Password: ")
    return password == "saqib123"

def start_agent():
    if not login():
import random

# --- AI Agent: The Master Business System ---

def login():
    print("--- 🔐 Secure Access ---")
    password = input("Enter Admin Password: ")
    return password == "saqib123"

def start_agent():
    if not login():
        print("❌ Access Denied!")
        return

    while True:
        print("\n" + "="*40)
        print("        🚀 BUSINESS DASHBOARD")
        print("="*40)
        print("1. New Order      2. View All")
        print("3. Update Status  4. Filter by Status")
        print("5. Finance        6. DELETE Order")
        print("7. Exit")
        print("="*40)
        
        choice = input("Select Option (1-7): ")

        # --- 1. Create New Order ---
        if choice == '1':
            email = input("Customer Email: ")
            service = input("Service (Video/Design/Content): ").lower()
            order_id = str(random.randint(1000, 9999))
            rates = {"video": 50, "design": 30, "content": 20}
            
            if service in rates:
                data = f"ID:{order_id} | Email:{email} |
pip install pyinstaller
pyinstaller --onefile agent.py
import random
import datetime # تاریخ اور وقت کے لیے

def create_receipt(order_id, email, product, service, price):
    # گاہک کے لیے ایک الگ فائل بنانا
    filename = f"Receipt_{order_id}.txt"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = f"""
    ========================================
           OFFICIAL SERVICE RECEIPT
    ========================================
    Date: {now}
    Order ID: #{order_id}
    ----------------------------------------
    Customer: {email}
    Product:  {product}
    Service:  {service.capitalize()}
    ----------------------------------------
    TOTAL PAID: ${price}
    ----------------------------------------
    Status: Confirmed
    Thank you for choosing our services!
    ========================================
    """
    with open(filename, "w") as f:
        f.write(content)
    print(f"📄 Receipt generated: {filename}")

def start_agent():
    # (باقی مینو اور لاگ ان وہی رہے گا، بس آپشن 1 میں تبدیلی ہوگی)
    print("\n--- 🚀 Smart Business Agent with Auto-Receipts ---")
    
    while True:
        choice = input("\n1. New Order | 2. View All | 3. Exit: ")

        if choice == '1':
            email = input("Customer Email: ")
            product = input("Product Name: ")
            service = input("Service (Video/Design/Content): ").lower()
            rates = {"video": 50, "design": 30, "content": 20}
            
            if service in rates:
                order_id = str(random.randint(1000, 9999))
                price = rates[service]
                
                # 1. مین ڈیٹا بیس میں سیو کریں
                with open("orders.txt", "a") as file:
                    file.write(f"ID:{order_id} | Email:{email} | Price:${price}\n")
                
                # 2. خودکار رسید بنائیں (New Feature!)
                create_receipt(order_id, email, product, service, price)
                
                print(f"✅ Order Record Saved!")
            else:
                print("❌ Invalid Service!")
        
        elif choice == '2':
            try:
                with open("orders.txt", "r") as file: print(file.read())
            except: print("No records.")
            
        elif choice == '3':
            break

start_agent()
import tkinter as tk
from tkinter import messagebox

# فنکشن: جب بٹن دبایا جائے گا
def order_now():
    email = email_entry.get()
    service = service_entry.get()
    
    if email == "" or service == "":
        messagebox.showwarning("Error", "Please fill all fields!")
    else:
        messagebox.showinfo("Success", f"Order received for {email}\nService: {service}")

# 1. ونڈو بنانا
root = tk.Tk()
root.title("Saqib Business AI")
root.geometry("400x300") # ونڈو کا سائز

# 2. اسکرین پر لکھنا (Labels)
tk.Label(root, text="Customer Email:", font=("Arial", 12)).pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

tk.Label(root, text="Service Type:", font=("Arial", 12)).pack(pady=5)
service_entry = tk.Entry(root, width=30)
service_entry.pack(pady=5)

# 3. بٹن بنانا
order_button = tk.Button(root, text="Submit Order", command=order_now, bg="green", fg="white", font=("Arial", 10, "bold"))
order_button.pack(pady=20)

# ونڈو کو چلاتے رہنا
root.mainloop()
import tkinter as tk
from tkinter import messagebox
import random

# --- فنکشنز (بیک اینڈ لاجک) ---

def save_order():
    email = email_entry.get()
    product = product_entry.get()
    service = service_var.get().lower()
    
    # قیمت کا حساب
    rates = {"video": 50, "design": 30, "content": 20}
    
    if email == "" or product == "":
        messagebox.showwarning("Error", "تمام خانے پُر کریں!")
        return

    if service in rates:
        price = rates[service]
        order_id = str(random.randint(1000, 9999))
        
        # فائل میں محفوظ کرنا
        with open("orders.txt", "a") as file:
            file.write(f"ID:{order_id} | Email:{email} | Product:{product} | Price:${price}\n")
        
        messagebox.showinfo("Success", f"آرڈر محفوظ ہو گیا!\nID: #{order_id}\nBill: ${price}")
        
        # ان پٹ خانے صاف کرنا
        email_entry.delete(0, tk.END)
        product_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "صحیح سروس منتخب کریں (Video/Design/Content)")

# --- گرافکس (فرنٹ اینڈ) ---

root = tk.Tk()
root.title("Saqib's AI Business Manager")
root.geometry("400x450")
root.configure(bg="#f0f0f0") # ہلکا سرمئی رنگ

# ہیڈنگ
tk.Label(root, text="BUSINESS PANEL", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333").pack(pady=20)

# ای میل کا خانہ
tk.Label(root, text="Customer Email:", bg="#f0f0f0").pack()
email_entry = tk.Entry(root, width=35)
email_entry.pack(pady=5)

# پروڈکٹ کا خانہ
tk.Label(root, text="Product Name:", bg="#f0f0f0").pack()
product_entry = tk.Entry(root, width=35)
product_entry.pack(pady=5)

# سروس سلیکشن (Option Menu)
tk.Label(root, text="Select Service:", bg="#f0f0f0").pack()
service_var = tk.StringVar(root)
service_var.set("Video") # ڈیفالٹ آپشن
options = tk.OptionMenu(root, service_var, "Video", "Design", "Content")
options.pack(pady=10)

# سبمٹ بٹن
submit_btn = tk.Button(root, text="SAVE ORDER", command=save_order, bg="#27ae60", fg="white", font=("Arial", 10, "bold"), width=20, height=2)
submit_btn.pack(pady=20)

# ایگزٹ بٹن
exit_btn = tk.Button(root, text="Exit System", command=root.quit, bg="#c0392b", fg="white", width=15)
exit_btn.pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import messagebox, ttk # ttk ٹیبل بنانے کے لیے ہے
import random

# --- ڈیٹا دکھانے کی ونڈو (Table Window) ---
def view_orders():
    view_window = tk.Toplevel(root) # ایک نئی چھوٹی ونڈو کھولنا
    view_window.title("All Orders Record")
    view_window.geometry("600x400")

    # ٹیبل بنانا
    tree = ttk.Treeview(view_window, columns=("ID", "Email", "Product", "Price"), show='headings')
    tree.heading("ID", text="Order ID")
    tree.heading("Email", text="Customer Email")
    tree.heading("Product", text="Product")
    tree.heading("Price", text="Price ($)")
    
    tree.pack(fill=tk.BOTH, expand=True)

    # فائل سے ڈیٹا پڑھ کر ٹیبل میں ڈالنا
    try:
        with open("orders.txt", "r") as file:
            for line in file:
                # ڈیٹا کو ٹکڑوں میں بانٹنا: ID:1234 | Email:abc...
                parts = line.strip().split(" | ")
                id_val = parts[0].split(":")[1]
                email_val = parts[1].split(":")[1]
                prod_val = parts[2].split(":")[1]
                price_val = parts[3].split(":")[1]
                
                tree.insert("", tk.END, values=(id_val, email_val, prod_val, price_val))
    except FileNotFoundError:
        messagebox.showerror("Error", "کوئی ریکارڈ نہیں ملا!")

# --- آرڈر محفوظ کرنے کا فنکشن ---
def save_order():
    email = email_entry.get()
    product = product_entry.get()
    service = service_var.get().lower()
    rates = {"video": 50, "design": 30, "content": 20}
    
    if email == "" or product == "":
        messagebox.showwarning("Error", "خانے پُر کریں!")
        return

    order_id = str(random.randint(1000, 9999))
    price = rates[service]
    
    with open("orders.txt", "a") as file:
        file.write(f"ID:{order_id} | Email:{email} | Product:{product} | Price:{price}\n")
    
    messagebox.showinfo("Success", f"آرڈر محفوظ ہو گیا! ID: {order_id}")
    email_entry.delete(0, tk.END)
    product_entry.delete(0, tk.END)

# --- مین ونڈو (Main GUI) ---
root = tk.Tk()
root.title("Saqib's Business Suite")
root.geometry("400x500")

tk.Label(root, text="ORDER MANAGEMENT", font=("Arial", 14, "bold")).pack(pady=20)

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

tk.Label(root, text="Product:").pack()
product_entry = tk.Entry(root, width=30)
product_entry.pack(pady=5)

tk.Label(root, text="Service:").pack()
service_var = tk.StringVar(root)
service_var.set("Video")
tk.OptionMenu(root, service_var, "Video", "Design", "Content").pack(pady=10)

# بٹنز
tk.Button(root, text="SAVE ORDER", command=save_order, bg="#27ae60", fg="white", width=20).pack(pady=10)
tk.Button(root, text="VIEW ALL RECORDS", command=view_orders, bg="#2980b9", fg="white", width=20).pack(pady=10)
tk.Button(root, text="EXIT", command=root.quit, bg="#c0392b", fg="white", width=20).pack(pady=10)

root.mainloop()
import sqlite3

# 1. ڈیٹا بیس کے ساتھ کنکشن بنانا (اگر فائل نہیں ہے تو بن جائے گی)
connection = sqlite3.connect("business.db")

# 2. ایک کرسر (Cursor) بنانا جو ڈیٹا بیس میں جا کر کام کرے گا
cursor = connection.cursor()

# 3. ایک ٹیبل بنانا (اگر پہلے سے نہیں بنا ہوا)
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_email TEXT,
    product_name TEXT,
    service_type TEXT,
    price INTEGER
)
""")

# 4. تبدیلیوں کو محفوظ کرنا اور کنکشن بند کرنا
connection.commit()
connection.close()

print("✅ Database and Table Created Successfully!")
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# --- ڈیٹا بیس کے فنکشنز ---

def init_db():
    """ڈیٹا بیس اور ٹیبل بنانا"""
    conn = sqlite3.connect("my_business.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            product TEXT,
            service TEXT,
            price INTEGER
        )
    """)
    conn.commit()
    conn.close()

def save_to_db():
    """ڈیٹا بیس میں آرڈر محفوظ کرنا"""
    email = email_entry.get()
    product = product_entry.get()
    service = service_var.get()
    rates = {"Video": 50, "Design": 30, "Content": 20}
    
    if email == "" or product == "":
        messagebox.showerror("Error", "تمام خانے پُر کریں!")
        return

    price = rates[service]
    
    conn = sqlite3.connect("my_business.db")
    cursor = conn.cursor()
    # SQL Query: ڈیٹا ڈالنے کے لیے
    cursor.execute("INSERT INTO orders (email, product, service, price) VALUES (?, ?, ?, ?)", 
                   (email, product, service, price))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", f"آرڈر ڈیٹا بیس میں محفوظ ہو گیا!")
    email_entry.delete(0, tk.END)
    product_entry.pack_forget() # یا صرف انٹری صاف کریں
    product_entry.delete(0, tk.END)

def show_records():
    """ڈیٹا بیس سے ریکارڈز لا کر ٹیبل میں دکھانا"""
    records_win = tk.Toplevel(root)
    records_win.title("Database Records")
    records_win.geometry("600x400")
    
    tree = ttk.Treeview(records_win, columns=("1","2","3","4","5"), show='headings')
    tree.heading("1", text="ID"); tree.heading("2", text="Email")
    tree.heading("3", text="Product"); tree.heading("4", text="Service")
    tree.heading("5", text="Price")
    tree.pack(fill=tk.BOTH, expand=True)

    conn = sqlite3.connect("my_business.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall() # تمام ڈیٹا نکالنا
    
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()

# --- مین ونڈو (GUI) ---

init_db() # پروگرام شروع ہوتے ہی ڈیٹا بیس تیار کرنا
root = tk.Tk()
root.title("Saqib's SQL Manager")
root.geometry("400x450")

tk.Label(root, text="SQL DATABASE SYSTEM", font=("Arial", 14, "bold")).pack(pady=20)

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root, width=30); email_entry.pack(pady=5)

tk.Label(root, text="Product:").pack()
product_entry = tk.Entry(root, width=30); product_entry.pack(pady=5)

service_var = tk.StringVar(root); service_var.set("Video")
tk.OptionMenu(root, service_var, "Video", "Design", "Content").pack(pady=10)

tk.Button(root, text="SAVE TO SQL", command=save_to_db, bg="#27ae60", fg="white", width=20).pack(pady=10)
tk.Button(root, text="VIEW SQL RECORDS", command=show_records, bg="#2980b9", fg="white", width=20).pack(pady=10)

root.mainloop()
import smtplib
from email.message import EmailMessage

def send_confirmation_email(customer_email, order_id, product):
    # اپنی معلومات یہاں ڈالیں
    my_email = "your-email@gmail.com" 
    my_password = "your-app-password" # گوگل سے حاصل کردہ ایپ پاس ورڈ

    # ای میل کا ڈھانچہ بنانا
    msg = EmailMessage()
    msg['Subject'] = f"Order Confirmed: #{order_id}"
    msg['From'] = my_email
    msg['To'] = customer_email
    msg.set_content(f"Hello,\n\nThank you for your order of {product}.\nYour Order ID is #{order_id}.\n\nBest regards,\nSaqib Business Team")

    # ای میل بھیجنا
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(my_email, my_password)
            smtp.send_message(msg)
        print("📧 Confirmation email sent!")
    except Exception as e:
        print(f"❌ Email failed: {e}")
pip install pywhatkit
import pywhatkit as kit

# میسج بھیجنے کا طریقہ: (نمبر، میسج، گھنٹہ، منٹ)
# نوٹ: نمبر کے ساتھ کنٹری کوڈ (+92) لازمی لکھیں
try:
    # یہ میسج ابھی سے 2 منٹ بعد جائے گا (تاکہ واٹس ایپ ویب لاگ ان ہونے کا وقت ملے)
    kit.sendwhatmsg("+923XXXXXXXXX", "Assalam-o-Alaikum! Your order is confirmed. - Saqib Business", 14, 30)
    print("✅ WhatsApp message scheduled!")
except Exception as e:
    print(f"❌ Error: {e}")
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3

# --- مین ڈیش بورڈ کلاس ---
class BusinessDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Saqib's Business OS v1.0")
        self.root.geometry("1000x600")
        self.root.configure(bg="#2c3e50")

        # 1. Sidebar (سائیڈ بار)
        self.sidebar = tk.Frame(self.root, bg="#34495e", width=200, height=600)
        self.sidebar.pack(side="left", fill="y")

        tk.Label(self.sidebar, text="MENU", font=("Arial", 14, "bold"), bg="#34495e", fg="white").pack(pady=20)
        
        # سائیڈ بار بٹنز
        self.btn_new = tk.Button(self.sidebar, text="➕ New Order", font=("Arial", 10), bg="#2ecc71", fg="white", width=18)
        self.btn_new.pack(pady=10)
        
        self.btn_db = tk.Button(self.sidebar, text="📂 Database", font=("Arial", 10), bg="#3498db", fg="white", width=18)
        self.btn_db.pack(pady=10)

        # 2. Main Content Area (مین ایریا)
        self.main_area = tk.Frame(self.root, bg="white", width=800, height=600)
        self.main_area.pack(side="right", fill="both", expand=True)

        # 3. Sales Graph (گراف کا حصہ)
        self.show_graph()

    def show_graph(self):
        # فرضی ڈیٹا (بعد میں ڈیٹا بیس سے جوڑیں گے)
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        sales = [200, 450, 300, 700, 600]

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(months, sales, marker='o', color='#e67e22', linewidth=2)
        ax.set_title("Monthly Sales Growth")
        ax.set_xlabel("Months")
        ax.set_ylabel("Earnings ($)")

        canvas = FigureCanvasTkAgg(fig, master=self.main_area)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=50)

# سسٹم لانچ کریں
if __name__ == "__main__":
    root = tk.Tk()
    app = BusinessDashboard(root)
    root.mainloop()
pip install gspread oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def sync_to_google_sheets(order_data):
    # گوگل کلاؤڈ سے حاصل کردہ چابی کا استعمال
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("your_key.json", scope)
    client = gspread.authorize(creds)

    # اپنی گوگل شیٹ کا نام لکھیں
    sheet = client.open("My_Business_Orders").sheet1

    # شیٹ کے آخر میں نیا ڈیٹا جوڑنا
    sheet.append_row(order_data)
    print("✅ Data Synced to Google Sheets Live!")

# مثال کے طور پر ڈیٹا بھیجنا
# sync_to_google_sheets(["101", "saqib@email.com", "Logo Design", "30"])
pip install streamlit
import streamlit as st
import pandas as pd
import sqlite3

# 1. ویب پیج کی سیٹنگ
st.set_page_config(page_title="Saqib Business Cloud", layout="wide")

st.title("🚀 Saqib's Business Web Dashboard")
st.markdown("Welcome to your **Live Marketing & Order** control center.")

# 2. ڈیٹا بیس سے لائیو ڈیٹا اٹھانا
def load_data():
    conn = sqlite3.connect("my_business.db")
    df = pd.read_sql_query("SELECT * FROM orders", conn)
    conn.close()
    return df

# 3. سائیڈ بار مینو
st.sidebar.header("Navigation")
menu = st.sidebar.radio("Go to", ["Dashboard", "Add New Order", "Analytics"])

if menu == "Dashboard":
    st.subheader("📊 Current Orders")
    data = load_data()
    st.dataframe(data, use_container_width=True) # خوبصورت ٹیبل

elif menu == "Add New Order":
    st.subheader("➕ Create New Order")
    with st.form("order_form"):
        email = st.text_input("Customer Email")
        product = st.text_input("Product")
        service = st.selectbox("Service", ["Video", "Design", "Content"])
        submit = st.form_submit_button("Save Order")
        
        if submit:
            st.success(f"Order for {email} has been synced to Cloud!")

elif menu == "Analytics":
    st.subheader("📈 Business Growth")
    data = load_data()
    # خودکار گراف بنانا
    st.line_chart(data['price'])


    
