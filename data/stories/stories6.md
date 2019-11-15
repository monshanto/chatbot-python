
## Generated Story 8037753529854674050
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
* confirm_otherstopics{"confirm_otherstopics": "Application Form Related"}
    - slot{"confirm_otherstopics": "Application Form Related"}
    - utter_appqueries
* confirm_appqueries{"confirm_appqueries": "Choice of 4 Exam Cities"}
    - slot{"confirm_appqueries": "Choice of 4 Exam Cities"}
    - action_get_answer
    - slot{"action_response": true}
    - utter_other_query
* deny{"deny": "No"}
    - utter_feedback
* confirm_feedback{"confirm_feedback": "Satisfied"}
    - slot{"confirm_feedback": "Satisfied"}
    - action_get_name

## Generated Story -2168135051057887121
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
* confirm_otherstopics{"confirm_otherstopics": "Application Form Related"}
    - slot{"confirm_otherstopics": "Application Form Related"}
    - utter_appqueries
* confirm_appqueries{"confirm_appqueries": "Acceptance of Photograph without name and date"}
    - slot{"confirm_appqueries": "Acceptance of Photograph without name and date"}
    - action_get_answer
    - slot{"action_response": true}
    - utter_other_query
* deny{"deny": "No"}
    - utter_feedback
* confirm_feedback{"confirm_feedback": "Not Satisfied"}
    - slot{"confirm_feedback": "Not Satisfied"}
    - action_get_name
    - slot{"person": null}
* person_name{"person": "sanjana"}
    - slot{"person": "sanjana"}
    - action_get_email
    - rewind
* email{"email": "sanjana@gmail.com"}
    - slot{"email": "sanjana@gmail.com"}
    - action_get_contact
    - rewind
* contact{"contact": "9876543211"}
    - slot{"contact": "9876543211"}
    - action_send_email

## Generated Story 5097347457167868861
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
* confirm_otherstopics{"confirm_otherstopics": "Application Form Related"}
    - slot{"confirm_otherstopics": "Application Form Related"}
    - utter_appqueries
* confirm_appqueries{"confirm_appqueries": "Id Proofs Required"}
    - slot{"confirm_appqueries": "Id Proofs Required"}
    - action_get_answer
    - slot{"action_response": true}
    - utter_other_query
* deny{"deny": "No"}
    - utter_feedback
* confirm_feedback{"confirm_feedback": "Satisfied"}
    - slot{"confirm_feedback": "Satisfied "}
    - action_get_name
