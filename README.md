# Python example for Less Neglect

Simple example of calling the [Less Neglect](http://www.lessneglect.com) API from Python.

## Example Registration Event

    params = {
      "person[name]": "Billy Coover",
      "person[email]": "billy@lessneglect.com",
      "person[properties][is_paying]": 1,
      "event[name]": "registered",
      "event[klass]": "actionevent"
    }

    log_event(params)

## Requirements

 - [requests](http://docs.python-requests.org/en/latest/)
