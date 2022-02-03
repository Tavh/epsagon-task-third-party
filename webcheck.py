import json
import time

import requests
import uuid


class RequestDetails:
    id: str
    timestamp: float
    duration: float
    targetUrl: str
    responseCode: int

    def __init__(self, id, timestamp, duration, targetUrl, responseCode):
        self.id = id
        self.timestamp = timestamp
        self.duration = duration
        self.targetUrl = targetUrl
        self.responseCode = responseCode


# Sends the request details to the server
def report(request_details):
    print(json.dumps(request_details.__dict__))
    requests.post(
        url="http://localhost:8080/request-details",
        data=json.dumps(request_details.__dict__),
        headers={"Content-Type": "application/json"}
    )


# Monkey patches request.get to extract all the data from it whenever called
def monitored_get(http_get):
    def extension(url):
        start_time = time.time()
        res = http_get(url)
        end_time = time.time()
        report(RequestDetails(
            str(uuid.uuid4()),
            start_time,
            end_time - start_time,
            res.url,
            res.status_code
        ))
        return res

    return extension


requests.get = monitored_get(requests.get)
