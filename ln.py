import config, requests

def log_event(data):
  url = config.LN_API_URL + config.LN_EVENTS_ENDPOINT
  resp = requests.post(url, data=data, auth=(config.LN_PROJECT_CODE, config.LN_API_SECRET))
  return resp
