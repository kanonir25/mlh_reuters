from authorize import createAuthorization
from TimeSeries.get_timeseries import retrieveTimeSeries

if __name__ == '__main__':
    username = "trkd-demo-wm@thomsonreuters.com"
    ##use getpass.getpass to hide user inputted password
    password = "o3o4h91ac"
    #password = getpass.getpass(prompt='Please input password: ')
    appid = "trkddemoappwm"

    token = createAuthorization(username,password,appid)
    print('Token = %s'%(token))

    ## if authentiacation success, continue subscribing News Headline
    if token is not None:
        retrieveTimeSeries(token,appid, "BTC=", "HOUR")