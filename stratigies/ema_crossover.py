from .base_strategy import BaseStrategy
import numpy as np

class EMAStrategy(BaseStrategy):
    def get_signal(self, symbol: str) -> str:
        data = self.exchange.fetch_ohlcv(symbol, '1h', limit=100)
        closes = [x[4] for x in data]
        
        ema12 = np.convolve(closes, np.ones(12)/12, mode='valid')[-1]
        ema26 = np.convolve(closes, np.ones(26)/26, mode='valid')[-1]
        
        if ema12 > ema26:
            return 'buy'
        elif ema12 < ema26:
            return 'sell'
        return 'hold'