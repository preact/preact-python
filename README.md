# Python example for Less Neglect

Simple example of calling the [Less Neglect](http://www.lessneglect.com) API from Python.

## Example Registration Event

    params = {
      "person[name]": "Billy Coover",
      "person[email]": "billy@lessneglect.com",
      "person[external_identifier]": "12345",
      "person[properties][created_at]": 1358108502.033349,
      "event[name]": "viewed:item",
      "event[klass]": "actionevent",
      "event[external_identifier]": "54321",
      "event[note]": "Item Name"
    }

    log_event(params)

## Requirements

 - [requests](http://docs.python-requests.org/en/latest/)
