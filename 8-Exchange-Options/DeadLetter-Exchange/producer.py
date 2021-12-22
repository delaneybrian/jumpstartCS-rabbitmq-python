import pika
from pika.exchange_type import ExchangeType
from pika.spec import BasicProperties

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct)

message = 'This message might expire'

channel.basic_publish(
    exchange='mainexchange', 
    routing_key='test',
    body=message)

print(f'sent message: {message}')

connection.close() 