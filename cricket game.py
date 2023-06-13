import random
import time
l=["pakistan","bangladesh","newzealand","westindies","england","australia","srilanka"]
match=["5 overs"]
b= random.choice(match)
print(f"Welcome to the {b} CRICKET Match ")
City= input("Enter the city of the Stadium : ").title()
Venue=input("Enter the Stadium of the match : ").title()
TeamA=input("Enter the home Team name : ").title()
print(l)
TeamB=input("Enter the Opposite Team from given upper list: ").title()
TeamAcaptain= input("Enter the Captain name of the Home team: ").title()
# TeamBcaptain= input("Enter the Captain name of the Opposite team: ").title()

time.sleep(3)
print()
print((f"""Welcome to the {Venue} for the Greatest Rivalry of Paytm {b} Trophy
between {TeamA} and {TeamB}.

Pitch report- Pitch has been looking Good for Balling conditions.

Welcome {City} Now it's time for the toss between the two greatest teams of the world
{TeamA} and {TeamB}.
{TeamAcaptain} has the coin in his hand.
He flips the coins.....
 """))
a= "Heads"
b= "Tails"
ask = input("""Choose
a) Heads
b) Tails
Enter the number of the coins: """)
toss = ["Heads","Tails"]
r1="tails"
r= random.choice(toss)
print("The coin in flipping in the air...")
print()
time.sleep(3)
if ask == "a":
    print(f"{a} is the call.... And {r} it is!")
else:
    print(f"{b} is the call.... And {r1} it is!")

listInd=["Rohit Sharma","Shubman Gill","Virat  Kohli","Surya  Yadav","Hardik Pandy",
        "Ravi  Jadeja","Kuldip Yadav","Yuzi  Chahal","Mohmd  Shami","Mohmd  Siraj","Umran  Malik"]
listAus = ["David Warner", "Travis Head", "Marnus Labuschagne", "Steve Smith", "Marcus Stoinis", "Glenn Maxwell",
           "Alex Carey", "Cameron Green", "Pat Cummins", "Adam Zampa", "Mitchell Starc"]
listEng = ['Jos Buttler','Jason Roy', 'Moeen Ali', 'Sam Billings', 'Sam Curran', 'Chris Jordan', 'Dawid Malan',
           'Adil Rashid', 'Olly Stone', 'David Willey', 'Chris Woakes']
listNz= ['Devon Conway','Henry Nicholls','Kane Williamson','Daryl Mitchell','Michael Bracewell'
    ,'Tom Blundell','Tom Latham','Blair Tickner','Matt Henry','Neil Wagner','Tim Southee']
listBan= [ 'Litton Das', 'Mushfiqur Rahim', 'Shakib Al Hasan', 'Mahmudullah', 'Mustafizur Rahman', 'Taskin Ahmed',
         'Mehidy Hasan Miraz','Ebadot Hossain', 'Najmul Hossain Shanto', 'Shoriful Islam', 'Hasan Mahmud']
listSri= ['Dasun Shanaka','Pathum Nissanka','Kusal Mendis','Charith Asalanka','Dhananjaya de Silva',
       'Bhanuka Rajapaksa','Wanindu Hasaranga','Chamika Karunaratne','Dushmantha Chameera','Asitha Fernando','Maheesh Theekshana']
listWi = ['Kraigg Brathwaite', 'Jermaine Blackwood', 'Shamarh Brook', 'Tagenarine Chanderpaul', 'Roston Chase', 'Devon Thomas', 'Jason Holder',
          'Kyle Mayers', 'Alzarri Joseph', 'Kemar Roach', 'Jayden Seales']
listPak = ['Babar Azam', 'Shadab Khan', 'Asif Ali', 'Fakhar Zaman', 'Haris Rauf',
          'Iftikhar Ahmed', 'Khushdil Shah', 'Mohammad Haris', 'Mohammad Nawaz', 'Mohammad Rizwan', 'Shaheen Shah Afridi']

if (a == r and b != r1):
        print(f"{TeamB} has won the toss and they decided to bat first")
elif (b== r and a != r1):
        print(f"{TeamA} has won the toss and they decided to ball first")

def Teams():
        print("\nNow introducing playing XI of the both Teams")
        print()
        time.sleep(5)
        if (TeamA== "India" and TeamB == "Australia"):
            print("India Playing XI   V/S   Australia Playing XI")
            for j,i in zip(listInd,listAus):
                print(f"{j}             {i}")
        elif (TeamA== "India" and TeamB == "Pakistan"):
            print("India Playing XI   V/S   Pakistan Playing XI")
            for j,i in zip(listInd,listPak):
                print(f"{j}             {i}")
        elif (TeamA== "India" and TeamB == "Bangladesh"):
            print("India Playing XI   V/S   Bangladesh Playing XI")
            for j,i in zip(listInd,listBan):
                print(f"{j}             {i}")
        elif (TeamA== "India" and TeamB == "Newzealand"):
            print("India Playing XI   V/S   Newzealand Playing XI")
            for j,i in zip(listInd,listNz):
                print(f"{j}             {i}")
        elif (TeamA== "India" and TeamB == "Srilanka"):
            print("India Playing XI   V/S   Srilanka Playing XI")
            for j,i in zip(listInd,listSri):
                print(f"{j}             {i}")
        elif (TeamA== "India" and TeamB == "England"):
            print("India Playing XI   V/S   England Playing XI")
            for j,i in zip(listInd,listEng):
                print(f"{j}             {i}")
        elif (TeamA== "India" and TeamB == "Westindies"):
            print("India Playing XI   V/S   Westindies Playing XI")
            for j,i in zip(listInd,listWi):
                print(f"{j}             {i}")
        else:
            print("Please Enter the name of that team only which is given inside the list")

        print("""
Lets Begin the Match
Umpires and Players boths walking on the field!!

Get Ready for the Big Event
        """)

        e= random.choice(listInd)
        f= random.choice(listInd)
        g= random.choice(listAus)
        h = random.choice(listBan)
        k = random.choice(listNz)
        l = random.choice(listSri)
        m = random.choice(listWi)
        n = random.choice(listPak)
        o = random.choice(listEng)
        if (TeamA == "India") and (TeamB== "Australia"):
            print(f"""
{e} and {f} are the openers for team India
{g} is the Bowler for the australia.
                    """)
        elif (TeamA == "India") and (TeamB == "Bangladesh"):
            print(f"""
{e} and {f} are the openers for team India
{h} is the Bowler for the Bangladesh.
                    """)
        elif (TeamA == "India") and (TeamB == "Newzealand"):
            print(f"""
{e} and {f} are the openers for team India
{k} is the Bowler for the Newzealand.
                            """)
        elif (TeamA == "India") and (TeamB == "Srilanka"):
            print(f"""
{e} and {f} are the openers for team India
{l} is the Bowler for the Srilanka.
                            """)
        elif (TeamA == "India") and (TeamB == "Westindies"):
            print(f"""
{e} and {f} are the openers for team India
{m} is the Bowler for the Westindies.
                            """)
        elif (TeamA == "India") and (TeamB == "Pakistan"):
            print(f"""
{e} and {f} are the openers for team India
{n} is the Bowler for the Pakistan.
                            """)
        elif (TeamA == "India") and (TeamB == "England"):
            print(f"""
{e} and {f} are the openers for team India
{o} is the Bowler for the England.
                            """)

# bat = [0, 1, 2, 3, 4, 6]
# time.sleep(3)
# print("Play shots with bat for only these given lists", bat)

def batball():
        bat = [0, 1, 2, 3, 4, 6]

        points= [536,450,600,900,750,723,640,890,1000]
        target=[98,85,90,81,66,70,89,59,94]
        # target =[1,6]
        region=["long on","long off","mid-wicket","fine-leg","square leg","square cut","cover",
                    "third-man","over wicket keeper","straight"]
        ball = [ "short ball","bouncer", "Good length", "Yorker", "Little bit short", "full toss", "on-off stump",
                    "leg side", ]
        x = [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        balls_left = 30
        b = []
        e = random.choice(listInd)
        f = random.choice(listInd)
        q = random.choice(target)
        wicket = 7
        print(f"{TeamB} has scored {q-1} runs in their 5 overs")
        print(f"{TeamA} needs {q} runs to win with {wicket} Wickets in Hand in their 5 overs\n")
        print(f"{q} runs needs in {balls_left} balls left . LETS  GOOO!")
        print("Play shots with bat for only these given lists", bat)
        for i in x:
                if wicket==0 or sum(b)>=q or sum(b)==-1:
                    break
                a = int(input("play the shot: "))
                j = random.choice(ball)
                f = random.choice(region)
                p = random.choice(points)
                o = random.choice(listEng)
                # q = random.choice(target)

                balls_left-=1
                runs_left =q-sum(b)
            # for i,j in zip(bat,ball):
                print(f"Bowler bowls a {j} delivery and Batsman plays for {f} region ")
                if j ==("Good length") or j==("Yorker") :
                    print("OOps! He is OUT!Thats a huge mistake by Batsman in this crucial time")
                    print("Next batsman is coming some cheers out for fans")
                    b.append(0)
                    wicket-=1
                    # print("Total runs you have made is",sum(b))
                    # print(f"You have [{balls_left}] balls left in this innings\n")
                elif a == 1 or a == 2 or a == 3 or a == 4 or a == 6 or a==0:
                    # print(f"lovely shot for {a}  runs")
                    if a == 1 or a == 2:
                        print(f"Its lovely shot for {a} runs")
                        # print(f"You have [{balls_left}] balls left in this innings\n")
                        b.append(a)
                    elif a==0:
                        print(f"He looks determined here plays solid defence")
                        # print(f"You have [{balls_left}] balls left in this innings\n")
                    elif a == 3 :
                        print(f"its put into a gap for {a} runs beautiul shot")
                        # print(f"You have [{balls_left}] balls left in this innings\n")
                        b.append(a)
                    elif a == 4:
                        print(f"Wow!! Now this gone like a tracer Bullets for {a} runs")
                        # print(f"You have [{balls_left}] balls left in this innings\n")
                        b.append(a)
                    elif a == 6:
                        print(f"Oohhh my Goodness It's huge six over the roof of stadium for {a} runs ")
                        # print(f"You have [{balls_left}] balls left in this innings\n")
                        b.append(a)
                else:
                    print("Bad luck! you played wrong shot! you are OUT you made", sum(b),"runs")
                    # print(f"You have [{balls_left}] balls left in this innings")
                    wicket-=1
                print(f"You have made total {sum(b)} runs in your innings with {wicket} wickets left")
                print(f"You need {q-sum(b)} in {balls_left} balls left with the RR : {(q-(sum(b)))/5}\n")
        if sum(b)==(q-1):
                print(f"""Match has been Tied! Both the team had fought so well! 
Both teams has made {q-1} runs""")
        elif (balls_left==0 and q>sum(b)):
            print(f"You Loose by {(q-sum(b))-1} runs with 0 balls left")
            print(f"You got {-p} points ")
        elif q <= (sum(b)):
                print(f"CONGRATULATIONS !  You Won the Game by [{balls_left}] balls left")
                print(f"You got {p} points ")
        elif q > (sum(b)):
                print(f"OOPS!!! You loose the game by {runs_left-1} runs")
                print(f"you got {-p} points")
        elif wicket==0:
                print(f"OOPS!!! You got all-out and looses the game by {runs_left-1} runs")
                print(f"you got {-p} points")




def playagain(z):

            if int(z) == 0:
                print("Thanks for playing!")
                return True
            else:
                # print("total runs you have made is",sum(z))
                return False
Teams()
# batball()
while True:
    # Teams()
    batball()
    print()

    if playagain(int(input("Tap to chase it again(Y==1/N==0):  "))):
        break
