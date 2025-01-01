CLEARALLCARD_DESCRIPTION = 'CLEARALLCARD: Remove all card'
CLEARALLCARD_PROMPT = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''
from api.utils import api_hit

def clear_all_cards_api():
  api_hit("ClearAllCard")

def run_testcase(input=None, expect_output=None):
  ret = clear_all_cards_api()
  if ret == expect_output:
    return True

if __name__ == "__main__":
  run_testcase()