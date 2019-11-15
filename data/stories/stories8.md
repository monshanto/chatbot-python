
## Generated Story -1558016695801932919
* greet
    - utter_greet
    - utter_query
* affirm{"affirm": "Yes"}
    - utter_ask_exam
* confirm_exam{"confirm_exam": "JEE-MAIN"}
    - slot{"confirm_exam": "JEE-MAIN"}
    - utter_querytopic
* confirm_topic{"confirm_topic": "Others"}
    - slot{"confirm_topic": "Others"}
    - utter_others
* confirm_otherstopics{"confirm_otherstopics": "Certificates Related"}
    - slot{"confirm_otherstopics": "Certificates Related"}
    - utter_certificatequeries
* confirm_certificatequeries{"confirm_certificatequeries": "Certificates required during submission"}
    - slot{"confirm_certificatequeries": "Certificates required during submission"}
    - action_get_answer
    - slot{"action_response": true}
    - utter_other_query
* deny{"deny": "No"}
    - utter_feedback
* confirm_feedback{"confirm_feedback": "Satisfied "}
    - slot{"confirm_feedback": "Satisfied "}
    - action_get_name

## Generated Story 4732412903635165457
* greet
    - utter_greet
    - utter_query
* affirm{"affirm": "Yes"}
    - utter_ask_exam
* confirm_exam{"confirm_exam": "JEE-MAIN"}
    - slot{"confirm_exam": "JEE-MAIN"}
    - utter_querytopic
* confirm_topic{"confirm_topic": "Others"}
    - slot{"confirm_topic": "Others"}
    - utter_others
* confirm_otherstopics{"confirm_otherstopics": "Certificates Related"}
    - slot{"confirm_otherstopics": "Certificates Related"}
    - utter_certificatequeries
* confirm_certificatequeries{"confirm_certificatequeries": "Certificates required during submission"}
    - slot{"confirm_certificatequeries": "Certificates required during submission"}
    - action_get_answer
    - slot{"action_response": true}
    - utter_other_query
* deny{"deny": "No"}
    - utter_feedback
* confirm_feedback{"confirm_feedback": "Satisfied "}
    - slot{"confirm_feedback": "Satisfied "}
    - action_get_name
