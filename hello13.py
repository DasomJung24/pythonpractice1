#This is a birthday match game.
print ('Hello! My name is Alice.')
print ('Whar is your name?')
myName = input()

realDay = 5
print ('Well, ' + myName + ', guess my birthday from 1 to 30.')

guessDay = input()
guessDay = int(guessDay)

if guessDay > realDay :
    print ('Guess an earlier day.')
if guessDay < realDay :
    print ('Guess a later day.')
if guessDay == realDay :
    print ('Good job, ' + myName + '! You guessed my birthday.')
