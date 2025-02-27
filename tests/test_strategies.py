import pytest
from strategies.ema_crossover import EMAStrategy
from strategies.macd_strategy import MACDStrategy
import ccxt

class TestStrategies:
    @pytest.fixture
    def exchange(self):
        return ccxt.binance()

    def test_ema_strategy(self, exchange):
        strategy = EMAStrategy(exchange)
        signal = strategy.get_signal('BTC/USDT')
        assert signal in ['buy', 'sell', 'hold']

    def test_macd_strategy(self, exchange):
        strategy = MACDStrategy(exchange)
        signal = strategy.get_signal('BTC/USDT')
        assert signal in ['buy', 'sell', 'hold']