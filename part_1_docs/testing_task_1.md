### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # Single '=' should be double '==' for comparison operator
    if card.value = 1:
      return True
    # Missing colon after "else".
    else
      return False
   
  # "def" is misspelled as "dif".
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  


def cards_total(self, cards):
  # "total" is not initialised before it is used in the loop.
  total
  for card in cards:
    total += card.value
    # Concatenation not possible between string and integer. 
    return "You have a total of" + total
  
```
