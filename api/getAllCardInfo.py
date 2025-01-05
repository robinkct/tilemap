api_name = "GetAllCardInfo"
description = f'{api_name}: Get all card info'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''

from api.utils import api_hit
#from utils import api_hit
#from addCard import run_api as addCard
import json
def run_api():
    ret = api_hit("GetAllCardInfo")
    if ret == "[]":
        print(f"{api_name}: No card")
    return ret

def run_testcase(input=None, expect_output=None):
    ret = run_api()

    if len(ret) != 0:
        return True
    else:
        return None

if __name__ == "__main__":
    #action = "GetAllCardInfo"
    #allcardinfo = api_hit(action)
    allcardinfo = run_api()
    print(allcardinfo)
    #print(allcardinfo)
    #print(type(allcardinfo))
    allcard = json.loads(allcardinfo)
    for card in allcard:
        print(card)