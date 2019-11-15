## Generated Story 8666448012529511115
* greet
    - utter_greet
    - utter_query
* deny{"deny": "No"}
    - utter_feedback
* confirm_feedback{"confirm_feedback": "Satisfied "}
    - slot{"confirm_feedback": "Satisfied"}
    - action_get_name
    
## Generated Story -766084129644292098
* greet
    - utter_greet
    - utter_query
* deny{"deny": "No"}
    - utter_feedback
* confirm_feedback{"confirm_feedback": "Not Satisfied"}
    - slot{"confirm_feedback": "Not Satisfied"}
    - action_get_name
    - slot{"person": null}
* person_name{"person": "shreya"}
    - slot{"person": "shreya"}
    - action_get_email
    - rewind
* email{"email": "shreya@gmail.com"}
    - slot{"email": "shreya@gmail.com"}
    - action_get_contact
    - rewind
* contact{"contact": "7009885433"}
    - slot{"contact": "7009885433"}
    - action_send_email

## Generated Story 5087095823866096379
* greet
    - utter_greet
    - utter_query
* deny{"deny": "No"}
    - utter_feedback
* confirm_feedback{"confirm_feedback": "Not Satisfied"}
    - slot{"confirm_feedback": "Not Satisfied"}
    - action_get_name
    - slot{"person": null}
* person_name{"person": "shivani"}
    - slot{"person": "shivani"}
    - action_get_email
    - rewind
* email{"email": "shivani@gmail.com"}
    - slot{"email": "shivani@gmail.com"}
    - action_get_contact
    - rewind
* contact{"contact": "9876543211"}
    - slot{"contact": "9876543211"}
    - action_send_email

## Generated Story -1793375598078664888
* thank you
    - utter_thank
    - action_restart

## Generated Story -6830477208814921973
* bye
    - action_bye

## Generated Story -1577498318899557733
* bye
    - action_bye
