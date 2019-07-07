#Quickly ban users
import praw
import re
from time import sleep
from getpass import getpass

def main(r, done):
	mods = r.get_moderators('INSERT_SUBREDDIT')
	for x in mods:
		r.get_subreddit('INSERT_SUBREDDIT').add_ban(x)
	
	
if __name__ == '__main__':
    r = praw.Reddit(user_agent='modeveryone banner')
    r.login(raw_input('Enter Username: ').strip(), getpass('Enter Password: ').strip())
    
    print 'Exit with CTRL-C'
    done =[]
    while True:
        main(r, done)
        sleep(60)
