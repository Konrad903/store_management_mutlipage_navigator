# 🧾 Customer & Invoice Management Suite (Streamlit Multi-Page App)

A combined Streamlit application that brings together **customer registration** and **invoice generation** into a single multi-page interface. The navigation controller (`complete.py`) ties the two pages together using Streamlit's modern `st.navigation` / `st.Page` API.

> **Note:** This README documents the combined app. For the individual page files, see the sections below. `gen_invoice.py` is referenced in the navigation but its full source is not included here; it is assumed to be a Streamlit form for creating invoices, similar in structure to `add_cust.py`.

## 📌 Project Overview

This multi-page project demonstrates:

- Multi-page Streamlit apps with `st.navigation` and `st.Page`
- Sidebar grouping with icons and default page selection
- Page dispatch via `page.run()`
- Form-based data entry with `st.text_input`, `st.number_input`, `st.text_area`
- Pandas DataFrame concatenation and CSV persistence
- Session-safe page structure

## ⚙️ How It Works

### 1. Navigation Controller (`complete.py`)

- Registers two pages using `st.Page(...)`:
  - **Add New Customer** — icon 🙍‍♂️, `default=False`
  - **Generate Invoice** — icon 💵, `default=True`
- Groups pages into sections:
  - `'Customer': [add_cust]`
  - `'Invoice': [gen_invoice]`
- Builds the sidebar with `st.navigation({...})`
- Runs the selected page with `page.run()`

### 2. Customer Page (`add_cust.py`)

- Loads `customers.csv` with `pd.read_csv`
- Collects:
  - Name (text input, auto-capitalized)
  - Phone number (10-digit number input)
  - Email (text input)
  - Address (text area)
- On **Add Customer** button click:
  - Builds a one-row DataFrame
  - Concatenates with existing data
  - Writes back to `customers.csv`
  - Displays the updated table
- Validates that name, phone, and email are non-empty

### 3. Invoice Page (`gen_invoice.py`)

> ⚠️ **Source not provided in this bundle.** Based on the navigation context, this page is expected to:
> - Accept invoice details (customer, items, amounts)
> - Generate an invoice record
> - Persist to a CSV or display a formatted invoice
> - Possibly link to the customer list from `customers.csv`

## ▶️ How to Run

### Requirements

```bash
pip install streamlit pandas
