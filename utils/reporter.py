from database.manager import DatabaseManager
from datetime import datetime
from config.settings import Config

class ReportGenerator:
    def __init__(self):
        self.db = DatabaseManager()
    
    def generate_period_report(self, period_id: int) -> str:
        cursor = self.db.conn.cursor()
        cursor.execute('''
            SELECT * FROM periods 
            WHERE period_id = ?
        ''', (period_id,))
        period_data = cursor.fetchone()
        
        cursor.execute('''
            SELECT COUNT(*), SUM(profit) 
            FROM trades 
            WHERE period = ?
        ''', (period_id,))
        trades_count, total_profit = cursor.fetchone()
        
        return (
            f"📊 *Report for Period {period_id}*\n"
            f"🕒 Period: {period_data[1]} - {period_data[2]}\n"
            f"💰 Start Balance: ${period_data[3]:.2f}\n"
            f"🏁 End Balance: ${period_data[4]:.2f}\n"
            f"🔢 Total Trades: {trades_count}\n"
            f"📈 Total Profit: ${total_profit:.2f}"
        )