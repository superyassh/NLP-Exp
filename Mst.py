from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("ChatBot")

trainer = ListTrainer(chatbot)
trainer.train([
'Hi',
'Hello',]), 
trainer.train([
'How was your day?',
'How everything going?',
]),
trainer.train([
"Yes, I need water",
"I need soil",
])

exit_conditions = ("exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f">> {chatbot.get_response(query)}")