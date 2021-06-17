'''
default user input is 'scissor'
http://localhost:5000
http://localhost:5000/?user=paper
'''
from flask import Flask, session, request
# in order to save computer generated data, import session
# in order to get user URL input, import request
import random
import os
 
 
app = Flask(__name__)
# to get session working need to set secret_key for app
app.secret_key = os.urandom(32)

def compare(computer, user):
    if computer == user:
        return("It's a tie!")
    elif computer == 'rock':
        if user == 'scissor':
            return("Computer wins!")
        else:
            # user = 'paper'
            return("Human wins!")
    elif computer == 'scissor':
        if user == 'paper':
            return("Computer win!")
        else:
            #user = 'rock'
            return("Human wins!")
    elif computer == 'paper':
        if user == 'rock':
            return("Computer wins!")
        else:
            #user ='scissor'
            return("Human win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissor, try again.")
    
@app.route('/index')
def index():
    return 'Hello, World!'
  
# convert 0, 1, 2 into "scissor, rock or paper"
def srp(number):
    data = ["scissor", "rock", "paper"]
    return data[number]
      
@app.route('/')
def computer():
    # must retrun sting
    # random number 1, 2, 3
    #computer generated data: cgd
    user = request.args.get('user')
    # dedault user input is 'scissor'
    if user == None:
        user = 'scissor'
    cgd = srp((random.randint(0,2)))
    session["computer"] = cgd
    # compare message
    cp = compare(cgd, user)
    result = "default user input is 'scissor', add ?user=rock or ?user=paper to change user input <br /><br />"
    result += "<a href='https://scissor-rock-paper2.herokuapp.com'>scissor</a><br /><br />"
    result += "<a href='https://scissor-rock-paper2.herokuapp.com?user=rock'>rock</a><br /><br />"
    result += "<a href='https://scissor-rock-paper2.herokuapp.com?user=paper'>paper</a><br /><br />"
    result += "computer: " + str(cgd) + " and user: " + str(user) + "<br /><br />"
    result += cp
    return result
 
@app.route('/check')
def check():
    if session.get('computer') != None:
        # get cgd from session
        return session.get('computer')
    else:
        return "no computer session"
         
  
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)