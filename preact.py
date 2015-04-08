import config, requests, json

def log_event(data):
  return post_data(data, config.EVENTS_ENDPOINT)
  
def log_metrics_bulk(data):
  return post_data(data, config.METRICS_BULK_ENDPOINT)

def post_data(data, endpoint):
  url = config.API_URL + endpoint
  auth = (config.PROJECT_CODE, config.API_SECRET)
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

  # convert dictionary to json
  json_data = json.dumps(data)

  resp = requests.post(url, data=json_data, headers=headers, auth=auth)
  return resp