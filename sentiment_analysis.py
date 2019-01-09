import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterSentimentAnalysis:
    def __init__(self):
        self.consumer_key = 'rRuIUHkfPVXBuUNfdvlybyky5'
        self.consumer_secret = 'fjpsILdzZsJQFJq9mq67EPoKVtNfjndBGOpzYcs0Apqd2rYTez'
        self.access_token = '1076364575790907392-zRabymhppRPxUsVu8OIldqmRFr1cwm'
        self.access_secret_token = 'IHa3fruniayzHEpmkWseIOXrDLSzo8yFaO06fWwEw9YuC'

    def set_twitter_auth(self):
        try:
            self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
            self.auth.set_access_token(self.access_token, self.access_token_secret)
        except Exception as e:
            print("ERROR:: Problem in setting tiwtter auth {}".format(e))
            self.auth = None
            
    def set_twitter_api_handle(self):
        try:
            self.auth.set_access_token(access_token, access_token_secret)
            self.api_handle = tweepy.API(auth)
        except Exception as e:
            print("ERROR:: Problem in geting twitter auth {}".format(e))
            self.api_handle = None

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
                    
    def get_tweets(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        import pdb;pdb.set_trace()
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        tweets = [] 
  
        try: 
            fetched_tweets = self.api_handle.search(q = query, count = count) 
  
            for tweet in fetched_tweets: 
                parsed_tweet = {} 
  
                parsed_tweet['text'] = tweet.text 
                parsed_tweet['sentiment'] = self.get_tweets(tweet.text) 
  
                if tweet.retweet_count > 0: 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            return tweets 
  
        except tweepy.TweepError as e: 
            print("ERROR in analysing tweet sentiment : " + str(e)) 

def main():
        import pdb;pdb.set_trace()
        api = TwitterSentimentAnalysis()
        tweets = api.get_tweets(query = 'Donald Trump', count = 20)

        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
        print("Neutral tweets percentage: {} % \
        ".format(100*len(tweets - ntweets - ptweets)/len(tweets)))

        print("\n\nPositive tweets:")
        for tweet in ptweets[:10]:
            print(tweet['text'])

        # printing first 5 negative tweets
        print("\n\nNegative tweets:")
        for tweet in ntweets[:10]:
            print(tweet['text'])

if __name__ == "__main__":
    main()
  

"""def get1_tweets(self, topic, count=10):
        try:
            fetched_tweets = self.api.search(q = query, count = count)
            tweets
        except Exception as e:
            print("ERROR:: Problem in getting tweets {}".format(e))

"""
