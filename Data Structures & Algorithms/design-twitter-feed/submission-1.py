class Twitter:

    def __init__(self):
        self.follows = {}
        self.newsfeed= []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.newsfeed.append(str(tweetId) + "#" + str(userId))

    def getNewsFeed(self, userId: int):
        #print(self.newsfeed)
        following = set()
        following.add(userId)
        results = []

        if userId in self.follows:
            for key, value in self.follows[userId].items():
                if value == True:
                    following.add(key)
        i = 0
        for key in self.newsfeed[::-1]:
            if i == 10:
                break
            element = key.split("#")
            tweet = int(element[0])
            user = int(element[1])

            if user in following:
                results.append(tweet)
                i+=1
        return results


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = {}
        self.follows[followerId][followeeId] = True


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return
        self.follows[followerId][followeeId] = False