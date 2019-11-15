
## Generated Story -4978779513798786675
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
* confirm_otherstopics{"confirm_otherstopics": "Payment/Fees Related"}
    - slot{"confirm_otherstopics": "Payment/Fees Related"}
    - utter_paymentqueries
* confirm_paymentqueries{"confirm_paymentqueries": "Refund of Money if transaction done multiple times"}
    - slot{"confirm_paymentqueries": "Refund of Money if transaction done multiple times"}
    - action_get_answer
    - slot{"action_response": true}
    - utter_other_query
* deny{"deny": "No"}
    - utter_feedback
* confirm_feedback{"confirm_feedback": "Satisfied "}
    - slot{"confirm_feedback": "Satisfied "}
    - action_get_name

## Generated Story 1793763871711038308
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
* confirm_otherstopics{"confirm_otherstopics": "Payment/Fees Related"}
    - slot{"confirm_otherstopics": "Payment/Fees Related"}
    - utter_paymentqueries
* confirm_paymentqueries{"confirm_paymentqueries": "Refund of money if Question challenged found correct"}
    - slot{"confirm_paymentqueries": "Refund of money if Question challenged found correct"}
    - action_get_answer
    - slot{"action_response": true}
    - utter_other_query
* deny{"deny": "No"}
    - utter_feedback
* confirm_feedback{"confirm_feedback": "Satisfied"}
    - slot{"confirm_feedback": "Satisfied"}
    - action_get_name
