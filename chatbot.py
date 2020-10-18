"""
This program is based on simple design on chatbot...
1.The bot starts with greeting, self introduction   and ask for the name of the person
2.The bot will greet and welcome the person
3.Bot will ask the person want to do, it will offer a choice of things based upon the bot design
4.It will respond to users to input correctly
"""
import random
from datetime import datetime
import requests
def Greeting():
    #a list of responses from bot
    res=["Nice to see you.\nI can help you do some calulations and you can know information about a movie",
    "\nIts wonderful to see to you.\nIam a chat bot,I have 2 special features.\nI can help you do some calulations and you can know information about a movie"]
    #to select a response at random and to return that
    return random.choice(res)



# greets the person based on the time of the day
def time_Of_The_Day():
    current_time=datetime.now()
    time_Greeting="Good Morning"
    if current_time.hour>21:
        time_Greeting="Good Night"
    elif current_time.hour>16 and current_time.hour<22:
        time_Greeting="Good Evening"
    elif current_time.hour>=12 and current_time.hour<17:
        time_Greeting="Good AfterNoon"
    
    return time_Greeting



#bot welcomes the person with his name 
def welcome_Greeting():
    name=input("May I know your name:")
    print(f"{time_Of_The_Day()},{name},{Greeting()}")




def menu():
    print("1.Calculate an expression")
    print("2.Know about a Movie")
    print("3.End this chat")
    print("-----------------------------------------------------")
    try:
        return int(input("Enter your choice from [1-3]:"))
    except:
        print("Oops,you must enter a number from [1-3]")
def evaluator():
    expression=input("Enter your expression: ")
    try:
        print("Result of the expression: ",eval(expression))
    except Exception as e:
        print(e)



def movie_Info():
    
    movie_name=input("Enter the movie name: ")
    data=requests.get("https://www.omdbapi.com/?t="+str(movie_name)+"&apikey=6637725e").json()
    try:
        data=requests.get("https://www.omdbapi.com/?t="+str(movie_name)+"&apikey=6637725e").json()
        print("Imdb rating: "+str(data["imdbRating"])
        +"\n"+"Runtime :"+str(data["Runtime"])+"\n"
        +"Actors :"+str(data["Actors"])+"\n"
        +"Director :"+str(data["Director"])+"\n"
        +"Plot :"+str(data["Plot"])+"\n")
    except:
        print("Sorry,this movie is not present in our database")



def bot():
    welcome_Greeting()
    choice=menu()
    while choice!=3:
        if(choice==1):
            evaluator()
        elif(choice==2):
            movie_Info()
        else:
            print("Oops,I didnt get it!")
        choice=menu()

bot()
