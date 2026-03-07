# Simple static chatbot
print("Hey!! Steady this side! how can I help you boss?")
l1=['bye','good bye','tata','see you']
l=['hii','hello','hey','what\'s up?']
while True:
    user_input = input("You: ").lower()
    # print(user_input)
    if user_input in l:
        print("Steady: Hello boss... How am I supposed to help you today?")
    elif user_input=="how you are created?":
        print("Steady:I am steady and created by basic python codes!!")
    
    elif user_input=="what is your name?":
        print("Steady:My name is steady as you can see!")
    
    elif "help" in user_input:
        print("Steady:Boss! I do have some boundaries still how can i help you?")

    elif user_input in ['what is god?', 'what is god']:
        print("Steady:God is the creator for me it\'s my developer or somehow I may say... \n God is something like infinite minus known knowledge..")
    
    elif user_input in ['who created you','who created you?']:
        print("Steady:My Creator Skit, IYKYK....😁😁")
    
    elif user_input in ['why python is used in your case?','why python is used in your case']:
        print("Steady:Boss python has a reach library support and convenient....😁😉😎")

    elif user_input in l1:
        print("Steady:I am glad that we had a convo... see you!!! boss🤗🤩😋🥰😍😅☺️")
        break
    else:
        print("Steady: Sorry I didn't got you , Will you please try something else?")