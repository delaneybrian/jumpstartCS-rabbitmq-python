import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare('headersexchamge', ExchangeType.headers)

message = 'This message will be sent with headers'


channel.basic_publish(
    exchange='headersexchamge', 
    routing_key='', 
    body=message, 
    properties=pika.BasicProperties(headers={'name': 'brian'}))

print(f'sent message: {message}')

connection.close()