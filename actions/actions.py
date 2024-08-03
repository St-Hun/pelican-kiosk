from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import Restarted, EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from sanic import Sanic, response

from main import Dose_Availability_District, Dose_Availability_Pincode, Dose_Availability_Lon_Lat, send_email

# Sanic 앱 인스턴스 생성
app = Sanic("custom_action_app")

# 기본 경로에 대한 응답 처리
@app.route('/')
async def main(request):
    return response.json({"message": "Action server is running"})

# 파비콘 요청에 대한 응답 처리
@app.route('/favicon.ico')
async def favicon(request):
    return response.empty(status=204)

class ActionHelloWorld(Action):
    def name(self) -> str:
        return "action_hello_world"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: dict) -> list:
        dispatcher.utter_message(text="Hello World!")
        return []

class ValidatepincodeForm(FormValidationAction):
    def name(self) -> Text:
        return "slot_pincode_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        required_slots = ["pincode", "date"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot", slot_name)]

        return [SlotSet("requested_slot", None)]

class ValidateDistrictForm(FormValidationAction):
    def name(self) -> Text:
        return "slot_district_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        required_slots = ["district_id", "date"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot", slot_name)]

        return [SlotSet("requested_slot", None)]

class ValidateLocationForm(FormValidationAction):
    def name(self) -> Text:
        return "slot_location_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        required_slots = ["lattitude", "longitude"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot", slot_name)]

        return [SlotSet("requested_slot", None)]

class ActionPincodeSubmit(Action):

    def name(self) -> Text:
        return "action_pincode_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message
        message = Dose_Availability_Pincode(tracker.get_slot('pincode'), tracker.get_slot('date'))
        dispatcher.utter_message(text=message)
        buttons = [
            {'payload': "/affirm", 'title': "Yes"},
            {'payload': "/deny", 'title': "No"},
        ]
        dispatcher.utter_message(text="Would you like to get the details on your email id?", buttons=buttons)

        return []

class ActionDistrictSubmit(Action):

    def name(self) -> Text:
        return "action_district_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message
        message = Dose_Availability_District(tracker.get_slot('district_id'), tracker.get_slot('date'))
        dispatcher.utter_message(text=message)
        buttons = [
            {'payload': "/affirm", 'title': "Yes"},
            {'payload': "/deny", 'title': "No"},
        ]
        dispatcher.utter_message(text="Would you like to get the details on your email id?", buttons=buttons)

        return []

class ActionLocationSubmit(Action):

    def name(self) -> Text:
        return "action_location_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message
        message = Dose_Availability_Lon_Lat(tracker.get_slot('lattitude'), tracker.get_slot('longitude'))
        dispatcher.utter_message(text=message)
        buttons = [
            {'payload': "/affirm", 'title': "Yes"},
            {'payload': "/deny", 'title': "No"},
        ]
        dispatcher.utter_message(text="Would you like to get the details on your email id?", buttons=buttons)
        return []

class ActionSendEmail(Action):

    def name(self) -> Text:
        return "action_send_mail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        send_email(tracker.get_slot("email"), message)
        dispatcher.utter_message(text="We have successfully sent the mail to your Email ID: {}".format(tracker.get_slot("email")))

        return []

class ActionRestart(Action):

    def name(self) -> Text:
        return "action_restart"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        return [Restarted()]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
