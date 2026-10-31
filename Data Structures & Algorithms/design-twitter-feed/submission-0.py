from collections import deque
class Twitter:

    def __init__(self):
        self.tweets = deque([]) #[userid, tweetId]
        self.users = {} #userid : set(following)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft([userId, tweetId])
        if not userId in self.users:
            self.users[userId] = {userId}

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for tweet in self.tweets:
            if len(feed) >= 10:
                break
            if tweet[0] in self.users[userId]:
                feed.append(tweet[1])
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.users:
            self.users[followerId] = {followerId}

        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
       self.users[followerId].discard(followeeId)
 