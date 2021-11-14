import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='request_queue')

def on_message_received(ch, method, properties, body):

    print(f"recieved : {properties.correlation_id} : {body}")

    response_message = "This is the response message"

    channel.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                     body=response_message)

    print(f"sent : {properties.correlation_id} : {response_message}")

channel.basic_consume(queue='request_queue', auto_ack=True,
    on_message_callback=on_message_received)

print("Server Starting Consuming")

channel.start_consuming()

connection.close()