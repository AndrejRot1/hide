
import string;

class hide():
    def __init__(self,message):
        letters = string.ascii_lowercase
        self.message = message
        self.new_message = ''

        for index in self.message:
            if (index in letters) == True:
                self.new_message = self.new_message + letters[letters.index(index)+1]
            else:
                self.new_message = self.new_message + index

        print(self.new_message)

    def save_to_file(self):
        f = open('hide.txt','a')
        f.write(self.new_message + '\n')
        f.close()

    def unhide(self):
        letters = string.ascii_lowercase
        self.unhide_new_message = ''
        for index in self.new_message:
            if (index in letters) == True:
                self.unhide_new_message = self.unhide_new_message + letters[letters.index(index)-1]
            else:
                self.unhide_new_message = self.unhide_new_message + index
        
        print(self.unhide_new_message)

    def read_file(self):
        f = open('hide.txt','r')
        lines = f.readlines()
        for message in lines:
            self.new_message = message
            self.unhide()
        f.close()
        

    
        
        



            

