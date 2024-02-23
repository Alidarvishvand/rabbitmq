import pika
import time
credentials = pika.PlainCredentials('ali','ali')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='logs',exchange_type='fanout')
ch.basic_publish(exchange='logs',routing_key='', body='FANOUT..!')
    # ,properties=pika.BasicProperties(
    # content_type='text/plain',
    # content_encoding ='gzip',
    # timestamp=100000,
    # expiration=str(time.time()),
    # delivery_mode=2,
    # user_id="10",
    # app_id="11",
    # type="exch.queue",
    # headers={"name": "ali", "age":"23"},
    
print('message sent to')

connection.close()

