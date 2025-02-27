import sqlite3
from datetime import datetime, timedelta
from config.settings import Config

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(Config.DB_NAME)
        self._create_tables()
    
    def _create_tables(self):
        cursor = self.conn.cursor()
        
        # Trades table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trades (
                id INTEGER PRIMARY KEY,
                timestamp DATETIME,
                type TEXT,
                entry_price REAL,
                quantity REAL,
                exit_price REAL,
                profit REAL,
                period INTEGER,
                status TEXT DEFAULT 'open'
            )
        ''')
        
        # Periods table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS periods (
                period_id INTEGER PRIMARY KEY,
                start_time DATETIME,
                end_time DATETIME,
                start_balance REAL,
                end_balance REAL,
                total_trades INTEGER,
                profitable_trades INTEGER
            )
        ''')
        
        self.conn.commit()

    def add_trade(self, trade_data):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO trades 
            (timestamp, type, entry_price, quantity, period)
            VALUES (?, ?, ?, ?, ?)
        ''', trade_data)
        self.conn.commit()
        return cursor.lastrowid

    def update_trade(self, trade_id, exit_price, profit):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE trades 
            SET exit_price = ?, profit = ?, status = 'closed'
            WHERE id = ?
        ''', (exit_price, profit, trade_id))
        self.conn.commit()

    def get_open_trades(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM trades WHERE status = "open"')
        return cursor.fetchall()

    def cleanup_old_data(self):
        cutoff_date = datetime.now() - timedelta(days=Config.DATA_RETENTION_DAYS)
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM trades WHERE timestamp < ?', (cutoff_date,))
        self.conn.commit()