import pika
import util
import sys

params = util.get_params()
conn = pika.BlockingConnection(params)
chan = conn.channel()

def callback(ch, method, properties, body):
	print("[x] Received %r" % body)

chan.queue_declare(queue='water-cooler')

chan.basic_consume(queue='water-cooler', auto_ack=True, on_message_callback=callback)
try:
	print("[*] Waiting for messages...")
	chan.start_consuming()
except KeyboardInterrupt:
	print("\nGoodbye!")
	sys.exit()