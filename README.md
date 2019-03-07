# Liverpool-Bot

### https://twitter.com/liverpool_never

A bot that tweets out Liverpool related content using the Twitter (tweepy) and Reddit (praw) APIs. Because you can never get enough Liverpool.

## As of right now, the bot has the capacity to:
1. Reply to any tweets where it is mentioned and contains the string '#YNWA'. 
2. Post the top post—which can be filtered from top, new, controversial, or hot—from a given subreddit (r/LiverpoolFC is most applicable here, of course). The posts can also be filtered by time—day, week, month, year.
3. Write and read two files. One stores the most recent mention ID so as to avoid replying to all mentions during each loop. The other stores all the submission IDs from the posts that the bot has tweeted out so as to avoid tweeting out the same post multiple times.

## In the future, I would like it to:
1. Be able to find all tweets with a certain string and reply to each one.
2. String longer tweets together as a thread.
3. Periodically bash Manchester United fans, of course.
4. Be hosted online.

## Challenges
The entire project was quite challenging, but I enjoyed it thoroughly. Although I knew python prior to starting this project, my knowledge in the language was definitely enhanced and solidified after having a go at this bot. Specifically, I found it very difficult to figure out a way to post only the first 280 characters of a longer tweet and reply to the initial tweet with the remainder of the string, which would be broken up into more replies as necessary. Additionally, it was challenging to find a way to only use submissions that were yet to be posted. However, after I thought about this with a Fundies 1 (Fundamentals of Computer Science I) mindset, I thought to use recursion, using first and rest. This has been fully functional thus far. Finally, I want to host this script online so that I can run the bot without having to have my computer open. For that, I am thinking about using Heroku, which I have not used before. This will be my first time dealing with online servers.

## Motivation
Of course, Liverpool is the best football club in the English Premier League. There is no shame in showing the Red spirit. It's also a great way to stay up-to-date with Liverpool activity and the general consensus about the club among fans. 

However, this was an idea I had come up with to practice my Python skills and to explore the Reddit and Twitter APIs. Admittedly, the Reddit API was fairly straightforward and well organized, making it very easy to use. Twitter, on the other hand, was much more difficult. I did not come up with all the code by myself. Luckily, I found YK Dojo's YouTube videos and was able to follow along for a portion of my project. He definitely helped me get started. 

#### You'll Never Walk Alone!

#### Pictures:
![alt text](https://imgur.com/a/ZQ7nQ2t.png)
![alt text](https://imgur.com/a/y7MQrRT.png)
![alt text](https://imgur.com/a/guojzXZ)
