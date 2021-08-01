import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    user = user.lower()
    computer = random.choice(['r', 'p', 's'])

    if user==computer:
        return "You and computer have bth chosen {}. It's a tie.".format(user, computer)
    if is_win(user, computer):
        return "You chosse this {} and the computer choose this {} Congrats Your Win!!.".format(user, computer)
    return "You choose this {} and the computer choose this {} Sorry You lost!!". format(user, computer)

def is_win(player, Opponent):
    if (player == 'r' and Opponent == 's') or (player == 'p' and Opponent == 'r') or (player == 's' and Opponent == 'p'):
        return True
    return False

if __name__ == '__main__':
    print(play())