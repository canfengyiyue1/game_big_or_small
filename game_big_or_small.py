import random
def roll_dice():
    print("<<< Roll The Dice！>>>")
    point1 = random.randrange(1,7)
    point2 = random.randrange(1,7)
    point3 = random.randrange(1,7)
    points =[point1,point2,point3]
    return points
def roll_result(tatal):
    if (3<=tatal<=10):
        return 'small'
    else:
        return 'big'
def game_start():
    money = 1000
    while(money>0):
        print('<<< Game Starts! >>>')
        user_choice = input('big or small:')
        money_bet = int(input('how much you wanna bet:'))
        while(money_bet>money):
                print('you only have ${}'.format(money))
                money_bet = int(input('how much you wanna bet:'))
        if (user_choice in ['small','big']):
            points = roll_dice()
            tatal = sum(points)
            roll_res = roll_result(tatal)
            if(user_choice == roll_res):
                print('The points are {},you win'.format(points))
                money += money_bet
                print('You have gained ${},now you have ${}'.format(money_bet,money))
            else:
                print('The points are {},you lose'.format(points))
                money -= money_bet
                print('You have lost ${},now you have ${}'.format(money_bet,money))
        else:
            print('Invilid words')
            continue
    print('game,over')

game_start()