# main.py
import logging
from bot import BasicBot

def setup_logging():
    """Configures logging to file and console."""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler("bot.log"),
                            logging.StreamHandler()
                        ])

def main():
    """Main function to run the trading bot CLI."""
    setup_logging()
    bot = BasicBot()

    print("\n--- Simplified Trading Bot ---")
    
    # Input validation
    while True:
        symbol = input("Enter the symbol (e.g., BTCUSDT): ").upper()
        if symbol: break
        print("Symbol cannot be empty.")

    while True:
        side = input("Enter order side (BUY or SELL): ").upper()
        if side in ['BUY', 'SELL']: break
        print("Invalid side. Please enter 'BUY' or 'SELL'.")

    while True:
        order_type = input("Enter order type (MARKET or LIMIT): ").upper()
        if order_type in ['MARKET', 'LIMIT']: break
        print("Invalid order type. Please enter 'MARKET' or 'LIMIT'.")

    while True:
        try:
            quantity = float(input("Enter quantity: "))
            if quantity > 0: break
            print("Quantity must be positive.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    
    price = None
    if order_type == 'LIMIT':
        while True:
            try:
                price = float(input("Enter price for LIMIT order: "))
                if price > 0: break
                print("Price must be positive.")
            except ValueError:
                print("Invalid price. Please enter a number.")
    
    # Place the order
    bot.place_order(symbol, side, order_type, quantity, price)

if __name__ == "__main__":
    main()
