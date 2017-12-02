import sys
import requests
import json
from TimeSeries.get_timeseries import doSendRequest


def createAuthorization(username, password, appid):
    token = None
    ##create authentication request URL, message and header
    authenMsg = {'CreateServiceToken_Request_1': { 'ApplicationID':appid, 'Username':username,'Password':password }}
    authenURL = 'https://api.trkd.thomsonreuters.com/api/TokenManagement/TokenManagement.svc/REST/Anonymous/TokenManagement_1/CreateServiceToken_1'
    headers = {'content-type': 'application/json;charset=utf-8'}
    print('############### Sending Authentication request message to TRKD ###############')
    authenResult = doSendRequest(authenURL, authenMsg, headers)
    if authenResult is not None and authenResult.status_code == 200:
        print('Authen success')
        print('response status %s'%(authenResult.status_code))
        ##get Token
        token = authenResult.json()['CreateServiceToken_Response_1']['Token']

    return token