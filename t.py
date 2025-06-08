import nltk
nltk.download('punkt')
from nltk.chat.util import Chat, reflections

# Sample pairs for pattern matching
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created with NLTK.",]
    ],
    [
        r"how are you ?",
        ["I am doing great!", "I am fine, thank you!",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries.", "No problem!",]
    ],
    [
        r"quit",
        ["Bye, have a nice day!", "See you soon!",]
    ],
    [
        r"(.*)",
        ["I am not sure I understand. Can you rephrase?",]
    ],
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi! I'm your chatbot. Type 'quit' to exit.")
chatbot.converse()
