import random

data = [
    {
     'Name':'Instagram',
     'Follower_count':346,
     'Description':'Social media platform',
     'Country':'United States'
    },
    {
      'Name':'Cristiano Ronaldo',
      'Follower_count':215,
      'Description':'Footballer',
      'Country':'Portugal'
    },
    {
      'Name':'Ariana Grande',
      'Follower_count':186,
      'Description':'Singer,actress',
      'Country':'United States'
    },
    {
      'Name':'Triggered Insaan',
      'Follower_count':230,
      'Description':'Youtuber',
      'Country':'India'
    },
    {
      'Name':'Slayy point',
      'Follower_count':183,
      'Description':'Youtuber',
      'Country':'India'
    },
    {
      'Name':'Tony Kakkar',
      'Follower_count':157,
      'Description':'Singer',
      'Country':'India'
    },
    {
      'Name':'Akshay Kumar',
      'Follower_count':246,
      'Description':'Actor',
      'Country':'India'
    }
  ]
#Format the account data in the printable format
def format_data(account):
    account_name = account['Name']
    account_descr = account['Description']
    account_country = account['Country']
    return (account_name,'a',account_descr,'from',account_country)

def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == "A"
    else:
        return user_guess == "B"

score = 0
should_continue = True
account_b = random.choice(data)

while should_continue:
    #Generate a random account from a game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    print("Compare A: ",format_data(account_a) )   
    print("VS") 
    print("Against B: ",format_data(account_b))

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B' \n").upper()

    #Clear the screen
    print("\n" * 20)

    #Check if user is correct
    # -Get follower count of each account
    a_follower_count = account_a["Follower_count"]
    b_follower_count = account_b["Follower_count"]
    # -Use if statement to check if user is correct

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Give user feedback on their guess
    #Score keeping
    if is_correct:
        score += 1
        print("You're right. Current score",score)
    else:
        print("Sorry, You're wrong. Final score",score)
        should_continue = False


#Make the game repeatable

#Making account at position B becoming the account at position A

