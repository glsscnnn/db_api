import pika
import util
import yaml

# get parameters and create connection
params = util.get_params()
conn = pika.BlockingConnection(params)

chan = conn.channel()

# declare queue and publish something
chan.queue_declare(queue='water-cooler')
chan.basic_publish(exchange='', routing_key='water-cooler', body='hello!')

# tell user that the message has been sent and close connection
print("[x] Sent Message!")
conn.close()