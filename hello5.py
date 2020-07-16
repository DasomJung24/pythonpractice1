#This is birthday match game.
print ('Hello! My name is Alice.')
print ('What is your name?')
myName = input()
realDay = 5
print ('Well, ' + myName + ', guess my birthday from 1 to 30.')

guessDay = input()
guessDay = int(guessDay)
if guessDay != realDay:
    print ('Your guess is wrong.')
if guessDay == realDay:
    print ('Excellent! ' + myName +', You guessed my birthday.')
