from collections import defaultdict 
from heapq import heappush, heappop
class Twitter:

    # count: Negative number that tracks the most recent tweet, 
    #           the smaller count, the more recent is tge tweet
    # postsByUser: Hashmap that stores  the posts published by each user
    # followers: Hashmap that match the userID with a set of its users that follows
    def __init__(self):
        self.count= 0
        self.postsByUser = defaultdict(list)
        self.followers = defaultdict(set)
        
    # Time and space: O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postsByUser[userId].append([self.count, tweetId])
        self.count -= 1
        
    # Time: O(n log n)
    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        minHeap = []

        # First, we push all the most recent posts from all users that the user follows
        # The main criteria for the min heap is count.
        self.followers[userId].add(userId)
        for followeeId in self.followers[userId]:
            if followeeId in self.postsByUser:
                index = len(self.postsByUser[followeeId]) - 1
                count, tweetId = self.postsByUser[followeeId][index]
                heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Then, we will push the next recent posts from every user, until we will have 10 elements
        # in the news array, and every time we push a new element, we decrement the index
        # to point to the next post in the current followeeId.
        while minHeap and len(news) < 10:
            count, tweetId, followeeId, index = heappop(minHeap)
            news.append(tweetId)
            if index >= 0:
                count, tweetId = self.postsByUser[followeeId][index]
                heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return news
        
    # Time and Space: O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    # Time and Space: O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
