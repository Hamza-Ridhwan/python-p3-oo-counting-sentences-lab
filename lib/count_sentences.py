#!/usr/bin/env python3
class MyString:
    def __init__(self, value = ''):
       self.value = value
   
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
          print('The value must be a string.')
          self._value = ''  # Assign a default empty string if input is invalid
        else:
            self._value = value

    def is_sentence(self):
       return self.value.endswith('.')
    

    def is_question(self):
       return self.value.endswith('?')
    
    def is_exclamation(self):
       return self.value.endswith('!')    
    
    def count_sentences(self):
       
       replaced_values = self.value.replace('!', '.').replace('?', ".")
    
       
       return len([s for s in replaced_values.split('.') if s.strip()])



string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())
# => 3
       

        
  