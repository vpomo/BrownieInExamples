import brownie
import time

def test_read_timestamp():
    timestamp = int(time.time())
    assert timestamp > 0


