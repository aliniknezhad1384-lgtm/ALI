print("hahaha")
from rich.console import Console
console = Console()
l : list[tuple[str,list[str],str]] = [
    ('1234?',["a=aqwer",'b=tyui','c=asdf','d=zxcvb'],'A'),
    ('5678?',["a=1234",'b=4312','c=4556','d=7654'],'B'),
    ('assfsg?',["a=lllll",'b=nnnnn','c=dddd','d=ytiegn'],'C')
]
score=0
true_number=0
soal=0
play_again=False
lose=False
def show_menu():
    global play_again
    if play_again==False:
        while True:
            start=input('mikhahid bazi ra shoroo konid?(yes or no)').strip().lower()
            if start==('yes'):
                play_again=True
                break

            elif start==('no'):
                print('thank you for playing')
                play_again=True
                exit()
            else:
                print('invalid input, pls type "yes" or "no" :)')
    else:
        while True:
            start=input('mikhahid bazi ra edame bedahid?(yes or no)').strip().lower()
            if start==('yes'):
                break
            elif start==('no'):
                print('thank you for playing')
                exit()
            else:
                print('invalid input, pls type "yes" or "no" :)')
def play_game():
    global score
    global true_number
    global soal
    global lose
    for i in range(len(l)):
        question=l[i][0]
        answer=l[i][1]
        print(question)
        for j in range(4):
            print(answer[j])
        user_answer:str=input('your choice?').strip().upper()
        if user_answer==l[i][2]:
            console.print('correct',style= "blue")
            score+=2
            print('score +2 =',score)
            true_number+=1
        else:
            console.print('incorrect',style= "red")
            score-=3
            print('score -3 =',score)
        if score<0:
            print('ohhhh...you lose')
            lose=True
            break
    if lose==False:
        print('congrats...you win')
        print((true_number*100)/len(l))
    score=0

while True:
    show_menu()
    play_game()
    true_number=0