import pika
import uuid

credential = pika.PlainCredentials('ali','ali')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credential))

ch = connection.channel()

ch.queue_declare(queue='request-queue')


def request_message_received(ch,method,properties,body):
    print(f'resived request:{properties.correlation_id}')

    ch.basic_publish('',routing_key = properties.reply_to,body = f'reply to {properties.correlation_id}')

ch.basic_consume(queue='request-queue',auto_ack=True,on_message_callback=request_message_received)
print('strating server :)')
ch.start_consuming()