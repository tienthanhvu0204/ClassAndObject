import random

class Flashcard:
    def __init__ (self):
        self.animals = {
            'con ong':'bee',
            'con thỏ':'rabit',
            'con rùa':'turtle',
            'con vịt':'duck',
            'con chó':'dog',
            'con mèo':'cat',
            'con hổ':'tiger',
            'con cá':'fish'
        }

    def quiz(self):
        while True:
            vietnamese, english = random.choice (list(self.animals.items()))
            # %s dùng cho string, %d cho interger, %f cho float, %.2f cho 2 số sau dấu ','
            print ('Tiếng Anh của %s là?' %vietnamese)
            print (f'Tiếng Anh của {vietnamese} là?')
            userAnswer = input ('Nhập đáp án của bạn: ')
            if english == userAnswer.lower():
                print ('Chúc mừng bạn đã trả lời đúng!')
            else:
                print ('Rất tiếc bạn đã trả lời sai!')
            option = input ('Tiếp tục? (y/n): ')
            if option == 'n':
                break
        print ('Kết thúc')
    
fc = Flashcard ()
fc.quiz ()




