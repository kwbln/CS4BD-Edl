from queue import Queue

from StreamingKafka import KConsumer
from StreamingKafka import KProducer


def main():
    network = ['localhost', '9092']
    queue = Queue()

    # Producer A: 20 numbers, even, 1s sleep
    queue.put((20, True, 1))

    # Producer B: 10 numbers, odd, 2s sleep
    queue.put((10, False, 2))

    topics = 'AB'

    for char in topics:
        worker = KProducer.KProducer(network=network, queue=queue, topic=char)
        worker.daemon = True
        worker.start()

    worker_consumer = KConsumer.KConsumer(network=network)
    worker_consumer.daemon = True
    worker_consumer.start()

    queue.join()


main()
