#!/usr/bin/env python3

class MyString:
  def __init__(self, value=None):
    self._value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    if self.value.endswith('.'):
      return True
    return False

  def is_question(self):
    if self.value.endswith('?'):
      return True
    return False

  def is_exclamation(self):
    if self.value.endswith('!'):
      return True
    return False
  
  def count_sentences(self):
    if type(self._value) == str:
      updated_string = self._value.replace("?", ".")
      updated_string2 = updated_string.replace("!", ".")
      seperated_list = updated_string2.split(". ")
      print(f'{updated_string2}')
      return len(seperated_list)
    else:
      return 0