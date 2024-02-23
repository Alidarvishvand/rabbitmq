import pika


credential = pika.PlainCredentials('ali','ali')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credential))

ch = connection.channel()

ch.exchange_declare(exchange='alt',exchange_type='fanin')
ch.exchange_declare(exchange='main',exchange_type='direct',arguments={'alternate0-exchange':'alt'})

ch.queue_declare(queue='altq')
ch.queue_bind('altq', 'alt')

ch.queue_declare(queue='mainq')
ch.queue_bind('mainq', 'main','home')




def alt_callback(ch,method,properties,body):
    print(f'ALT :{body}')



def main_callback(ch,method,properties,body):
    print(f'Main :{body}')




ch.basic_consume(queue='altq',on_message_callback=alt_callback,auto_ack=True)
ch.basic_consume(queue='mainq',on_message_callback=main_callback,auto_ack=True)
print('start cosuming')
ch.start_consuming() 