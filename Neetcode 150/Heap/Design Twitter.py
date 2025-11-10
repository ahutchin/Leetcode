from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        # Hashmap for tweets and follows
        self.tweets, self.follows = defaultdict(lambda: []), defaultdict(lambda: [])

        # Var to track number of tweets
        self.tweetNum = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add (tweetNum, tweetId) to user's tweets
        self.tweets[userId].append((self.tweetNum, tweetId))
        self.tweetNum -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Create a maxHeap of user's and their follower's tweets
        tweets = self.tweets[userId].copy()
        for followee in self.follows[userId]:
            tweets += self.tweets[followee].copy()
        
        heapq.heapify(tweets) 
        res = []
        i = 0
        while tweets and i < 10:
            tweet = heapq.heappop(tweets)[1]
            res.append(tweet)
            i += 1
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followee to the follower's list of following
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove the followee from the follower's following list
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Intuition:
# Need to store User, their own posts, and who they follow

# Test
["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]

Twitter = Twitter()
Twitter.postTweet(1,5)
print(Twitter.getNewsFeed(1))
Twitter.follow(1,2)
Twitter.postTweet(2,6)
print(Twitter.getNewsFeed(1))
Twitter.unfollow(1,2)
print(Twitter.getNewsFeed(1))

# Time complexity: O(nlogn) for getNewsFeed and O(1) for all others