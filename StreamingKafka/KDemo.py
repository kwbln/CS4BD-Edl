from queue import Queue

from StreamingKafka import KProducer
from StreamingKafka import KConsumer



def main():
    network = ['localhost', '9092']
    queue = Queue()

    queue.put((20, True, 1))  # 20 numbers, even, 1s sleep
    queue.put((10, False, 2))  # 10 numbers, odd, 2s sleep

    topics = 'AB'

    for char in topics:
        worker = KProducer(network=network, queue=queue, topic=char)
        worker.daemon = True
        worker.start()

    worker_consumer = KConsumer(network=network)
    worker_consumer.daemon = True
    worker_consumer.start()

    queue.join()


main()
