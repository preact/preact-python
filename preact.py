import config, requests, json

def log_event(data):
  url = config.API_URL + config.EVENTS_ENDPOINT
  auth = (config.PROJECT_CODE, config.API_SECRET)
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

  # convert dictionary to json
  json_data = json.dumps(data)

  resp = requests.post(url, data=json_data, headers=headers, auth=auth)
  return resp
