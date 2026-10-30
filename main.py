from rich.console import Console
console = Console()
l : list[tuple[str,list[str],str]] = [
    ('bozorg tarin sayare manzoome shamsi kodam ast?',["a=zamin",'b=merikh','c=moshtari','d=zohal'],'C'),
    ('kodam keshvar mabda ekhtera pitza ast?',["a=france",'b=italia','c=spain','d=germany'],'B'),
    ('sari tarin heyvan khoshki kodam ast?',["a=shir",'b=asb','c=yoozpalang','d=gorg'],'C')
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
def golden_question():
    global score
    global lose
    print('mikhahid soal talaii ra entekhab konid?')
    player_answer=input('agar dorost bashad: +10 score , dar sorat javab eshtebah mostaghiman hazf mishavid)').strip().upper()
    if player_answer=='YES':
        print('kodam heyvan beyn gozine ha toolani tarin omr ra darad?\na=phil\nb=lakposht ghoolpeykar\nc=shir\nd=asb')
        golden_answer=input('your choice?').strip().upper()
        if golden_answer=='B':
            console.print( 'correct' , style = "yellow")
            score+=10
            print('score +10 =',score)
        else:
            print('ohhhh...you lose')
            lose=True
            exit()


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
        user_answer=input('your choice?').strip().upper()
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
    golden_question()  

while True:
    show_menu()
    play_game()
    true_number=0