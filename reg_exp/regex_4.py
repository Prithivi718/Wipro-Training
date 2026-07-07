import re

tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0p0xd cc: @garybernhardt #rstats"

tweet = re.sub(r"http\S+", "", tweet)      # Remove URLs
tweet = re.sub(r"@\w+", "", tweet)         # Remove mentions
tweet = re.sub(r"#\w+", "", tweet)         # Remove hashtags
tweet = re.sub(r"\bRT\b|\bcc\b", "", tweet) # Remove RT and cc
tweet = re.sub(r"[^\w\s]", "", tweet)      # Remove punctuation

print(tweet.strip())