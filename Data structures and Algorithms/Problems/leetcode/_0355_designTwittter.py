'''
355. Design Twitter
Medium

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output:
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5, because tweet id 6 is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

Constraints:

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
All the tweets have unique IDs.
At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

'''
from typing import List

class Twitter:

    def __init__(self):

        # use of a heap to keep track of recency?
        # hashmap that stores the users that user follows?
        # follow and unfollow commands -> how to add and remove users
        # 
        # {
        #  "1": [5, 7, 8], #<- userNumber: [postId, postId]
        #              
        # }
        # {
        # "1": ["followerId", "followerId"]
        # }
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:

        print("post!")
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        print("get!")
        return []

    def follow(self, followerId: int, followeeId: int) -> None:

        print("follow!")
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print("unfollow!")
        pass


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

command = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
values = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]


twitter = Twitter()
for i in range(1, len(command) - 1):
    if command[i] == "postTweet":
        x, y = values[i]
        twitter.postTweet(x, y)
    elif command[i] == "getNewsFeed":
        x = values[i]
        twitter.getNewsFeed(x[0])
    elif command[i] == "follow":
        er, ee = values[i]
        twitter.follow(er, ee)
    elif command[i] == "unfollow":
        er, ee = values[i]
        twitter.unfollow(er, ee)
    print()