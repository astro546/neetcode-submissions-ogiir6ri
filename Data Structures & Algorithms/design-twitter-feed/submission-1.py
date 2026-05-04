from collections import defaultdict 
from heapq import heappush, heappop
class Twitter:

    def __init__(self):
        self.count= 0
        self.postsByUser = defaultdict(list)
        self.followers = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postsByUser[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        minHeap = []

        self.followers[userId].add(userId)
        for followeeId in self.followers[userId]:
            if followeeId in self.postsByUser:
                index = len(self.postsByUser[followeeId]) - 1
                count, tweetId = self.postsByUser[followeeId][index]
                heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(news) < 10:
            count, tweetId, followeeId, index = heappop(minHeap)
            news.append(tweetId)
            if index >= 0:
                count, tweetId = self.postsByUser[followeeId][index]
                heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return news
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
