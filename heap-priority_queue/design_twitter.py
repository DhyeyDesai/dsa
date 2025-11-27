# 355. Design Twitter
# https://leetcode.com/problems/design-twitter/


from collections import defaultdict
import heapq
from typing import List

class Twitter:
    # INTUITION:
    # - Use a global timestamp (count) to track tweet order (decrements for min-heap compatibility)
    # - Store tweets per user with timestamps for efficient retrieval
    # - Use heap-based k-way merge to get the 10 most recent tweets from all followees
    
    # TIME COMPLEXITY: O(1) for init
    # SPACE COMPLEXITY: O(U + T) where U = users, T = total tweets (capped at 10 per user)
    

    def __init__(self):
        self.count = 0  # Global timestamp (decrements to work with min-heap)
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeIds


    def postTweet(self, userId: int, tweetId: int) -> None:
        # INTUITION:
        # - Append tweet with current timestamp
        # - Keep only 10 most recent tweets per user to save memory
        # - Decrement count so newer tweets have more negative values (min-heap priority)
        
        # TIME COMPLEXITY: O(1)
        # SPACE COMPLEXITY: O(1) per tweet (bounded by 10 tweets per user)
        
        # Add tweet with current timestamp
        self.tweetMap[userId].append([self.count, tweetId])
        
        # Memory optimization: keep only 10 most recent tweets
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)  # Remove oldest tweet
        
        # Decrement timestamp (newer tweets get more negative values)
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # INTUITION:
        # - Use k-way merge with a min-heap to efficiently get 10 most recent tweets
        # - Each followee contributes their most recent tweet to the heap
        # - Pop the most recent tweet, then replace it with the next tweet from that same user
        # - This avoids loading all tweets into memory at once
        
        # TIME COMPLEXITY: O(F + 10*log(F)) where F = number of followees
        # SPACE COMPLEXITY: O(F) for the heap
        
        res = []  # Result list (ordered from most recent)
        minHeap = []  # Min-heap for k-way merge
        
        # User should see their own tweets
        self.followMap[userId].add(userId)

        # Strategy A: Many followees (>10) - pre-filter with max-heap
        if len(self.followMap[userId]) > 10:
            maxHeap = []  # Keep top 10 most recent tweets globally
            
            # Get the latest tweet from each followee
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1  # Most recent tweet
                    count, tweetId = self.tweetMap[followeeId][index]
                    
                    # Push to max-heap (negate count for max-heap behavior)
                    heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])
                    
                    # Keep only top 10 tweets
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            
            # Transfer from max-heap to min-heap (negate count back)
            while maxHeap:
                count, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followeeId, index])
        
        # Strategy B: Few followees (≤10) - add directly to min-heap
        else:
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1  # Most recent tweet
                    count, tweetId = self.tweetMap[followeeId][index]
                    
                    # Add to min-heap with index pointing to next tweet
                    heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        # K-way merge: extract 10 most recent tweets
        while minHeap and len(res) < 10:
            # Pop the most recent tweet
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # If this user has more tweets, add the next one to the heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        # INTUITION:
        # - Simply add followee to the follower's set
        
        # TIME COMPLEXITY: O(1)
        # SPACE COMPLEXITY: O(1)
        
        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # INTUITION:
        # - Remove followee from follower's set (with safety check)
        
        # TIME COMPLEXITY: O(1)
        # SPACE COMPLEXITY: O(1)
        
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)