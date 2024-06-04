import random
import nltk
import re
from nltk.tokenize import word_tokenize
from fuzzywuzzy import fuzz
import logging

logging.basicConfig(level=logging.DEBUG)

responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hi there, how can I help you today"],
    "goodbye": ["Have a nice day", "Bye! Have a nice day."],
    "thank_you": ["Happy to help!", "Any time!", "My pleasure"],
    "delivery_time": ["The delivery time is within 30 minutes."],
    "order_status": ["Your order is on the way.", "Your order has been picked up!", "Your shopping assistant is currently working on your items", "Your order has been delivered!"],
    "contact_support": ["You can contact our support at support@grocery.com or call our support team at +91 999999999.", "Please call our support team at +91 999999999 or you can contact our support at support@grocery.com"],
    "chat_executive": ["Please hold on, connecting you to an executive.", "An executive will be with you shortly."]
}

keywords = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "See you later", "goodbye"],
    "thank_you": ["Thanks", "Thank you", "That's helpful", "Thank's a lot!", "helpful"],
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
    logging.debug(f"User input: {user_input}")
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    logging.debug(f"Tokens: {tokens}")
    
    if any(fuzzy_match(token, keywords["greeting"]) for token in tokens):
        response = random.choice(responses["greeting"])
        logging.debug(f"Greeting response: {response}")
        return response
    
    if any(fuzzy_match(token, keywords["goodbye"]) for token in tokens):
        response = random.choice(responses["goodbye"])
        logging.debug(f"Goodbye response: {response}")
        return response
    
    if any(fuzzy_match(token, keywords["thank_you"]) for token in tokens):
        response = random.choice(responses["thank_you"])
        logging.debug(f"Thank you response: {response}")
        return response
    
    if any(fuzzy_match(token, keywords["delivery_time"]) for token in tokens):
        response = random.choice(responses["delivery_time"])
        logging.debug(f"Delivery time response: {response}")
        return response
    
    if any(fuzzy_match(token, keywords["order_status"]) for token in tokens):
        response = random.choice(responses["order_status"])
        logging.debug(f"Order status response: {response}")
        return response
    
    if any(fuzzy_match(token, keywords["contact_support"]) for token in tokens):
        response = random.choice(responses["contact_support"])
        logging.debug(f"Contact support response: {response}")
        return response
    
    if any(fuzzy_match(token, keywords["chat_executive"]) for token in tokens):
        response = random.choice(responses["chat_executive"])
        logging.debug(f"Chat executive response: {response}")
        return response
    
    default_response = "I'm sorry, I'm not sure I understand that. Can you please rephrase?"
    logging.debug(f"Default response: {default_response}")
    return default_response
