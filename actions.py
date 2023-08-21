# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# from typing import Any, Text, Dict, List
# # import arrow 
# # import dateparser
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher
import psycopg2


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
    
    
connection=psycopg2.connect(user="postgres",

                            password="root@123",

                            host="localhost",

                            port="5432",

                            database="NMS")



cursor=connection.cursor()

cursor.execute("CREATE TABLE Alarm(ACK BOOLEAN,severity TEXT, nodeName TEXT, nodeId TEXT)")

cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("1","Major","AF","1"))

cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("0","Critical","AMF","2"))

cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("1","Major","PCF","3"))

cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("0","Minor","UPF","4"))

cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("1","Major","SMF","5"))

cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("1","Cleared","UE","6"))

cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("0","Critical","gnb","7"))

cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("1","Minor","NWDAF","8"))

cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("0","Critical","NEF","9"))

cursor.execute("INSERT INTO Alarm(ACK,severity,nodeName, nodeId) VALUES (%s,%s,%s,%s)",("1","Cleared","NSSAAF","10"))





class ActionNonACKMinorAlarms(Action):
    
    def name(self) -> Text:
        return "action_NonACK_Minor_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("UPDATE Alarm SET ACK='0' WHERE severity='Minor'")
        cursor.execute("SELECT *FROM Alarm WHERE severity='Minor'")
    
        NonACK_Minor_alarms=cursor.fetchall()
        
        if NonACK_Minor_alarms:
            alarms_description = NonACK_Minor_alarms
            dispatcher.utter_message(text=f"NonACKed Minor Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No NonACKed Minor alarms found for you.")

        return []


class ActionNonACKMajorAlarms(Action):
    
    def name(self) -> Text:
        return "action_NonACK_Major_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("UPDATE Alarm SET ACK='0' WHERE severity='Major'")
        cursor.execute("SELECT *FROM Alarm WHERE severity='Major'")
    
        NonACK_Major_alarms=cursor.fetchall()
        
        if NonACK_Major_alarms:
            alarms_description = NonACK_Major_alarms
            dispatcher.utter_message(text=f"NonACKed Major Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text=f"NonACKed Major alarms found for you.")

        return []

class ActionNonACKCriticalAlarms(Action):
    
    def name(self) -> Text:
        return "action_NonACK_Critical_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("UPDATE Alarm SET ACK='0' WHERE severity='Critical'")
        cursor.execute("SELECT *FROM Alarm WHERE severity='Critical'")
    
        NonACK_Critical_alarms=cursor.fetchall()
        
        if NonACK_Critical_alarms:
            alarms_description = NonACK_Critical_alarms
            dispatcher.utter_message(text=f"NonACKed Critical Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No NonACKed Critical alarms found for you.")

        return []





class ActionNonACKClearedAlarms(Action):
    
    def name(self) -> Text:
        return "action_NonACK_Cleared_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("UPDATE Alarm SET ACK='0' WHERE severity='Cleared'")
        cursor.execute("SELECT *FROM Alarm WHERE severity='Cleared'")
    
        NonACK_Cleared_alarms=cursor.fetchall()
        
        if NonACK_Cleared_alarms:
            alarms_description = NonACK_Cleared_alarms
            dispatcher.utter_message(text=f"NonACKed Cleared Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No NonACKed Cleared alarms found for you.")

        return []





class ActionACKMinorAlarms(Action):
    
    def name(self) -> Text:
        return "action_ACK_Minor_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("UPDATE Alarm SET ACK='1' WHERE severity='Minor'")
        cursor.execute("SELECT *FROM Alarm WHERE severity='Minor'")
    
        ACK_Minor_alarms=cursor.fetchall()
        
        if ACK_Minor_alarms:
            alarms_description = ACK_Minor_alarms
            dispatcher.utter_message(text=f"ACKed Minor Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No ACKed Minor alarms found for you.")

        return []


class ActionACKMajorAlarms(Action):
    
    def name(self) -> Text:
        return "action_ACK_Major_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("UPDATE Alarm SET ACK='1' WHERE severity='Major'")
        cursor.execute("SELECT *FROM Alarm WHERE severity='Major'")
    
        ACK_Major_alarms=cursor.fetchall()
        
        if ACK_Major_alarms:
            alarms_description = ACK_Major_alarms
            dispatcher.utter_message(text=f"ACKed Major Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text=f"ACKed Major alarms found for you.")

        return []

class ActionACKCriticalAlarms(Action):
    
    def name(self) -> Text:
        return "action_ACK_Critical_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("UPDATE Alarm SET ACK='1' WHERE severity='Critical'")
        cursor.execute("SELECT *FROM Alarm WHERE severity='Critical'")
    
        ACK_Critical_alarms=cursor.fetchall()
        
        if ACK_Critical_alarms:
            alarms_description = ACK_Critical_alarms
            dispatcher.utter_message(text=f"ACKed Critical Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No ACKed Critical alarms found for you.")

        return []





class ActionACKClearedAlarms(Action):
    
    def name(self) -> Text:
        return "action_ACK_Cleared_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("UPDATE Alarm SET ACK='1' WHERE severity='Cleared'")
        cursor.execute("SELECT *FROM Alarm WHERE severity='Cleared'")
    
        ACK_Cleared_alarms=cursor.fetchall()
        
        if ACK_Cleared_alarms:
            alarms_description = ACK_Cleared_alarms
            dispatcher.utter_message(text=f"ACKed Cleared Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No ACKed Cleared alarms found for you.")

        return []



class ActionShowNonACKMinorAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_NonACK_Minor_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Minor' AND ACK=false")
        NonACK_Minor_alarms=cursor.fetchall()
        
        if NonACK_Minor_alarms:
            alarms_description = NonACK_Minor_alarms
            dispatcher.utter_message(text=f"NonACKed Minor Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No NonACKed Minor alarms found for you.")

        return []


class ActionShowNonACKMajorAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_NonACK_Major_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Major' AND ACK=false")
        NonACK_Major_alarms=cursor.fetchall()
        
        if NonACK_Major_alarms:
            alarms_description = NonACK_Major_alarms
            dispatcher.utter_message(text=f"NonACKed Major Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No NonACKed Major alarms found for you.")

        return []


class ActionShowNonACKCriticalAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_NonACK_Critical_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Critical' AND ACK=false")
        NonACK_Critical_alarms=cursor.fetchall()
        
        if NonACK_Critical_alarms:
            alarms_description = NonACK_Critical_alarms
            dispatcher.utter_message(text=f"NonACKed Critical Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No NonACKed Critical alarms found for you.")

        return []






class ActionShowNonACKClearedAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_NonACK_Cleared_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Cleared' AND ACK=false")
        NonACK_Cleared_alarms=cursor.fetchall()
        
        if NonACK_Cleared_alarms:
            alarms_description = NonACK_Cleared_alarms
            dispatcher.utter_message(text=f"NonACKed Cleared Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No NonACKed Cleared alarms found for you.")

        return []




class ActionShowACKMinorAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_ACK_Minor_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Minor' AND ACK=true")
        ACK_Minor_alarms=cursor.fetchall()
        
        if ACK_Minor_alarms:
            alarms_description = ACK_Minor_alarms
            dispatcher.utter_message(text=f"ACKed Minor Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No ACKed Minor alarms found for you.")

        return []


class ActionShowACKMajorAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_ACK_Major_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Major' AND ACK=true")
        ACK_Major_alarms=cursor.fetchall()
        
        if ACK_Major_alarms:
            alarms_description = ACK_Major_alarms
            dispatcher.utter_message(text=f"ACKed Major Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No ACKed Major alarms found for you.")

        return []


class ActionShowACKCriticalAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_ACK_Critical_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Critical' AND ACK=true")
        ACK_Critical_alarms=cursor.fetchall()
        
        if ACK_Critical_alarms:
            alarms_description = ACK_Critical_alarms
            dispatcher.utter_message(text=f"ACKed Critical Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No ACKed Critical alarms found for you.")

        return []






class ActionShowACKClearedAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_ACK_Cleared_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Cleared' AND ACK=true")
        ACK_Cleared_alarms=cursor.fetchall()
        
        if ACK_Cleared_alarms:
            alarms_description = ACK_Cleared_alarms
            dispatcher.utter_message(text=f"ACKed Cleared Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No ACKed Cleared alarms found for you.")

        return []




class ActionShowClearedAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_cleared_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Cleared'")
        cleared_alarms=cursor.fetchall()
        
        if cleared_alarms:
            alarms_description = cleared_alarms
            dispatcher.utter_message(text=f"Cleared Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No cleared alarms found for you.")

        return []


class ActionShowCriticalAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_critical_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Critical'")
        critical_alarms=cursor.fetchall()
        
        if critical_alarms:
            alarms_description = critical_alarms
            dispatcher.utter_message(text=f"Critical Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No critical alarms found for you.")

        return []


class ActionShowMinorAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_minor_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Minor'")
        minor_alarms=cursor.fetchall()
        
        if minor_alarms:
            alarms_description = minor_alarms
            dispatcher.utter_message(text=f"Minor Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No minor alarms found for you.")

        return []


class ActionShowMajorAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_major_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm WHERE severity='Major'")
        major_alarms=cursor.fetchall()
        
        if major_alarms:
            alarms_description = major_alarms
            dispatcher.utter_message(text=f"Major Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No major alarms found for you.")

        return []

class ActionShowAlarms(Action):
    
    def name(self) -> Text:
        return "action_show_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT *FROM Alarm")
        all_alarm=cursor.fetchall()
        
        if all_alarm:
            alarms_description = all_alarm
            dispatcher.utter_message(text=f"Alarms: {alarms_description}")
        else:
            dispatcher.utter_message(text="No alarms found for you.")

        return []

class ActionTotalOnlineDevice(Action):
    
    def name(self) -> Text:
        return "action_total_online_device"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT COUNT(nodeId) FROM Alarm WHERE ACK ='1' ")
        cnt_online_node=cursor.fetchone()[0]
        
        if cnt_online_node:
            device_description = cnt_online_node
            dispatcher.utter_message(text=f"Total number of online device: {device_description}")
        else:
            dispatcher.utter_message(text="No device is online found for you.")

        return []
        

class ActionTotalOfflineDevice(Action):
    
    def name(self) -> Text:
        return "action_total_offline_device"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cursor.execute("SELECT COUNT(nodeId) FROM Alarm WHERE ACK ='0' ")
        cnt_online_node=cursor.fetchone()[0]
        
        if cnt_online_node:
            device_description = cnt_online_node
            dispatcher.utter_message(text=f"Total number of offline device: {device_description}")
        else:
            dispatcher.utter_message(text="No device is offline found for you.")

        return []
        















