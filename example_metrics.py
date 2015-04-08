from preact import log_metrics_bulk

metricsdata = {
  'data': [
    {
      'account_id': '517eda23c82561f72a000005',
      'name': 'total-gigabytes-utilized',
      'value': 691.751,
      'ts': 1428527783
    },
    {
      'account_id': '533dd27f4443aec9e4000001',
      'name': 'total-gigabytes-utilized',
      'value': 913.751,
      'ts': 1428527783
    }
  ] 
}

resp = log_metrics_bulk(metricsdata)

print resp
