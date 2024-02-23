import pika
import time




credentials = pika.PlainCredentials('ali','ali')
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost',credentials=credentials))
ch = connection.channel()



# def callback1(ch,method,properties,body):
#     print(f'receiver{body}')
#     print(method)
#     time.sleep(5)
#     print("done!")
#     ch.basic_ack(delivery_tag=method.delivery_tag)
#     # print(properties.headers)
# ch.basic_qos(prefetch_count=1)
# ch.basic_consume(queue='one', on_message_callback=callback1)
# print('waiting for message, ')
# ch.start_consuming()

ch.exchange_declare(exchange='logs',exchange_type='fanout')
result = ch.queue_declare(queue='',exclusive=True)
ch.queue_bind(exchange='logs',queue= result.method.queue)

print('waiting for logs...')
print(result.method.queue)


def callback(ch,method,properties, body):
    print(f'receiver{body}')


ch.basic_consume(queue=result.method.queue , on_message_callback=callback  ,auto_ack=True)
ch.start_consuming()
