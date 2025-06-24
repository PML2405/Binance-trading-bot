# Simplified Binance Futures Trading Bot

This project is a **command-line trading bot** built in Python for the **Binance Futures Testnet**. It was developed as a skills assessment for the Junior Python Developer role. The bot connects to Binance's API to place **market** and **limit** orders for USDT-M futures contracts.

---

## 🚀 Features

* **Binance Testnet Integration** – Connects securely to Binance Futures Testnet.
* **Order Placement** – Supports both **Market** and **Limit** orders.
* **Buy & Sell Support** – Executes both `BUY` (long) and `SELL` (short) trades.
* **Interactive CLI** – User-friendly command-line prompts for trade execution.
* **Input Validation** – Basic validation for order types and sides.
* **Robust Logging** – Logs API requests, responses, and errors to `bot.log`.
* **Error Handling** – Gracefully handles common API issues like tick size precision errors.

---

## 🧰 Technology Stack

* **Language**: Python 3
* **Main Library**: [`python-binance`](https://github.com/sammchardy/python-binance)
* **Supporting Libraries**: `pandas`, `numpy` (for future analytical features)

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/PML2405/Binance-trading-bot.git
cd Binance-trading-bot
```

### 2. Install Dependencies

Make sure you have Python 3 installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Configure API Credentials

Get your API key and secret from the Binance **Futures Testnet**.

* Create a file called `config.py` in the root directory.
* Add your credentials:

```python
# config.py
API_KEY = "your_testnet_api_key_here"
API_SECRET = "your_testnet_api_secret_here"
```

> `config.py` is included in `.gitignore` so it will not be committed to the repository.

---

## 🧪 How to Use

Run the bot using:

```bash
python main.py
```

You'll be prompted to enter trade details.

### 💡 Example Session:

```
--- Simplified Trading Bot ---
Enter the symbol (e.g., BTCUSDT): BTCUSDT
Enter order side (BUY or SELL): BUY
Enter order type (MARKET or LIMIT): LIMIT
Enter quantity: 0.001
Enter price for LIMIT order: 102500.0
```

The bot will place the order and log the outcome to the console and `bot.log`.

---

## 📘 Key Learnings & Challenges

This was my first trading bot project. A major challenge was handling **Binance's strict tick size precision rules**. I overcame the `"Price not increased by tick size"` error by dynamically fetching API filters and formatting prices accordingly. This deepened my understanding of external API integration, debugging, and precision handling in real-world applications.

---

## 📈 Future Improvements

* ✅ Add support for advanced order types like **Stop-Limit** and **OCO**.
* ✅ Implement basic trading strategies (e.g., **Moving Averages**, **RSI**).
* ✅ Real-time **position tracking dashboard** with open positions, P\&L, and balance.
* ✅ Improve **error reporting** and **user feedback** mechanisms.

---
