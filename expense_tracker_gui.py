import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import pandas as pd

CSV_FILE = 'expenses.csv'
FIELDNAMES = ['date', 'amount', 'category', 'description']

# Ensure CSV file exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()

def add_expense(date_str, amount, category, description):
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({
            'date': date_str,
            'amount': amount,
            'category': category,
            'description': description
        })

def load_expenses():
    expenses = []
    with open(CSV_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['amount'] = float(row['amount'])
            expenses.append(row)
    return expenses

def view_summary():
    expenses = load_expenses()
    if not expenses:
        messagebox.showinfo('Summary', 'No expenses to summarize.')
        return
    # By category
    summary_cat = {}
    for exp in expenses:
        summary_cat[exp['category']] = summary_cat.get(exp['category'], 0) + exp['amount']
    summary_cat_str = '\n'.join([f'{cat}: {total:.2f}' for cat, total in summary_cat.items()])
    # By month
    summary_month = {}
    for exp in expenses:
        month = exp['date'][:7]  # YYYY-MM
        summary_month[month] = summary_month.get(month, 0) + exp['amount']
    summary_month_str = '\n'.join([f'{month}: {total:.2f}' for month, total in summary_month.items()])
    messagebox.showinfo('Summary', f'Summary by Category:\n{summary_cat_str}\n\nSummary by Month:\n{summary_month_str}')

def plot_chart():
    expenses = load_expenses()
    if not expenses:
        messagebox.showinfo('Plot', 'No expenses to plot.')
        return
    # Bar chart by category
    summary_cat = {}
    for exp in expenses:
        summary_cat[exp['category']] = summary_cat.get(exp['category'], 0) + exp['amount']
    categories = list(summary_cat.keys())
    totals = list(summary_cat.values())
    plt.figure(figsize=(8,5))
    plt.bar(categories, totals, color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Total Spent')
    plt.title('Expenses by Category')
    plt.tight_layout()
    plt.show()

def export_to_excel():
    try:
        df = pd.read_csv(CSV_FILE)
        out_file = 'expenses_export.xlsx'
        df.to_excel(out_file, index=False)
        messagebox.showinfo('Export', f'Exported to {out_file}')
    except Exception as e:
        messagebox.showerror('Export', f'Export failed: {e}')

def submit_expense(date_entry, amount_entry, category_entry, desc_entry):
    date_str = date_entry.get().strip()
    if not date_str:
        date_str = datetime.today().strftime('%Y-%m-%d')
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror('Error', 'Invalid date format. Use YYYY-MM-DD.')
        return
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror('Error', 'Invalid amount.')
        return
    category = category_entry.get().strip()
    description = desc_entry.get().strip()
    add_expense(date_str, amount, category, description)
    messagebox.showinfo('Success', 'Expense added!')
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.title('Expense Tracker')
    root.geometry('400x350')

    frm = ttk.Frame(root, padding=10)
    frm.pack(fill='both', expand=True)

    ttk.Label(frm, text='Date (YYYY-MM-DD):').grid(row=0, column=0, sticky='e')
    date_entry = ttk.Entry(frm)
    date_entry.grid(row=0, column=1, pady=5)

    ttk.Label(frm, text='Amount:').grid(row=1, column=0, sticky='e')
    amount_entry = ttk.Entry(frm)
    amount_entry.grid(row=1, column=1, pady=5)

    ttk.Label(frm, text='Category:').grid(row=2, column=0, sticky='e')
    category_entry = ttk.Entry(frm)
    category_entry.grid(row=2, column=1, pady=5)

    ttk.Label(frm, text='Description:').grid(row=3, column=0, sticky='e')
    desc_entry = ttk.Entry(frm)
    desc_entry.grid(row=3, column=1, pady=5)

    submit_btn = ttk.Button(frm, text='Add Expense', command=lambda: submit_expense(date_entry, amount_entry, category_entry, desc_entry))
    submit_btn.grid(row=4, column=0, columnspan=2, pady=10)

    sep = ttk.Separator(frm, orient='horizontal')
    sep.grid(row=5, column=0, columnspan=2, sticky='ew', pady=10)

    summary_btn = ttk.Button(frm, text='View Summary', command=view_summary)
    summary_btn.grid(row=6, column=0, columnspan=2, pady=5, sticky='ew')

    plot_btn = ttk.Button(frm, text='Plot Chart', command=plot_chart)
    plot_btn.grid(row=7, column=0, columnspan=2, pady=5, sticky='ew')

    export_btn = ttk.Button(frm, text='Export to Excel', command=export_to_excel)
    export_btn.grid(row=8, column=0, columnspan=2, pady=5, sticky='ew')

    root.mainloop()

if __name__ == '__main__':
    main() 
