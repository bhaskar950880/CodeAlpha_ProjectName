import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 320,
    "AMZN": 3300
}

portfolio = []  # list to store portfolio entries


def calculate_total():
    stock = stock_entry.get().upper()
    qty = qty_entry.get()

    if stock not in stock_prices:
        messagebox.showerror("Error", f"{stock} is not in our stock list.")
        return

    try:
        qty = int(qty)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be a number.")
        return

    price = stock_prices[stock]
    total = price * qty
    result_text = f"{stock} - Qty: {qty} @ ${price} = ${total}"
    result_list.insert(tk.END, result_text)
    portfolio.append((stock, qty, price, total))


def save_to_file():
    if not portfolio:
        messagebox.showinfo("No Data", "No portfolio data to save.")
        return

    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if filepath:
        with open(filepath, "w") as file:
            file.write("Stock Portfolio Tracker Summary:\n\n")
            total_investment = 0
            for stock, qty, price, total in portfolio:
                file.write(f"{stock} - Qty: {qty} @ ${price} = ${total}\n")
                total_investment += total
            file.write(f"\nTotal Investment Value: ${total_investment}")
        messagebox.showinfo("Saved", f"Portfolio saved to {filepath}")


# Main Window
root = tk.Tk()
root.title("Stock Portfolio Tracker")
root.geometry("500x450")
root.configure(bg="#f4f4f4")  # light office-style background

# Title Label
title = tk.Label(root, text="📈 Stock Portfolio Tracker", font=("Helvetica", 16, "bold"), bg="#f4f4f4")
title.pack(pady=10)

# Stock Input
stock_label = tk.Label(root, text="Stock Symbol (e.g., AAPL):", bg="#f4f4f4")
stock_label.pack()
stock_entry = tk.Entry(root, width=30)
stock_entry.pack(pady=5)

# Quantity Input
qty_label = tk.Label(root, text="Quantity:", bg="#f4f4f4")
qty_label.pack()
qty_entry = tk.Entry(root, width=30)
qty_entry.pack(pady=5)

# Buttons
calc_btn = tk.Button(root, text="Calculate Investment", command=calculate_total, bg="#4CAF50", fg="white", width=25)
calc_btn.pack(pady=10)

save_btn = tk.Button(root, text="Save to File", command=save_to_file, bg="#2196F3", fg="white", width=25)
save_btn.pack()

# Result Listbox
result_label = tk.Label(root, text="Portfolio Summary:", bg="#f4f4f4")
result_label.pack(pady=(20, 5))
result_list = tk.Listbox(root, width=60, height=10)
result_list.pack()

# Run the app
root.mainloop()
