import pika


credential = pika.PlainCredentials('ali','ali')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credential))

ch = connection.channel()


ch.exchange_declare(exchange='alt',exchange_type='fanin')
ch.exchange_declare(exchange='main',exchange_type='direct',arguments={'alternate0-exchange':'alt'})

ch.basic_publish(exchange='main',routing_key='home',body="hello world")

print('sent....!')
connection.close()