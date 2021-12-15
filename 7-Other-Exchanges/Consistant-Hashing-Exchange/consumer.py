import pika

def queue_1_on_message_received(ch, method, properties, body):
    print(f'queue 1 received new message: {body}')

def queue_2_on_message_received(ch, method, properties, body):
    print(f'queue 2 received new message: {body}')

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare('samplehashing', 'x-consistent-hash') 

channel.queue_declare(queue='letterbox1')
channel.queue_declare(queue='letterbox2')

channel.queue_bind('letterbox1', 'samplehashing', routing_key='1')
channel.basic_consume(queue='letterbox1', auto_ack=True,
    on_message_callback=queue_1_on_message_received)

channel.queue_bind('letterbox2', 'samplehashing', routing_key='1')
channel.basic_consume(queue='letterbox2', auto_ack=True,
    on_message_callback=queue_2_on_message_received)

print('Starting Consuming')

channel.start_consuming()