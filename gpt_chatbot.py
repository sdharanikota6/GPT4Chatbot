import mysql.connector
import json

with open('config.json', 'r') as file:
    login = json.load(file)

mydb = mysql.connector.connect(
    host=login['host'],
    user=login['user'],
    password=login['password'],
    port=login['port']
)

conversation_history = []

while True:
    cursor = mydb.cursor()
    print("\nEnter your prompt for the chatbot")
    text = input()

    conversation_history.append(text)

    conversation_input = '\n'.join(conversation_history)

    cursor.execute(
        '''SELECT response from mindsdb.smartbutdumb_model WHERE author_username = "" AND text="%s"''' % (conversation_input,))

    for x in cursor:
        print(x)
