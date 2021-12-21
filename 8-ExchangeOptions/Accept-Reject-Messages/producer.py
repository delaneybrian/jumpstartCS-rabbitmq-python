import pika
from pika.exchange_type import ExchangeType
from time import sleep

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(
    exchange='acceptrejectexchange', 
    exchange_type=ExchangeType.fanout)

message = 'Lets send this'

while True:
    channel.basic_publish(exchange='acceptrejectexchange', routing_key='samplekey', body=message)
    print(f"sent message: {message}")
    input('Press any key to continue')

