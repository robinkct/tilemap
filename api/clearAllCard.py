CLEARALLCARD_DESCRIPTION = 'CLEARALLCARD: Remove all card'
CLEARALLCARD_PROMPT = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''
from utils import api_hit
def clear_all_cards_api():
  api_hit("ClearAllCard")

if __name__ == "__main__":
  clear_all_cards_api()
