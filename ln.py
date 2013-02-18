import config, requests

#basic events

def registered(person):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_REGISTERED}
  body = dict(person, **req)

  #debug
  print body
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp

def upgraded(person):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_UPGRADED}
  body = dict(person, **req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp

def deleted_account(person):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_DELETED_ACCOUNT}
  body = dict(person, **req)
  resp = requests.post(url, data=data, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp

def updated_account(person):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_UPDATED_ACCOUNT}
  body = dict(person, **req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp

def logged_in(person):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_LOGGED_IN}
  body = dict(person, **req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp

def logged_out(person):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_LOGGED_OUT}
  body = dict(person, **req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp

def forgot_password(person):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_FORGOT_PASSWORD}
  body = dict(person, **req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp

def changed_password(person):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_CHANGED_PASSWORD}
  body = dict(person, **req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp

def updated_profile(person):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_UPDATED_PROFILE}
  body = dict(person, **req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp

#item based events  

def purchased(person, item):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_PURCHASED}
  body = dict(person, **item)
  body.update(req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp

def created(person, item):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_CREATED}
  body = dict(person, **item)
  body.update(req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp

def uploaded(person, item):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_UPLOADED}
  body = dict(person, **item)
  body.update(req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp 

def deleted(person, item):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_DELETED}
  body = dict(person, **item)
  body.update(req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp 

def modified(person, item):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_MODIFIED}
  body = dict(person, **item)
  body.update(req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp 

def viewed(person, item):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_VIEWED}
  body = dict(person, **item)
  body.update(req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp     

#global generic event

def log_event(data):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  req = {"event[name]": config.LN_EVENT_UPGRADED}
  body = dict(person, **data)
  body.update(req)
  resp = requests.post(url, data=body, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp                
