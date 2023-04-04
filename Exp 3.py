from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
"Hi",
"Welcome, friend ",
"Hello",
"Hello, How are you?", ])
trainer.train([
"How are you?",
"I'm fine, how about you?",
])
trainer.train([
"Are you a plant?",
"No, I'm the pot below the plant!",
])
trainer.train([
"Are you thristy?",
"Yes, I need water!",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")