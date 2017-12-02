import sys
import requests
import json

def doSendRequest(url, requestMsg, headers):
    result = None
    try:
        # send request
        result = requests.post(
            url, data=json.dumps(requestMsg), headers=headers)
        # handle error
        if result.status_code is not 200:
            print('Request fail')
            print('response status %s' % (result.status_code))
            if result.status_code == 500:  # if username or password or appid is wrong
                print('Error: %s' % (result.json()))
            result.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('Exception!!!')
        print(e)
        sys.exit(1)
    return result


def retrieveTimeSeries(token, appid, val, interval):
    ##construct news headline URL and header
    newsURL = 'http://api.trkd.thomsonreuters.com/api/TimeSeries/TimeSeries.svc/REST/TimeSeries_1/GetIntradayTimeSeries_4'
    headers = {'content-type': 'application/json;charset=utf-8' ,'X-Trkd-Auth-ApplicationID': appid, 'X-Trkd-Auth-Token' : token}
    ##construct a news headline request message
    newsRequestMsg = {
   "GetIntradayTimeSeries_Request_4": {
      "Symbol": val ,
      "StartTime": "2017-11-25T00:00:00",
      "EndTime": "2017-12-02T23:59:00",
      "Interval": interval,
      "TrimResponse": 'true'
   }
}
    print('############### Sending News Headline request message to TRKD ###############')
    newsResult = doSendRequest(newsURL, newsRequestMsg,headers)
    if newsResult is not None and newsResult.status_code == 200:
        print('News Headline response message: ')
        print(newsResult.json())

