api_name = "ADDCARD"
ADDCARD_DESCRIPTION = f'{api_name}: Add a new card to the board.'
ADDCARD_PROMPT = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''

from api.utils import api_hit

def add_card_api(msg: str):
  if type(msg) is str:
    msg = {
      "X": 10,
      "Y": 10,
      "TextInfo": {
        "Text": msg,
      }
  }
  api_hit("AddCard", msg)


def create_dummy():
  input  = {
    "ID": '1',
    "X": 10,
    "Y": 10,
    "TextInfo": {
      "Text": "AddCard1",
    }
  }
  expect_output = None
  return (input, expect_output)

def run_testcase(input=None, expect_output=None):
  if input is None and expect_output is None: # Dummy testcase
    input, output = create_dummy()

  ret = add_card_api(input)
  if ret == expect_output:
    return True

if __name__ == "__main__":

  msg = {
    "ID": '2',
    "X": 200,
    "Y": 200,
    "TextInfo": {
      "Text": "AddCard2",
    }
  }
  run_testcase(input=msg)

