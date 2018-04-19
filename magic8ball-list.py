# Magic 8 Ball with Lists

import random

messages =[
    'It is certain',
    'It is decidedly so',
    'Yes definitly',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very Doubtful']
print(messages[random.randint(0, len(messages)-1)])
