#find missind numbers in list of numbers based on min and max

user_list=[]
while True:
    num=input("Enter Number: ")
    try:
        if num=="":
            break
        else:
            num=int(num)
            user_list.append(num)
    except:
        print("Invalid input. enter number only")
missed_numbers=[]
def find_missings():
    min_num=min(user_list)
    max_num=max(user_list)
    for i in range(min_num,max_num+1):
        if i not in user_list:
            missed_numbers.append(i)
    print("\n\n",60*"*","\n","MISSED NUMBERS IN ",min_num,"to",max_num,"range are:\n",missed_numbers,"\n",60*"*")

find_missings()