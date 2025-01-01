ADDCARD_DESCRIPTION = 'ADDCARD: Add a new card to the board.'
ADDCARD_PROMPT = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''

from api.util import api_hit

def add_card_api(msg: str):
  api_hit("AddCard", msg)

if __name__ == "__main__":

  action = "AddCard"
  msg1 = {
    "ID": '1',
    "X": 10,
    "Y": 10,
    "TextInfo": {
      "Text": "AddCard1",
    }
  }
  msg2 = {
    "ID": '2',
    "X": 200,
    "Y": 200,
    "TextInfo": {
      "Text": "AddCard2",
    }
  }
  add_card_api(msg1)
  add_card_api(msg2)
