import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='altexchange', exchange_type=ExchangeType.fanout)

channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct, arguments={'alternate-exchange': 'altexchange'})

message = 'Hello this is my first message'

channel.basic_publish(exchange='mainexchange', routing_key='test', body=message)

print(f'sent message: {message}')

connection.close()