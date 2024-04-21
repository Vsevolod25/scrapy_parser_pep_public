import datetime as dt

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = {}
        self.now = dt.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    def process_item(self, item, spider):
        self.statuses[
            item['status']
        ] = self.statuses.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        with open(
            f'{BASE_DIR}/results/status_summary_{self.now}.csv',
            mode='w',
            encoding='utf-8'
        ) as f:
            f.write('Статус,Количество\n')
            for status in self.statuses:
                f.write(f'{status},{self.statuses[status]}\n')
            f.write(f'Total,{sum(self.statuses.values())}\n')
