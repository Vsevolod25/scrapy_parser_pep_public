class StatusSummaryPipeline:

    def open_spider(self, spider):
        self.statuses = {}

    def process_item(self, item, spider):
        self.statuses[item['status']] = self.statuses.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        file_path = 'results/status_summary_%(time)s.csv'
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status in self.statuses:
                f.write(f'{status},{self.statuses[status]}\n')
            f.write(f'Total,{sum(self.statuses.values())}\n')
        print(self.statuses)
