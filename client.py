import pika
import uuid

credential = pika.PlainCredentials('ali','ali')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credential))

ch = connection.channel()

reply_queue = ch.queue_declare(queue='',exclusive=True)

def reply_message_receive(ch,method,properties,body):
    print(f'replay to :{body}')

ch.basic_consume(queue=reply_queue.method.queue,auto_ack=True,on_message_callback=reply_message_receive)
ch.queue_declare(queue='request-queue')
cor_id = str(uuid.uuid4())

print(f'sending request to :{cor_id}')

ch.basic_publish('',routing_key='request-queue',properties=pika.BasicProperties(
    reply_to=reply_queue.method.queue,
    correlation_id=cor_id),
    body =  'can i request a replaye?'
)

print('startin client..!')
ch.start_consuming()