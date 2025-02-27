import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Trading parameters
    RISK_PERCENT = 1.0
    INITIAL_BALANCE = 1000.0
    MAX_DAILY_TRADES = 5
    STOP_LOSS = 1.5    # %
    TAKE_PROFIT = 3.0  # %
    SYMBOL = 'BTC/USDT'
    STRATEGY = 'macd'  # macd/ema/rsi
    
    # Exchange configuration
    EXCHANGE = 'binance'
    API_KEY = os.getenv("API_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    # Telegram configuration
    TG_TOKEN = os.getenv("TG_TOKEN")
    TG_CHAT_ID = os.getenv("TG_CHAT_ID")
    
    # Database
    DB_NAME = 'trading.db'
    DATA_RETENTION_DAYS = 90