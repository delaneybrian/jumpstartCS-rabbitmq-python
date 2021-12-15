import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f'received new message: {body}')

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare('headersexchange', ExchangeType.headers)

channel.queue_declare('letterbox')

bind_args = {
  'x-match': 'any',
  'name': 'brian',
  'age': '21'
}

channel.queue_bind('letterbox', 'headersexchange', arguments=bind_args)

channel.basic_consume(queue='letterbox', auto_ack=True,
    on_message_callback=on_message_received)

print('Starting Consuming')

channel.start_consuming()