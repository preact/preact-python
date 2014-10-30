from preact import log_event

person = {
  'email': 'gooley@preact.com',
  'name': 'Christopher Gooley',
  'properties': {
    'is_paying': True
  }
}

event = {
  'name': 'updated-profile'
}

eventdata = {
  'person': person,
  'event': event
}

resp = log_event(eventdata)

print resp
