# ☕ Starbucks CLI Ordering System

A command-line based coffee ordering simulation system built in Python.  
Simulates real-world ordering experience, handles user login, multiple orders, pricing, and receipt generation.

---

## 🚀 Features

- ✅ Secure login system with password masking (`getpass`)
- ✅ Password retry limit with cooldown
- ✅ Clean, looped order input using `take_order()` function
- ✅ Custom drink selection: coffee type, size, milk, temperature
- ✅ Automatic price calculation based on selections
- ✅ Estimated wait-time generation
- ✅ Receipts saved as `.txt` files with unique order IDs
- ✅ Supports multiple orders in one session

---

## 📦 How to Run

```bash
python starbucks_cli_system.py

## 🧠 Tech Used

- Python 3.x
- getpass for secure password input
- random for wait time + receipt IDs
- File I/O (open, write) for saving receipts
- Dictionaries and lists for structured data

---

## 📁 Example Receipt

Order Receipt #49281  
Customer: Alex  
Drink: Iced Grande Latte with Oat milk  
Price: $4.50  
Estimated wait time: 5 minutes

---

## 🔧 Future Improvements (Planned)

- [ ] Cart system: order multiple drinks in one go
- [ ] Loyalty points system per user
- [ ] Daily summary report
- [ ] Centralized receipt log file
- [ ] Tip option + total breakdown
- [ ] GitHub Actions auto-run for test logging


👤 Author

exile-code
GitHub Profile →https://github.com/exile-code

📜 License

MIT License – free to use, modify, distribute.