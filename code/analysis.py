from TwitterAPI import TwitterAPI
import pandas as pd
import dateutil.parser
import matplotlib.pyplot as plt

consumer_key = 'xxx'
consumer_secret = 'yyy'
access_token_key = 'www'
access_token_secret = 'zzz'
# Note that it is necessary to replace the keys above 
# with real values taken from a real twitter developer account

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

fr_tweets_per_day = {}
it_tweets_per_day = {}

first_day = 25
last_day = 30

for i in range(first_day, last_day + 1):
    j = i + 1
    r = api.request('search/tweets', {'q':'%23vinted', 'count':100, 'since':'2021-05-'+str(i), 'until':'2021-05-'+str(j), 'lang':'fr'})
    fr_tweets_per_day[i] = r.json()['statuses']

for i in range(first_day, last_day + 1):
    j = i + 1
    r = api.request('search/tweets', {'q':'%23vinted', 'count':100, 'since':'2021-05-'+str(i), 'until':'2021-05-'+str(j), 'lang':'it'})
    it_tweets_per_day[i] = r.json()['statuses']

for value in fr_tweets_per_day[first_day + 2]:
    print(value['id'])

for tweet in fr_tweets_per_day[first_day + 4]:
    datestring = tweet['created_at']
    yourdate = dateutil.parser.parse(datestring)
    if(yourdate.month < 10):
        data = str(yourdate.year)+'-0'+str(yourdate.month)+'-'+str(yourdate.day)+' '+str(yourdate.hour)+'-'+str(yourdate.minute)+'-'+str(yourdate.second)
        print(data)
    else:
        data = str(yourdate.year)+'-'+str(yourdate.month)+'-'+str(yourdate.day)+' '+str(yourdate.hour)+'-'+str(yourdate.minute)+'-'+str(yourdate.second)
        print(data)

index = 0
for i in range(first_day, last_day + 1):
    hour_tweet = None
    for tweet in fr_tweets_per_day[i]:
        datestring = tweet['created_at']
        yourdate = dateutil.parser.parse(datestring)
        if(0 <= yourdate.hour <= 3):
            fr_tweets[0, index] = fr_tweets[0, index] + 1
        elif(4 <= yourdate.hour <= 7):
            fr_tweets[1, index] = fr_tweets[1, index] + 1
        elif(8 <= yourdate.hour <= 11):
            fr_tweets[2, index] = fr_tweets[2, index] + 1
        elif(12 <= yourdate.hour <= 15):
            fr_tweets[3, index] = fr_tweets[3, index] + 1
        elif(16 <= yourdate.hour <= 19):
            fr_tweets[4, index] = fr_tweets[4, index] + 1
        elif(20 <= yourdate.hour <= 23):
            fr_tweets[5, index] = fr_tweets[5, index] + 1
    index = index + 1

index = 0
for i in range(first_day, last_day + 1):
    hour_tweet = None
    for tweet in it_tweets_per_day[i]:
        datestring = tweet['created_at']
        yourdate = dateutil.parser.parse(datestring)
        if(0 <= yourdate.hour <= 3):
            it_tweets[0, index] = it_tweets[0, index] + 1
        elif(4 <= yourdate.hour <= 7):
            it_tweets[1, index] = it_tweets[1, index] + 1
        elif(8 <= yourdate.hour <= 11):
            it_tweets[2, index] = it_tweets[2, index] + 1
        elif(12 <= yourdate.hour <= 15):
            it_tweets[3, index] = it_tweets[3, index] + 1
        elif(16 <= yourdate.hour <= 19):
            it_tweets[4, index] = it_tweets[4, index] + 1
        elif(20 <= yourdate.hour <= 23):
            it_tweets[5, index] = it_tweets[5, index] + 1
    index = index + 1

fr_final = pd.DataFrame(np.mean(fr_tweets, axis=1).round(decimals=2), columns=['French tweets mean'], index=['00:00 - 03:59', '04:00 - 07:59', '08:00 - 11:59', '12:00 - 15:59', '16:00 - 19:59', '20:00 - 23:59'])
it_final = pd.DataFrame(np.mean(it_tweets, axis=1).round(decimals=2), columns=['Italian tweets mean'], index=['00:00 - 03:59', '04:00 - 07:59', '08:00 - 11:59', '12:00 - 15:59', '16:00 - 19:59', '20:00 - 23:59'])

plt.close("all")

fig = plt.figure(figsize=(16,10))
plt.plot(fr_final, label='French Tweets')
plt.plot(it_final, label='Italian Tweets')
plt.legend(loc="upper left")
plt.xlabel('4-hours Time Interval')
plt.ylabel('Tweets posted')
plt.show()