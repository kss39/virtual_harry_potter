import game
import hero

def main():
  print('kssnb!')
  print('Testing HP Hogwarts Battle...')

  user_input = input('How many people are playing? ')
  while True:
    try:
      num_player = int(user_input)
      if num_player < 0 or num_player > 4:
        print('Please type a number between 1 and 4.')
        continue
      print(num_player, 'players are playing.')
      break
    except ValueError:
      print('Please enter a valid integer between 1 and 4.')

  print('Setting up game...')

if __name__ == "__main__":
  main()