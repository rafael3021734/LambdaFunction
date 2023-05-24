# arquivo s3_sqs_consumer.py
import json
import io
import logging
import boto3

# configura um logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# obtem um cliente para integrar com servico SQS, e a URL da fila
#sqs = boto3.client('sqs', endpoint_url='http://192.168.99.100:4566/000000000000/teste')
sqs = boto3.client('sqs', endpoint_url='http://192.168.99.100:4566')

#queue = sqs.get_queue_url(QueueName='FILA_S3')
queue_url = 'http://192.168.99.100:4566/000000000000/minha-fila'
message_body = 'Olá, LocalStack!'
response = sqs.send_message(QueueUrl= queue_url, MessageBody=message_body)
print(response)

response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
messages = response.get('Messages', [])
logging.info(f'Mensagem recebida')
for message in messages:
    message_body = message['Body']
    receipt_handle = message['ReceiptHandle']

    # Faça o processamento da mensagem
    print('Mensagem recebida:', message_body)
    logging.info(f'Mensagem [{message["MessageId"]}] recebida')

    # Exclua a mensagem da fila
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)

# obtem um cliente para integrar com servico S3
s3 = boto3.client('s3', endpoint_url='http://192.168.99.100:4566')