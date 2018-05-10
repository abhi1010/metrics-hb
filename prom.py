from prometheus_client import start_http_server, Summary, Counter
import random
import time

_ID = 'bot-id-1'

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds',
                       'Time spent processing request')

Heartbeat = Counter('request_hb_total', 'heartbeat total', ['id'])


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    Heartbeat.labels(_ID).inc()
    # Heartbeat.inc()
    time.sleep(t)
    # print('Sleeping for {}'.format(t))


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random() / 3)
