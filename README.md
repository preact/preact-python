# Python example for Less Neglect

Simple example of calling the [Less Neglect API](http://beta.lessneglect.com/api/quickstart) with a Python helper.

## Example Registration Event

    params = {
      "person[name]": "Billy Coover",
      "person[email]": "billy@lessneglect.com",
      "person[uid]": "12345",
      "person[created_at]": 1358108502.033349,
      "person[properties][is_paying]": true,
      "event[name]": "registered"
    }

    log_event(params)

## Example Viewed Product Event

    params = {
      "person[name]": "Billy Coover",
      "person[email]": "billy@lessneglect.com",
      "person[uid]": "12345",
      "person[created_at]": 1358108502.033349,
      "event[name]": "viewed:product",
      "event[target_id]": "09555",
      "event[note]": "Slim-fit Textured Shirt",
      "event[timestamp]": 1359661757,
      "event[extras][color]": 'white',
      "event[extras][length]": 29.5,
      "event[extras][chest]": 41,
      "event[extras][waist]": 38,
      "event[extras][price]": 55.99
    }

    log_event(params)

## Requirements

 - [requests](http://docs.python-requests.org/en/latest/)
