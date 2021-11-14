import pika
import uuid

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='request_queue')

reply_queue = channel.queue_declare(queue='', exclusive=True)

correlation_id = str(uuid.uuid4())

message = "This Message needs a response"

channel.basic_publish(exchange='', routing_key='request_queue',
            properties=pika.BasicProperties(
                reply_to=reply_queue.method.queue,
                correlation_id=correlation_id,
            ),
            body=message)

print(f"sent : {correlation_id} : {message}")

def on_message_received(ch, method, properties, body):
    print(f"received: {properties.correlation_id} : {body}")

channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True,
    on_message_callback=on_message_received)

print("Client Starting Consuming")

channel.start_consuming()

connection.close()