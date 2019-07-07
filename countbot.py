# Counting bot
## pulls last comment with a number in a given subreddit and responds with the next number
import praw
import re
from time import sleep
from getpass import getpass
 
def main(r, done):
    comments = r.get_subreddit('INSERT_SUBREDDIT').get_comments()
    last_comment = list(comments)[0]
    try:
        last_no = re.search(r'\d+', last_comment.body).group()
        last_no = int(last_no)
    except ValueError:
        return
 
    if str(last_comment.author) != 'INSERT_USERNAME' \
            and 'bot test' in last_comment.link_title.lower() \
            and last_comment.id not in done:
        last_comment.reply(str(last_no+1))
        print 'Last number: ' + str(last_no)
        print 'replied with: ' + str(last_no+1)
        done.append(last_comment.id)
 
if __name__ == '__main__':
    r = praw.Reddit(user_agent='counting bot')
    r.login(raw_input('Enter Username: ').strip(), getpass('Enter Password: ').strip())
    
    print 'Exit with CTRL-C'
    done =[]
    while True:
        main(r, done)
        sleep(60)
