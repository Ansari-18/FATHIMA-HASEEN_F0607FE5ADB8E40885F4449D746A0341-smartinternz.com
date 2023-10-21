



Challenges1.1 & 1.2/ PYTHON-unit1/ Fundamental of Coding & Cloud #naanmudhalvan #smartinternz #2023
9.2K views · 1 month ago...more

Answers dotcom
8.4K

Subscribe

82


Share

Save

Report

Comments36
BEAST BOY YT
Thank you akka❤
Up next
Auto-play


10:00
UPLOAD & SUBMIT CHALLENGES 1.1 & 1.2 │GITHUB │#naanmudhalvan │Fundamentals of Coding & Cloud #2023
Answers dotcom•5.3K views

Shorts
Don't worry about Naan Mudhalvan Login Problem/ Use the above login Method
120K views

How to get Project Steps and Guide through Naan Mudhalvan Portal | #naanmudhalvan #tableau #tamil
6.6K views

Focus on one programming language 🙌 #programming #coding
318K views

Leo🔥Expectation Super-ஆ இருக்கு🔥🔥எதிர்பார்ப்பை எகிறவைத்த Keerthy Suresh
600K views

Gulab Jamun 🤤👌#sweet #shorts #bangalorethamizhanvlogs
2.8K views

Leo 🔥 Home Work பண்ண Help பண்ணு Vijay அப்பா 🥰
520K views

salam ya Mahdi🥺|Now we are helpless|come soon.✊🥺😥 #islam #islamic #islamicstatus #imammahdi #muslim
2.6M views

தஜ்ஜாலை விட்டு பாதுகாப்பு பெற இதை செய்யுங்கள். அவன் வரப்போகிறான் #Shorts
822 views

"Leo படத்தை Stop பண்ணிட்டாங்க" 😲 Mimicry Aadhavan Shocking Video
29K views

"Leo 1000 கோடி வராது" Open-ஆ சொன்ன Producer Lalit
2.5K views

"Vijay கூட நடிச்சது, Lokesh Kanagaraj என்ன வச்சுதான்.." George Maryan | Throwback
42K views

Leo Exclusive 🔥VIJAY நெத்திய காட்டுங்க, பொட்டு வெச்சு விட்ட Trisha 🥰
403K views

Hey, Same pinch ❤️ Archana பார்த்து Sweet Shock ஆன Tamannaah
977K views

10 videos
FundamentalsOfCodingAndCloud
Answers dotcom

7:51
How to Apply Malaysia Visa Online For Singapore Long-Term Pass Holders/PR
Discover_SG
New
11 views

3:27
2ndYear/Cyber Security(Module6)/MICROSOFT OFFICE ESSENTIALS/DigitalSkillsForEmployability
Answers dotcom•3.1K views

8 videos
Naan Mudhalvan Project Tasks
Bit to Yottabyte

21:49
Procedure to submit task in naan mudhalvan for third year. Github.
Digital Market•1.8K views

9:49
Incredible😭FREE AI APP-Speak ENGLISH Fluently LIKE PRO in 30DAYS🔥
Curious Freaks•86K views

0:45
இங்கிலீஷ் பேசுனாலும் தமிழன்டா - ஆயுத பூஜை Special - October 23, Monday 4 PM - Promo - Zee Tamil
Zee Tamil
New
17K views

8:29
Challenge 2.1 / UNIT 2 / Fundamental of Coding & Cloud #naanmudhalvan #smartinternz #2023
Answers dotcom•6.3K views

6:39
வேகமாக உடல் எடை குறைக்க | Weight loss Treatment in Tamil | Dr. A.VENI | RockFort Neuro Centre
Neuro Doctor Tamil•138K views

10:33
Zero Skills😳Just 20Mins/Day👉EARN MONEY EASILY from Home-💰🔥
Curious Freaks•155K views

7:01
UPLOAD CHALLENGES📱│GITHUB │MOBILE PHONE│#naanmudhalvan │Fundamentals of Coding & Cloud #2023
Answers dotcom•5.1K views


Comments
36


Add a comment…


Pinned by Answers dotcom
@answersdotcom-bg2lx
1 month ago
# 1.1 Implement a recursive function to calculate the factorial of a given number
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))

# 1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.

year = 2023

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))