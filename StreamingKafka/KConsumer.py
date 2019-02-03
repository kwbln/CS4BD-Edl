from threading import Thread

from kafka import KafkaConsumer


class KConsumer(Thread):

    def __init__(self, network):

        Thread.__init__(self)

        self.consumer = KafkaConsumer('A', 'B', consumer_timeout_ms=10000, bootstrap_servers=network)

    def run(self):
        while True:
            try:
                print('timestamp | topic | offset | value')
                for message in self.consumer:
                    print(message.timestamp, ' | ', message.topic, ' | ', message.offset, ' | ', message.value)

            finally:
                print('done')
