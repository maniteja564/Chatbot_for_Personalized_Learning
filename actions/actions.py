# This file contains your custom actions to implement personalized learning.

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

# Custom action to fetch educational resources
class ActionProvideEducationalResources(Action):

    def name(self) -> Text:
        return "action_provide_educational_resources"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the topic from the user's input
        topic = tracker.get_slot("topic")
        if not topic:
            dispatcher.utter_message(text="Could you please specify the topic you'd like to learn about?")
            return []

        # Sample educational resources URLs
        urls = {
            "geeksforgeeks": f"https://www.geeksforgeeks.org/search/?q={topic}",
            "tutorialspoint": f"https://www.tutorialspoint.com/index.htm?q={topic}",
            "youtube": f"https://www.youtube.com/results?search_query={topic}"
        }

        # Construct the response
        response_message = f"Here are some resources for learning about **{topic}**:\n\n"
        response_message += f"- [GeeksforGeeks]({urls['geeksforgeeks']})\n"
        response_message += f"- [TutorialsPoint]({urls['tutorialspoint']})\n"
        response_message += f"- [YouTube]({urls['youtube']})\n"
        response_message += "\nI hope these resources help you with your learning!"

        # Send the response back to the user
        dispatcher.utter_message(text=response_message)
        return []

# Custom action to capture feedback for iterative improvements
class ActionCollectUserFeedback(Action):

    def name(self) -> Text:
        return "action_collect_user_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Ask the user for feedback
        dispatcher.utter_message(text="I hope the resources were helpful! Do you have any feedback or suggestions to improve this bot?")
        return []
