# Import modules

import pyinputplus as pyip
import random 
import time


#numberOfQuestion = 10
#correctAnswer = 0

#for questionNumber in range(numberOfQuestion):
#    #pick two random numbers
#    numb1 = random.randint(0, 9)
#    numb2 = random.randint(0, 9)
#
#    prompt = '#%s: %s x %s = ' % (questionNumber, numb1, numb2)
#    try:
#        # Right answer are treated by allow regex
#        pyip.inputStr(prompt, allowRegexes= ['^%s$' % (numb1 * numb2)],
#                      blockRegexes=[('.*', 'Incorrect!')],
#                      timeout=8, limit=3)
#    except pyip.TimeoutException:
#        print("Time Out!")
 #   except pyip.RetryLimitException:
#        print("Out of tries!")
#    else:
#        print("Correct Answer.")
#        correctAnswer += 1
#    time.sleep(1) # breif pouse to let the see the result.
#print('Score: %s / %s' % (correctAnswer, numberOfQuestion))

''''
class Multiplication():
    def __init__(self):
        self.numberOfQuestion = 10
        self.correctAnswer = 0
    
    def generate_question(self):
        numb1 = random.randint(0, 9)
        numb2 = random.randint(0, 9)
        return numb1, numb2
    
    def askQuestion(self):
        prompt = f"{numb1}*{numb2} = "
        try:
            pyip.inputStr(prompt, allowRegexes= [f"^{numb1 * numb2}$"],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3)
        except pyip.TimeoutException:
            print("Time out!")
            answer = None
        except pyip.RetryLimitException:
            print("Out of tries.")
            answer = None
        return answer

    def runQuiz(self):
        for questionNumber in range(self.numberOfQuestion):
            numb1, numb2 = self.generate_question()
            answer = self.askQuestion(numb1, numb2)
            if answer is not None:
                print("Correct Answer.")
                self.correctAnswer += 1
            time.sleep(1)

    def show(self):
        print(f'Score: {self.correctAnswer / self.correctAnswer}')

if __name__ == "__main__":
    quiz = Multiplication()
    quiz.runQuiz()
    quiz.show()

'''

def name( name):
    print("hello " + name)

print(name("alex"))
print(name("john"))

import random as rd

def return_vlue(answerNumber):
    if answerNumber == 1:
        return "It's certain."
    elif answerNumber == 2:
        return "That's Bullshit."
    elif answerNumber == 3:
        return "That's Crazy."

r = rd.randint(1,3)
fortune = return_vlue(r)
print(fortune)




    











