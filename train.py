import random
import nltk
import re
from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz

# Download and append NLTK data path
# nltk.download('punkt', download_dir='./nltk_data')
# nltk.data.path.append('./nltk_data')

responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hi there, how can I help you today"],
    "goodbye": ["Have a nice day", "Bye! Have a nice day."],
    "thank_you": ["Happy to help!", "Any time!", "My pleasure"],
    "delivery_time": ["The delivery time is within 30 minutes."],
    "order_status": ["Your order is on the way.", "Your order has been picked up!", "Your shopping assistant is currently working on your items", "Your order has been delivered!"],
    "contact_support": ["You can contact our support at support@grocery.com or call our support team at +91 999999999.", "Please call our support team at +91 999999999 or you can contact our support at support@grocery.com"],
    "chat_executive": ["Please hold on, connecting you to an executive.", "An executive will be with you shortly."]
}

# keywords
keywords = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye" :["bye", "See you later", "goodbye"],
    "thank_you" : ["Thanks", "Thank you", "That's helpful", "Thank's a lot!", "helpful"],
    "delivery_time": ["delivery", "time", "when", "arrive", "expected", "receive"],
    "order_status": ["order", "status", "where", "check", "track", "tracking"],
    "contact_support": ["contact", "support", "help", "assist"],
    "chat_executive": ["executive", "chat", "talk", "speak", "representative"]
}

FUZZY_THRESHOLD = 80

def fuzzy_match(user_input, category_keywords):
    for keyword in category_keywords:
        if fuzz.partial_ratio(user_input, keyword) >= FUZZY_THRESHOLD:
            return True
    return False

def get_response(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    
    # fuzzy matching
    if any(fuzzy_match(token, keywords["greeting"]) for token in tokens):
        return random.choice(responses["greeting"])
    
    if any(fuzzy_match(token, keywords["goodbye"]) for token in tokens):
        return random.choice(responses["goodbye"])
    
    if any(fuzzy_match(token, keywords["thank_you"]) for token in tokens):
        return random.choice(responses["thank_you"])
    
    if any(fuzzy_match(token, keywords["delivery_time"]) for token in tokens):
        return random.choice(responses["delivery_time"])
    
    if any(fuzzy_match(token, keywords["order_status"]) for token in tokens):
        return random.choice(responses["order_status"])
    
    if any(fuzzy_match(token, keywords["contact_support"]) for token in tokens):
        return random.choice(responses["contact_support"])
    
    if any(fuzzy_match(token, keywords["chat_executive"]) for token in tokens):
        return random.choice(responses["chat_executive"])
    
    # if any(fuzzy_match(token, keywords["chat_executive"]) for token in tokens):
    # Initiate live chat session (integration)
    # live_chat_response = initiate_live_chat_session()
    
    # if live_chat_response:  # Successful connection
    #     return f"You are now connected with a live representative. {live_chat_response}"
    # else:
    #     return "We are currently experiencing high volume. Our chat representatives are unavailable at this moment. Please try again later."
    
    # default
    return "I'm sorry, I'm not sure I understand that. Can you please rephrase?"


