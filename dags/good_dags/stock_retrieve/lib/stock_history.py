import io
from time import sleep

import pandas as pd
import requests
from good_dags.stock_retrieve.lib.epoch_manipulate import EpochManipulate


class StockHistory(object):
    def __init__(self):
        self.epoch = EpochManipulate()

    def stock_retrieve(
        self, stock, period1=None, period2=None, interval="1d", events="history", **kwargs
    ):
        period1 = self.epoch._get_previous_epoch_days(7) if not period1 else period1
        period2 = self.epoch._get_current_epoch() if not period2 else period2

        print(
            f"[DataRetriever] Getting data for: stock {stock}, {period1} to {period2}, interval: {interval}, events: {events}..."
        )

        stock = stock.strip()
        url = f"https://query1.finance.yahoo.com/v7/finance/download/{stock}?period1={period1}&period2={period2}&interval={interval}&events={events}"
        response = requests.get(url)

        if not response.ok:
            # Retry one time due to page not found
            print("[DataRetriever] Failure occurred, waiting 10 seconds then retrying once...")
            sleep(10)

            response = requests.get(url)
            if not response.ok:
                raise Exception(f"[DataRetriever] Yahoo request error. Response: {response.text}")

        data = response.content.decode("utf8")
        df_history = pd.read_csv(io.StringIO(data))
        print(df_history)


if __name__ == '__main__':
    StockHistory().stock_retrieve('GOOGL')
