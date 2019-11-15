from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa.core.events import SlotSet
from rasa_sdk.events import AllSlotsReset, Restarted
from rasa_sdk import Action, Tracker, ActionExecutionRejection
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    FollowupAction,
    Form,
)
import json
import pandas as pd
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process
import time
import smtplib 
from typing import Dict, Text, Any, List, Union, Optional
#faq_data=pd.read_csv('./data/FAQ_Data.csv')
csir_data=pd.read_csv('./data/csirugcdata.csv')
jee_data=pd.read_csv('./data/jeedata.csv')
ugc_data=pd.read_csv('./data/ugcdata.csv')
class GetNextStep(Action):

	def name(self):
		return 'action_get_nextstep'
		
	def run(self, dispatcher, tracker, domain):

		examinations =tracker.get_slot("confirm_exam")
		print(examinations)
	
		#if examinations == "JEE-MAIN":
		if examinations == "jee - main":
				topics = tracker.get_slot("confirm_topic")
				print(topics)
				
				#if topics == "Eligibility Criteria":
				if topics == "eligibility criteria":
					print("hellos")
					dispatcher.utter_button_message("utter_criteriatype",buttons)
					print("1")
					return[UserUtteranceReverted()]
			
				#elif topics == "Important Dates" :
				elif topics == "important dates" :
					print("helloss")
					dispatcher.utter_button_message("utter_askwhichdate",buttons)
					return[UserUtteranceReverted()]
				
				#elif topics == "Center Related Query" :
				elif topics == "important dates" :
					print("helloss")
					dispatcher.utter_button_message("utter_centerquery",buttons)
					return[UserUtteranceReverted()]
				elif topics == "Fees Related Query" :
				#elif topics == "fees related query" :
					dispatcher.utter_button_message("utter_category",buttons)
					return[UserUtteranceReverted()]
				
				else:
					dispatcher.utter_button_message("utter_others",buttons)
					return[UserUtteranceReverted()]
class GetAnswer(Action):

	def __init__(self):
		#self.faq_data = faq_data
		self.csir_data =csir_data
		self.jee_data = jee_data
		self.ugc_data = ugc_data

	def name(self):
		return 'action_get_answer'
		
	def run(self, dispatcher, tracker, domain):

		examinations =tracker.get_slot("confirm_exam")
		print(examinations)
	
		if examinations == "JEE-MAIN":
		#if examinations == "jee - main":
				topics = tracker.get_slot("confirm_topic")
				print(topics)
				if topics == "Eligibility Criteria":
				#if topics == "eligibility criteria":
					print("hellos")
					criteria=tracker.get_slot("confirm_criteriatype")
					print(criteria)
					if criteria != None:
						query  = (tracker.latest_message)['text'].capitalize()
						questions = self.jee_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.jee_data.loc[self.jee_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				elif topics == "Important Dates" :
				
					print("helloss")
					date= tracker.get_slot("confirm_whichdate")
					print(date)
					if date != None:
						query  = (tracker.latest_message)['text'].capitalize()
						print(query)
						questions = self.jee_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.jee_data.loc[self.jee_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				elif topics == "Fees Related Query" :
				#elif topics == "fees related query" :
					print("hellosss")
					categories = tracker.get_slot("confirm_category")
					print(categories)
					gender= tracker.get_slot("confirm_gender")
					print(gender)
					if categories != None and gender != None:
					#dispatcher.utter_template("utter_askwhichdate",tracker)
						query  = "fees of {} in {} ".format( gender , categories)
						print(query)
						questions = self.jee_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.jee_data.loc[self.jee_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				elif topics == "Center Related Query" :
					print("hellosss")
					center = tracker.get_slot("confirm_centerquery")
					print(center)
					if center != None:
					#dispatcher.utter_template("utter_askwhichdate",tracker)
						#query  = "fees of {} in {} ".format( gender , categories)
						query  = (tracker.latest_message)['text'].capitalize()
						print(query)
						questions = self.jee_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.jee_data.loc[self.jee_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				else:
					print("hellosssss")
					other = tracker.get_slot("confirm_otherstopics")
					print(other)
					if other == "Exam Related Queries":
						examquery = tracker.get_slot("confirm_examquery")
						print(examquery)
						questions = self.jee_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(examquery, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 90: 
							matched_row = self.jee_data.loc[self.jee_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "Application Form Related":
						appquery = tracker.get_slot("confirm_appqueries")
						print(appquery)
						questions = self.jee_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(appquery, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.jee_data.loc[self.jee_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "Payment/Fees Related":
						paymentqueries = tracker.get_slot("confirm_paymentqueries")
						print(paymentqueries)
						questions = self.jee_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(paymentqueries, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.jee_data.loc[self.jee_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "General FAQs":
						generalfaqs = tracker.get_slot("confirm_generalfaqs")
						print(generalfaqs)
						questions = self.jee_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(generalfaqs, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.jee_data.loc[self.jee_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "Certificates Related":
						certificatequeries = tracker.get_slot("confirm_certificatequeries")
						print(certificatequeries)
						questions = self.jee_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(certificatequeries, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.jee_data.loc[self.jee_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]

		elif examinations == "UGC-NET":
		#if examinations == "jee - main":
				topics = tracker.get_slot("confirm_topic")
				print(topics)
				if topics == "Eligibility Criteria":
				#if topics == "eligibility criteria":
					print("hellos")
					criteria=tracker.get_slot("confirm_criteriatype")
					print(criteria)
					if criteria != None:
						query  = (tracker.latest_message)['text'].capitalize()
						questions = self.ugc_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.ugc_data.loc[self.ugc_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				elif topics == "Important Dates" :
				#elif topics == "important dates" :
					print("helloss")
					date= tracker.get_slot("confirm_whichdate")
					print(date)
					if date != None:
						query  = (tracker.latest_message)['text'].capitalize()
						print(query)
						questions = self.ugc_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.ugc_data.loc[self.ugc_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				elif topics == "Fees Related Query" :
				#elif topics == "fees related query" :
					print("hellosss")
					categories = tracker.get_slot("confirm_category")
					print(categories)
					gender= tracker.get_slot("confirm_gender")
					print(gender)
					if categories != None and gender != None:
					#dispatcher.utter_template("utter_askwhichdate",tracker)
						query  = "fees of {} in {} ".format( gender , categories)
						print(query)
						questions = self.ugc_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.ugc_data.loc[self.ugc_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				elif topics == "Center Related Query" :
					print("hellosss")
					center = tracker.get_slot("confirm_centerquery")
					print(center)
					if center != None:
					#dispatcher.utter_template("utter_askwhichdate",tracker)
						#query  = "fees of {} in {} ".format( gender , categories)
						query  = (tracker.latest_message)['text'].capitalize()
						print(query)
						questions = self.ugc_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.ugc_data.loc[self.ugc_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				else:
					print("hellosssss")
					other = tracker.get_slot("confirm_otherstopics")
					print(other)
					if other == "Exam Related Queries":
						examquery = tracker.get_slot("confirm_examquery")
						print(examquery)
						questions = self.ugc_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(examquery, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 90: 
							matched_row = self.ugc_data.loc[self.ugc_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "Application Form Related":
						appquery = tracker.get_slot("confirm_appqueries")
						print(appquery)
						questions = self.ugc_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(appquery, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.ugc_data.loc[self.ugc_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "Payment/Fees Related":
						paymentqueries = tracker.get_slot("confirm_paymentqueries")
						print(paymentqueries)
						questions = self.ugc_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(paymentqueries, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.ugc_data.loc[self.ugc_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "General FAQs":
						generalfaqs = tracker.get_slot("confirm_generalfaqs")
						print(generalfaqs)
						questions = self.ugc_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(generalfaqs, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.ugc_data.loc[self.ugc_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "Certificates Related":
						certificatequeries = tracker.get_slot("confirm_certificatequeries")
						print(certificatequeries)
						questions = self.ugc_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(certificatequeries, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.ugc_data.loc[self.ugc_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]

		#elif examinations == "csir ugc - net" :
		elif examinations == "CSIR UGC-NET" :
				topics = tracker.get_slot("confirm_topic")
				print(topics)
				if topics == "Eligibility Criteria":
				#if topics == "eligibility criteria":
					print("hellos")
					criteria=tracker.get_slot("confirm_criteriatype")
					print(criteria)
					if criteria != None:
						query  = (tracker.latest_message)['text'].capitalize()
						questions = self.csir_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.csir_data.loc[self.csir_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				elif topics == "Important Dates" :
				#elif topics == "important dates" :
					print("helloss")
					date= tracker.get_slot("confirm_whichdate")
					print(date)
					if date != None:
						query  = (tracker.latest_message)['text'].capitalize()
						print(query)
						questions = self.csir_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.csir_data.loc[self.csir_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				elif topics == "Fees Related Query" :
				#elif topics == "fees related query" :
					print("hellosss")
					categories = tracker.get_slot("confirm_category")
					print(categories)
					gender= tracker.get_slot("confirm_gender")
					print(gender)
					if categories != None and gender != None:
					#dispatcher.utter_template("utter_askwhichdate",tracker)
						query  = "fees of {} in {} ".format( gender , categories)
						print(query)
						questions = self.csir_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.csir_data.loc[self.csir_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				elif topics == "Center Related Query" :
					print("hellosss")
					center = tracker.get_slot("confirm_centerquery")
					print(center)
					if center != None:

						query  = (tracker.latest_message)['text'].capitalize()
						print(query)
						questions = self.csir_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(query, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						#print(matched_question)
						if score > 70: 
							matched_row = self.csir_data.loc[self.csir_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
				else:
					print("hellosssss")
					other = tracker.get_slot("confirm_otherstopics")
					print(other)
					if other == "Exam Related Queries":
						examquery = tracker.get_slot("confirm_examquery")
						print(examquery)
						questions = self.csir_data['question'].values.tolist()
						matched_question, score = process.extractOne(examquery, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 90: 
							matched_row = self.csir_data.loc[self.csir_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "Application Form Related":
						appquery = tracker.get_slot("confirm_appqueries")
						print(appquery)
						questions = self.csir_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(appquery, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.csir_data.loc[self.csir_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "Payment/Fees Related":
						paymentqueries = tracker.get_slot("confirm_paymentqueries")
						print(paymentqueries)
						questions = self.csir_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(paymentqueries, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.csir_data.loc[self.csir_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "General FAQs":
						generalfaqs = tracker.get_slot("confirm_generalfaqs")
						print(generalfaqs)
						questions = self.csir_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(generalfaqs, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.csir_data.loc[self.csir_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
					elif other == "Certificates Related":
						certificatequeries = tracker.get_slot("confirm_certificatequeries")
						print(certificatequeries)
						questions = self.csir_data['question'].values.tolist()
						#print(questions)
						matched_question, score = process.extractOne(certificatequeries, questions, scorer=fuzz.token_set_ratio) # use process.extract(.. limits = 3) to get multiple close matches
						if score > 70: 
							matched_row = self.csir_data.loc[self.csir_data['question'] == matched_question,]
							answer = matched_row['answer'].values[0]
							response =  "{} \n".format( answer)
							dispatcher.utter_message(response)
							return[SlotSet('action_response',True)]
						else:
							response = "Sorry I couldn't find anything relevant to your query!"
							dispatcher.utter_message(response)
							return[SlotSet('action_response',False)]
		else:
				dispatcher.utter_message("Sorry")

class GetName(Action):
	def name(self):
		return 'action_get_name'
	def run(self,dispatcher,tracker,domain):
		feedback = tracker.get_slot("confirm_feedback")
		print("hello")
		print(feedback)
		#if response == "no 👎":
		if feedback == "Not Satisfied":
			name= next(tracker.get_latest_entity_values("person"), None)
			if not name:
				dispatcher.utter_template("utter_name",tracker)
				UserUtteranceReverted()
				#return [UserUtteranceReverted()]
				
			return [SlotSet('person',name)]	
		else:
			dispatcher.utter_template("utter_goodbye",tracker)
			return[Restarted()]

class GetEmail(Action):
	def name(self):
		return 'action_get_email'
	def run(self,dispatcher,tracker,domain):
		userdata={}
		name= next(tracker.get_latest_entity_values("person"), None)
		userdata['name']={'name':name}
		with open('userdata.json','w') as f:
			json.dump(userdata, f)
		#dispatcher.utter_message(name)
		email= next(tracker.get_latest_entity_values("email"), None)
		if not email:
			dispatcher.utter_template("utter_email",tracker)
			return [UserUtteranceReverted()]

		return [SlotSet('email',email)]	

class GetContact(Action):
	def name(self):
		return 'action_get_contact'
	def run(self,dispatcher,tracker,domain):
		user_data={}
		email=next(tracker.get_latest_entity_values("email"), None)
		user_data['email']={'email':email}
		with open('user_data.json','w') as f:
			json.dump(user_data, f)
		#dispatcher.utter_message(email)
		contact= next(tracker.get_latest_entity_values("contact"), None)
		if not contact:
			dispatcher.utter_template("utter_contact_number",tracker)
			return [UserUtteranceReverted()]
		return [SlotSet('contact',contact)]
class SendEmail(Action):
	def name(self):
		return 'action_send_email'
	def run(self,dispatcher,tracker,domain):
		contact=tracker.get_slot("contact")
		if contact is not None:
			
	
					with open('userdata.json','r') as tf:
						data = json.load(tf)
						username=data["name"]["name"]
					with open('user_data.json','r') as g:
						data = json.load(g)
						useremail=data["email"]["email"]
		
		
					dispatcher.utter_template("utter_feedbackresponse",tracker)
					s = smtplib.SMTP('smtp.gmail.com', 587) 
			  			
						# start TLS for security 
					s.starttls() 
						  
						# Authentication 
					s.login("developers.absolvetech@gmail.com", "Absolve@Tech19##") 
						  
						# message to be sent 
					message = " DATA: {}\n\n{}\n\n{}".format(username,contact,useremail)
						
						# sending the mail 
					s.sendmail("developers.absolvetech@gmail.com", "shivani.python@outlook.com", message) 
						  
						# terminating the session 
					s.quit()
		return[Restarted()]


class ActionGoodBye(Action):
	def name(self):
		return 'action_bye'
		
	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_template("utter_goodbye",tracker)
		return[Restarted()]

class ActionRestarted(Action): 	
    def name(self): 		
        return 'action_restarted' 	
    def run(self, dispatcher, tracker, domain): 
        return[Restarted()]
		
class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]
