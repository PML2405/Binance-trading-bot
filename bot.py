# bot.py
import logging
from binance import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from config import API_KEY, API_SECRET

class BasicBot:
    def __init__(self, testnet=True):
        """Initializes the bot by connecting to the Binance client."""
        self.client = Client(API_KEY, API_SECRET, testnet=testnet)
        # Point the client to the Futures Testnet URL
        self.client.API_URL = 'https://testnet.binancefuture.com/fapi'
        logging.info("Bot initialized and connected to Binance Futures Testnet.")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        """Places a market or limit order."""
        try:
            logging.info(f"Attempting to place a {side} {order_type} order for {quantity} of {symbol}.")
            
            params = {
                'symbol': symbol,
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity,
            }

            if order_type.upper() == 'LIMIT':
                if not price:
                    logging.error("Price is required for a LIMIT order.")
                    return None
                params['price'] = price
                params['timeInForce'] = 'GTC'  # Good 'Til Canceled

            order = self.client.futures_create_order(**params)
            logging.info("Successfully placed order:")
            logging.info(order)
            return order

        except BinanceAPIException as e:
            logging.error(f"Binance API Error: {e.status_code} - {e.message}")
            return None
        except BinanceOrderException as e:
            logging.error(f"Binance Order Error: {e.code} - {e.message}")
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return None
