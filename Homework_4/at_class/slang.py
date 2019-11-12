#!/usr/bin/env python3
# Indian style program in 1 min :)
import random

test = """Reading is the best way to improve your vocabulary! The context of articles, stories, and conversations helps you figure out and understand the meaning of English words in the text that are new to you. Reading also provides repetition of vocabulary words you have already learned to help you remember them.

Reading comprehension is easier if you already know the keywords in the reading. This is one reason that new vocabulary is presented and practiced at the beginning of each USA Learns unit. You learn the meaning and practice the pronunciation of the most important words that you will later read in video scripts and reading lessons.!!!"""

slang_phrases = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?",
                 ", eh?", ", aw yea.", ", yo.", "? No way!", ". Awesome!"]


test_list = test.split()


print(random.choice(slang_phrases))


a = test.replace("!", random.choice(slang_phrases))
b = a.replace(".", random.choice(slang_phrases))
c = b.replace("!", random.choice(slang_phrases))
d = c.replace("?", random.choice(slang_phrases))
print(d)
