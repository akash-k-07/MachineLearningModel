from typing import Any, Text, Dict, List
from random import choice
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class CustomAction(Action):
    def name(self) -> Text:
        return "custom_action_default_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("This is a custom action with default implementation.")
        return []

class ActionFAQQuizPrizes(CustomAction):
    def name(self) -> Text:
        return "action_faq_quiz_prizes"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Our quiz prizes include amazing rewards such as [describe prizes]."
        dispatcher.utter_message(response)
        return []

class ActionFAQTechnicalRequirements(CustomAction):
    def name(self) -> Text:
        return "action_faq_technical_requirements"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "To participate, you only need a device with a stable internet connection and a modern web browser."
        dispatcher.utter_message(response)
        return []

class ActionFAQParticipation(CustomAction):
    def name(self) -> Text:
        return "action_faq_participation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Participating in our quiz is easy! Just follow these steps: [provide participation steps]."
        dispatcher.utter_message(response)
        return []

class ActionFAQPrizesDelivery(CustomAction):
    def name(self) -> Text:
        return "action_faq_prizes_delivery"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "Prizes are usually delivered within [timeframe]. If you encounter any issues, please contact our support team."
        dispatcher.utter_message(response)
        return []

class ActionGreet(CustomAction):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses = [
            "Greetings! How may I be of service to you?",
        ]
        response = choice(responses)
        dispatcher.utter_message(response)
        return []

class ActionDefaultFallback(CustomAction):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        responses = [
            "I'm sorry, I didn't quite understand. Could you please rephrase or ask another question?",
            "Apologies, I couldn't catch that. Can you rephrase or ask something else?",
            "Sorry, I didn't get that. Can you please rephrase or ask a different question?",
        ]
        response = choice(responses)
        dispatcher.utter_message(response)
        return []
