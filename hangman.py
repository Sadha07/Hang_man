import random
import hangman_design as ds
import words

print(ds.logo)
print(ds.version)
rep='y'
while(rep=='y'):
    word_choice = random.choice(words.words)
    key=[]
    life=6
    end_of_game = False
    for i in range(len(word_choice)):
        key.append("_")
    while( not end_of_game):
        letter=input("\nGuess a letter:").lower()
        for i in range(len(word_choice)):
            if(letter==word_choice[i]):
                key[i]=letter
        if(letter not in key):
            print(ds.stages[life])
            if(life==0):
                print("You lose")
                end_of_game = True
                continue
            life-=1
        for i in key:
            print(i,end=" ")
        print("\n")
        if "_" not in key:
            end_of_game = True
            print("You win.")
    
    rep=input("Do you want to play again?(y/n):")
else:
    print("Thank you")