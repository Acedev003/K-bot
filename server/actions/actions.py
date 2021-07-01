from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import time

class ActionCollegeInfo(Action):
     def __init__(self):
         self.nirf_count = 4

     def name(self) -> Text:
         return "action_college_info"

     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         dispatcher.utter_message("Karunya Institute of Technology and Sciences, a Deemed University and a Christian Minority Residential Institution is ranked among the Top 100 Institutions in NIRF Ranking for the last " + str(self.nirf_count) + " years.")
         dispatcher.utter_message("The institute is located in a sprawling 720-acre campus, amidst the green vegetation and misty mountains accommodating over 7500 students for learning and Research.")
         dispatcher.utter_message("We also have\n\n- Foreign Internship with Stipend\n- Industry Certification\n- Pre Placement Training Programs\n- Industry tie-up with Siemens, IBM, Novel, CISCO, Salzer, Jasmine InfoTech, Trident and Pneumatics, AMZ Automotive and Boeing\n-A Centre for Student Innovations, Incubation and Business start-up")
         dispatcher.utter_message("Other perks include\n\n- Industry Oriented Curriculum\n- International collaborations\n- Wi-Fi enabled Green Campus\n- Digital Library Resources")
         return []