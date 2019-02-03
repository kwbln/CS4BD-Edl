import time
from threading import Thread

from kafka import KafkaProducer


class KProducer(Thread):

    def __init__(self, queue, network, topic):

        Thread.__init__(self)
        self.queue = queue
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=network)

    def run(self):
        while True:

            n, even, sleep = self.queue.get()
            print('Producer topic {0}: n {1} numbers, even {2}, sleep for {3}s'.format(self.topic, n, even, sleep))

            try:
                for i in range(n):

                    if (even == True and i % 2 == 0):
                        self.producer.send(self.topic, str(i).encode('utf-8'))

                    elif (even == False and i % 2 == 1):

                        self.producer.send(self.topic, str(i).encode('utf-8'))

                    time.sleep(sleep)
            finally:
                self.queue.task_done()
