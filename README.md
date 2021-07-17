# Twitter API Tutorial
In this tutorial there will be a detailed explaination of __how to use the Twitter API__. <br> This work is going to use __Python__ as programming language.<br><br>
# What is Twitter?
Twitter is a 'microblogging' social network that allows you to send and receive short posts called tweets. Tweets can be up to 140 characters long and can include links to relevant websites and resources.<br>

Twitter users follow other users. If you follow someone you can see their tweets in your twitter 'timeline'. You can choose to follow people and organisations with similar academic and personal interests to you.<br>

You can create your own tweets or you can retweet information that has been tweeted by others. Retweeting means that information can be shared quickly and efficiently with a large number of people [1]. <br>

During the last years, Twitter became very important and its popolarity is increasing day by day. It is literally used by everybody, from artists to politicians, for many reasons, such as:<br>
* express an idea and tell thoughts about something
* promote a product or a service
* reach a big amount of people
* explore the audience and try to reach new people
* share th work and get feedbacks from people<br>

## How to use Twitter
* To use the social media and its features users have to log in. If they don't have any Twitter account, it is possible to sign in and create a new account.
* After the log in, users can use all twitter features, such as creating new tweet, retweet an existing tweet, search for specific tweets, and so on.<br><br>

# Twitter Developer Platform
Twitter, as well as many social networks, provides to users __API (Application Programming Interfaces)__.
## API
APIs are tools used to facilitate the interaction between developers and platforms. They are useful when developers would like to use some elements of this social network with ease, to make the work faster. There are many types of API which are able to extend and improve the functions of a software. This tool, moreover, allows the interaction between programmes and software, with the possibility to create more professional features.<br>

How can APIs be used? How can a software interract with APIs? The relationship created between APIs and a software is similar to what happens in the Web server-Client paradigm: to request a service or data, the client generally sends a message to a server, which respondes with the desired result. The same thing happens between APIs and softwares. The request is made to an __endpoint__, which provides a specific response. Clearly, the sofware has to be authentificated to access to the server data.<br>

To make these requests, __REST__ (Representational State Transfer) is used. It is the way to made the requests between softwares and APIs. REST uses some protocols such as HTTP. For instance, if a sofware needs to use an API, HTTP is used to define the structure of the request and the response. In this scenario, the server (API) respondes to the sofware not with a HTML page, but with structured data in a specific format, such as Json.
## Twitter API
Twitter API allow its service to be accessed via APIs to enable software development that integrates with Twitter, such as a solution that helps a company respond to customer feedback on Twitter. They also allow users to deal with Tweets is a easier way. <br>

Usually, Twitter API are used to:
* Access Twitter profiles and posts
* Publish tweets and retweet existing tweets
* Analyze tweets and make evaluations<br>

## How to access to Twitter API
Starting to use Twitter API requires some steps:
* Firstly, go to the Developer Platform [page](https://developer.twitter.com/en) and click on sign in (top right)<br>

![](/images/login.JPG)<br><br><br>

* After clicking on sign in, create a Twitter account if there is not one available, then click access<br>

![](/images/login2.JPG)<br><br><br>

* Now go again to the Developer Platform [page](https://developer.twitter.com/en). In the top right section of the page there will be a [link](https://developer.twitter.com/en/apply-for-access) to apply for a developer account<br>

![](/images/apply.JPG)<br><br><br>

* After clicking apply, click to the choice 'Apply for a developer account'<br>

![](/images/apply2.JPG)<br><br><br>

* In the next page, choose the option 'Academic', 'Student' and then click on 'Get started'<br>

![](/images/apply3.JPG)<br><br><br>

* Once you reach the next page, fill the infos and then click on 'Next'<br>

![](/images/apply4.JPG)<br><br><br>

* In the next page, insert the reasons why APIs are going to be used<br>

![](/images/apply5.JPG)<br><br><br>

* Then, there will be a 'Review' page where it is possible to check one more time the informations <br>

![](/images/apply6.JPG)<br><br><br>

* After agree to the term, the access request will be submitted<br>

![](/images/apply7.JPG)<br><br><br>

* After have verificated the email __(the verification has to be done via browser)__, a project has to be created

![](/images/api1.JPG)<br><br><br>

* Insert the informations about the project and the name of the App which will be created inside the project

![](/images/pro1.JPG)![](/images/pro2.JPG)![](/images/pro3.JPG)![](/images/pro4.JPG)<br><br><br>

* After that, informations about API Key and API secret Key will be available. Note that this infos should be kept __secret__.

![](/images/pro5.JPG)<br><br><br>

> __Note__ Note that I already had a Twitter Developer Profile, and I'm going to use that. If a standard developer profile is already available, it is possible to directly create a __standalone app__ outside any project<br><br>![](/images/api2.JPG)

<br><br>
However, since standalone apps can't use v2 Early Access endpoints, for this tutorial i will use the Twitter Developer Profile i have created during the previous procedure.<br>
## Projects and Apps
It is possible to use Apps and Projects to help organize the work with the Twitter Developer Platform by use case. Each Project can contain a single app at this point in time. To access the new Twitter API v2 endpoints, it is needed to use credentials from an App that is associated with a project.

If you have previously created Apps, they will be visible in the section entitled “Standalone Apps”. Standalone Apps are Apps outside of the Project structure, meaning that the credentials from that App will be able to make requests to all endpoints other than the new Twitter API v2 offering [2].

Apps are useful to access to Twitter API, expecially to obtain a set of authentication credentials, also known as keys and tokens, that must being passed with each request.

The standard for authorization used in Twitter API is __OAuth__.

OAuth is an open standard for access delegation, commonly used as a way for Internet users to grant websites or applications access to their information on other websites but without giving them the passwords. This mechanism is used by companies such as Amazon, Google, Facebook, Microsoft and Twitter to permit the users to share information about their accounts with third party applications or websites.

Generally, OAuth provides clients a "secure delegated access" to server resources on behalf of a resource owner. It specifies a process for resource owners to authorize third-party access to their server resources without providing credentials. Designed specifically to work with Hypertext Transfer Protocol (HTTP), OAuth essentially allows access tokens to be issued to third-party clients by an authorization server, with the approval of the resource owner. The third party then uses the access token to access the protected resources hosted by the resource server [3].<br><br><br>

# Twitter API Example - Official REST API
This section will focus on an example which will explain how to interact with Twitter API. __The offical Twitter REST API__ are going to be used. It is possible to access to these API through ``cURL``.<br>

The usage of official Twitter API is possible using both __cURL__ and __request in Python__.<br>

* ``cURL`` is a computer software project providing a library (libcurl) and command-line tool (curl) for transferring data using various network protocols. cURL allows to execute command on a terminal.
* ``request`` in python is a way to use the cURL features into Python. For instance, it is possible to use a tool which will convert cURL commands in Python code.<br>

This section will continue with the explaination of the usage of ``cURL`` in order to access the Tweitter REST API, and then with the description of the same requests in Python.
## Authentication - cURL
In order to use Twitter REST API, you first need to acquire a set of application tokens. To get these key, creating an App is necessary. After that, go in that App and click the Keys and tokens section to get the keys.<br>

Now, it is necessary get a __temporary token__:
        
    curl --user "$API_KEY:$API_SECRET_KEY" \
          --data 'grant_type=client_credentials' \
          'https://api.twitter.com/oauth2/token'
 
The response will be a json object containing:
 
    {"token_type":"bearer","access_token":"AAAAAAAAAAAAAAAAAAAAA……"}

> __Note__ It is necessary to replace the real keys in place of the sections in brackets
## Search Tweets - cURL
After the authentication, it is possible to execute some requests to Twitter REST API. For instance, let's search some tweets.

    curl https://api.twitter.com/2/tweets/search/recent?query=(%23palestine)%20lang%3Aen&max_results=10 
    -H "Authorization: Bearer AAAAAAAAAAAAAAAAAA....."

The response will contain a json object.

## Authentication - Python
In this case, cURL will be substituted with requests in Python. To do that, it is possible to use a [tool](https://curl.trillworks.com/#) which will convert cURL commands in Python code.<br>

The process will be the same as the cURL one, but it will be able to be runned in Python.

    import requests

    data = {
      'grant_type': 'client_credentials'
    }

    response = requests.post('https://api.twitter.com/oauth2/token', data=data, auth=('GQ7ny8Zo2Pa7B1ukVOPPrN0Yl', 'V66iB79Cr9QXCjs9oxLzO9U7QfrfUl5XSKKo72alCTdya10Icg'))

<br>

    response.json()
    
## Search Tweets - Python
The process will be the same as the Tweets Search with cURL, but it will be able to be runned in Python.<br>

    import requests

    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMRsQAEAAAAAtrqo8DI7e9aWNnmqh9iyaA0A42w%3DPhSvY3IgCfrkaY9L89qAG7iACJ7QYvfuFD82FkNIhmxxvjCSaO',
    }

    params = (
        ('query', '(#palestine) lang:en'),
        ('max_results', '10'),
    )

    response1 = requests.get('https://api.twitter.com/2/tweets/search/recent', headers=headers, params=params)
    
<br>
For instance, let's print the json of the response.
    
    response1.json()
    
Let's create a list of the response tweets.

    t = response1.json()['data']
    
Now, let's parse the list to find the tweets ids, and insert it in a new list.

    ids = []
    for item in t:
        ids.append(item['id'])
        
Since a Tweets IDs list is available, it is possible to make another cURL request to get all the tweets by their IDs.<br>

Here the cURL command:

    curl "https://api.twitter.com/2/tweets/id" -H "Authorization: Bearer BEARER_TOKEN"

The Python code for this cURL command is:

    import requests
    texts = []
    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMRsQAEAAAAAtrqo8DI7e9aWNnmqh9iyaA0A42w%3DPhSvY3IgCfrkaY9L89qAG7iACJ7QYvfuFD82FkNIhmxxvjCSaO',
    }
    for item in ids:
        response2 = requests.get('https://api.twitter.com/2/tweets/'+item, headers=headers)
        texts.append(response2.json()['data']['text'])

So, the cURL command has been used to request all the tweets according to the ids list. The text of these tweets has been inserted in another list.<br><br><br>

# Twitter API Example - TwitterAPI
This section will focus on an example which will explain how to interact with Twitter API. The library that is going to be used is __TwitterAPI__. This library provides a pure Python interface for the Twitter API.
## Installation
To install the library, go on the terminal and execute:

    pip install TwitterAPI
    
## Authentication
In order to use the python-twitter API client, you first need to acquire a set of application tokens. To get these key, creating an App is necessary. After that, go in that App and click the __Keys and tokens__ section to get the keys.<br>

Then, open a Python file, import twitter and call the function ``TwitterAPI``, passing the keys

    from TwitterAPI import TwitterAPI
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    
> __Note__ It is necessary to replace the real keys in place of the sections in brackets
## Search Tweets
To search a specific tweet it is possible to use the ``TwitterAPI.request()``. The method ``request()`` works with all endpoints found in either the REST APIs or the Streaming APIs. Usually ``request()`` takes two arguments: a Twitter endpoint and a dictionary of endpoint parameters. If a particular search is needed, it is possible to find Twitter’s documentation at https://dev.twitter.com/rest/public/search and go to the [GET /2/tweets/search/recent](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent) section.<br>

Here an example.

    r = api.request('search/tweets', {'q':'covid19','count':10, 'expansion':'geo.place'})
    tweets = r.json()['statuses']
    
``api.request()`` returns a Twitter response object, and with the method ``json()`` is it possible to return the json object.<br>

``tweets`` is a list of json object, each one refering to a tweet. The length of this list is equal to the parameter ``count`` passed to the ``request()`` method.<br>

For instance, let's print some informations about tweets.

    len(tweets)
    
<br>

    for tweet in tweets:
        print(tweet["lang"])

<br><br>

# Twitter API Example - python-twitter
This section will focus on an example which will explain how to interact with Twitter API. The library that is going to be used is __python-twitter__. This library provides a pure Python interface for the Twitter API.
## Installation
To install the library, go on the terminal and execute:

    pip install python-twitter
    
## Authentication
In order to use the python-twitter API client, you first need to acquire a set of application tokens. These will be your consumer_key and consumer_secret, which get passed to ``twitter.Api()`` when starting your application [4]. To get these key, creating an App is necessary. After that, go in that App and click the __Keys and tokens__ section to get the keys.<br>

Then, open a Python file, import twitter and call the function ``twitter.Api()``, passing the keys

    import twitter
    api = twitter.Api(consumer_key=[consumer key],
                  consumer_secret=[consumer secret],
                  access_token_key=[access token],
                  access_token_secret=[access token secret])
                  
It is also possible to get a Bearer token with ``GetAppOnlyAuthToken(consumer_key, consumer_secret)``

    twitter.Api().GetAppOnlyAuthToken(consumer_key, consumer_secret)

The response will be a Json such as

    {'token_type': 'bearer',
    'access_token': 'AAAAAAAAAAAAAAAAAAAAAMR...'}
    
> __Note__ It is necessary to replace the real keys in place of the sections in square brackets
## Search Tweets
To search a specific tweet it is possible to use the ``Api.GetSearch()`` method, and pass the parameter ``raw_query``, which should be the query string wanted to use for the search omitting the leading “?”. If a particular search is needed, it is possible to find Twitter’s documentation at https://dev.twitter.com/rest/public/search and go to the [GET /2/tweets/search/recent](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent) section.<br>

Here an example.

    results = api.GetSearch(
    raw_query="q=biden%20&result_type=recent&since=2014-07-19&count=100")

In results there will be an object containing the tweets informations.<br><br>

# Data Analysis
This last section of the tutorial will focus on a simple analysis of twitter data extracted with Twitter API. The library used for this analysis is TwitterAPI. The full code is available in the /code directory.<br><br>
## Scenario
Vinted is a Lithuanian online marketplace and community that allows its users to sell, buy, and swap new or secondhand clothing items and accessories [5].<br>

The analysis is about Vinted. Vinted is widespread in Europe, and this analysis focuses on what times of the day French people and Italian people prefer to tweet about Vinted.<br><br>
## Preparation
Firstly, the authentication is needed to use ``Twitter API``.

    from TwitterAPI import TwitterAPI
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    
> __Note__ It is necessary to replace the real keys in place of the sections in brackets

After the authentication, create two dictionaries which will contain for every key (day) a value (list of json object, which basically are either Italian or French Tweets).<br>

    fr_tweets_per_day = {}
    it_tweets_per_day = {}
    
Then, to search a specific tweet it is possible to use the ``TwitterAPI.request()``. The method ``request()`` works with all endpoints found in either the REST APIs or the Streaming APIs. Usually ``request()`` takes two arguments: a Twitter endpoint and a dictionary of endpoint parameters.<br>

> __Note__ In this case, the parameters are an __hashtag__, __since__, which specifies the minimum creation date that tweets returned by the method will have, __until__, which specifies the maximum creation date that tweets returned by the method will have, and __lang__, which specifies the language of the tweets returned. The analysis is supposing that only French language tweets refers to Vinted French Tweets, as well as Italy<br>

> __Note__ Since standard Twitter Developer Platform is used, the search is possible only within the last 6 days; therefore, the analysis will be done from 25 May to 31 May.<br>

    first_day = 25
    last_day = 30

To insert tweets inside the dictionaries created previously, it is possible to use a for loop in a range between the days choosen for the analysis.<br>

    for i in range(first_day, last_day + 1):
            j = i + 1
            r = api.request('search/tweets', {'q':'%23vinted', 'count':100, 'since':'2021-05-'+str(i), 'until':'2021-05-'+str(j), 'lang':'fr'})
            fr_tweets_per_day[i] = r.json()['statuses']
<br>

    for i in range(first_day, last_day + 1):
            j = i + 1
            r = api.request('search/tweets', {'q':'%23vinted', 'count':100, 'since':'2021-05-'+str(i), 'until':'2021-05-'+str(j), 'lang':'it'})
            it_tweets_per_day[i] = r.json()['statuses']

Now, both dictionaries contain tweets.<br>

For instance, here all the French Tweets posted on 27 May 2021 about Vinted (the IDs):

    for value in fr_tweets_per_day[first_day + 2]:
        print(value['id'])
    
Now, let's show the creation date of tweets posted on Twitter by French people on 29 May 2021 in a pretty format:

    import dateutil.parser

    for tweet in fr_tweets_per_day[first_day + 4]:
        datestring = tweet['created_at']
        yourdate = dateutil.parser.parse(datestring)
        if(yourdate.month < 10):
            data = str(yourdate.year)+'-0'+str(yourdate.month)+'-'+str(yourdate.day)+' '+str(yourdate.hour)+'-'+str(yourdate.minute)+'-'+str(yourdate.second)
            print(data)
        else:
            data = str(yourdate.year)+'-'+str(yourdate.month)+'-'+str(yourdate.day)+' '+str(yourdate.hour)+'-'+str(yourdate.minute)+'-'+str(yourdate.second)
            print(data)
       
<br><br>
## Analysis
Once the creation of the two dictionaries containing for every key (day from 25 to 31) a value (list of json object, which basically are either Italian or French Tweets), the analysis will begin.<br>

Firstly, it is a good choice to create two numpy array 6x6:
* each one will have 6 rows, each refering to a 4-hours time interval (the first row will refer to tweets posted between 00.00 and 03.59, and so on)
* each one will have 6 columns, each refering to the day (from 25 to 31) when the tweet has been posted

Both array are will be initialized to zero (int).
     
    import numpy as np
    fr_tweets = np.zeros((6,6)).astype(int)
    it_tweets = np.zeros((6,6)).astype(int)

After that, both array will be filled: each entry will contain the number of tweet posted within a 4-hours time interval (row) and a specific day (column).<br>

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
        
For instance, the ``fr_tweets[0, 0]`` will contain the number of tweets posted on 25 May between 00:00 and 03:59.<br>

It is also possible to check the correctness of the data by comparing the two final numpy array with the effective posting hour of the tweets.<br>

Now, the analysis will continue with the creation of another array: each entry of this array will contain the mean of tweets posted in the 6 days during a specific 4-hours time interval.<br>

For instance, the first entry of the array will contain the mean of tweets posted between 00:00 and 03:59 calculated for six days.

To better organize data, it is a good practise use __Pandas__ and __Data Frames__.

    import pandas as pd
    fr_final = pd.DataFrame(np.mean(fr_tweets, axis=1).round(decimals=2), columns=['French tweets mean'], index=['00:00 - 03:59', '04:00 - 07:59', '08:00 - 11:59', '12:00 - 15:59', '16:00 - 19:59', '20:00 - 23:59'])
    it_final = pd.DataFrame(np.mean(it_tweets, axis=1).round(decimals=2), columns=['Italian tweets mean'], index=['00:00 - 03:59', '04:00 - 07:59', '08:00 - 11:59', '12:00 - 15:59', '16:00 - 19:59', '20:00 - 23:59'])
    
The analysis is done. Looking at the last two array, it is quite simple understand that, taking the time interval between 25 May and 31 May, on average French people prefer to post tweets about Vinted between 12:00 and 15:59, while they don't prefer to do it between 00:00 and 03:59.

To better understand the behaviors of this analysis, it is a good choice to __visualize the results__.<br><br>

## Visualization
To visualize the data frames obtained, it is possible to use the library ``MatPlotLib``.<br>
    
    import matplotlib.pyplot as plt
    plt.close("all")
    
    fig = plt.figure(figsize=(16,10))
    plt.plot(fr_final, label='French Tweets')
    plt.plot(it_final, label='Italian Tweets')
    plt.legend(loc="upper left")
    plt.xlabel('4-hours Time Interval')
    plt.ylabel('Tweets posted')
    plt.show()

## Note about the Analysis
The Data Analysis discussed above has been made with a standard Developer Account. This means that, for instance, the search tweet functionality on Twitter API is restricted to a __recent__ mode, and it allows to get tweets __only within the last 7 days__.<br>

Thus, since the days choosen for the analysis are static (25 May to 31 May), the project will not work if it will be runned after some day. Therefore, change the analyis days would be a solution to let the analsyis work.<br><br><br>
# Conclusion
The tutorial was a simple study-case of Twitter API. It introduced both API and Twitter API, explaining:
* What is API
* What is Twitter
* How to be able to use Twitter API
* How to use Twitter API with Official REST API calls, and some wrapper in Python

It offered also a simple example of a Data Analysis made from Tweets informations obtained from the Twitter API usage.

It is clearly evident that using Twitter API is not hard as it is likely to think, and with a sufficient knowledge of the topics it is possible to use Twitter to develop some interesting projects.


# References
[1] https://esrc.ukri.org/research/impact-toolkit/social-media/twitter/what-is-twitter/. Accessed on 27 May 2021.<br>
[2] https://developer.twitter.com/en/docs/apps/overview. Accessed on 28 May 2021.<br>
[3] https://en.wikipedia.org/wiki/OAuth. Accessed on 28 May 2021.<br>
[4] https://python-twitter.readthedocs.io/en/latest/. Accessed on 30 May 2021.<br>
[5] https://en.wikipedia.org/wiki/Vinted. Accessed on 31 May 2021.<br>
