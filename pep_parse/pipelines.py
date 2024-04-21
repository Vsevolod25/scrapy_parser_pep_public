import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR, RESULTS_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
            f'{BASE_DIR}/{RESULTS_DIR}/status_summary_'
            f'{dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.csv',
            mode='w',
            encoding='utf-8'
        ) as f:
            f.write('Статус,Количество\n')
            for status in self.statuses:
                f.write(f'{status},{self.statuses[status]}\n')
            f.write(f'Total,{sum(self.statuses.values())}\n')
