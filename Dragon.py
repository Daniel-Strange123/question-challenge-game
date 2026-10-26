import time

import random

print("Hello, my name is Favour, an abbreviation for FAST ANALYSIS ON THE VAST OBSERVATION OF UNIVERSAL REALITIES", )
print(" a weird name, right?")
       
print("What might your name be ye mighty observer")


def name(): 
    name = input()

    if name == "Elu":
        print("Game over for you poor man")
    else:
        print("Alright " + name + " Welcome to the dragon realm.")
        print("Here you have to answer a bunch of questions to save the human specie and as for why it's called Dragon realm, don't ask because i know not")
        print("Are you ready? ")
        answer = input("yes/no: ").strip().lower()
        while answer not in ("yes", "no"):  
            answer = input("answer only yes or no: ").strip().lower()
        if answer == "yes":
            print("Loading...")
            time.sleep(5)

            score = 0
            print("it's a multiple choice question, based on the most important field ever developed by man...SCIENCE")
            answer = input("Who discovered gravity? A.Sir Isaac Newton. B.Albert Einstein. C.Nikola Tesla. D.Richard Feynman. ")

            if answer == "A":
                print("Correct!!!")
                score = score +1
            else:
                print ("Incorrect!!!")

            answer = input("Who is the father of quantum mechanics? A.Werner Heisenberg. B.Niels Bohr. C.Max Planck. D.Robert J.Oppenheimer. ")
                
            if answer == "C":
                print("Brilliant!!!, you just might be humanity's saviour.")
                score = score +1
            else:
                print("loooserrrr...Hahahahahaha")

            answer = input("What is the derivative of acceleration with respect to time. A.Velocity. B.Jerk. C.Momentum. D.Action. ")

            if answer == "B":
                print("Woooooah, you,re moving like Lionel Messi now. A genius you might be")
                score = score +1
            else:
                print("Nope...")
                
            answer = input("Which theoretical particle travels at light speed. A.Protons. B.Muons. C.Electrons. D.Neutrinos. ")
                
            if answer == "D":
                print("That is right!")
                score = score +1    
            else:
                 print("You got that one wrong...")

            answer = input("What is the mathematical value of pi.A.2.14.B.4.14.C.3.14.D.5.14. ")

            if answer == "C":
                print("Accurate!!!!")
                score = score +1
            else:
                print("It's basic math whacko, looooser")

            print("Quiz finished")
                
            print("Your score is: " + str(score) + "/5")

            if score == 5:
                print("Congrats for ye have saved humanity, you have survived annhilation for the next 1000 years")
            else:
                print("You have doomed your specie human and you all shall perish...Hahahahahahahaha")
                return
        else:
            print("Okay, bye!!")
        return
    return
name()

    










    



 
                

                              
        
    
