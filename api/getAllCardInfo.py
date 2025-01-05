api_name = "GetAllCardInfo"
description = f'{api_name}: Get all card info'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''

try:
    from utils import api_hit
    from addCard import run_api as addCard
except:
    from api.utils import api_hit
    from api.addCard import run_api as addCard


def run_api():
    ret = api_hit("GetAllCardInfo")
    if ret == "[]":
        print(f"{api_name}: No card")
    return ret

def run_testcase(input=None, expect_output=None):
    ret = run_api()
    #print("getAllCardInfo ret:", type(ret)) # ret is list

    if type(ret) is list:
        return True
    else:
        return None

if __name__ == "__main__":
    print(f"== {api_name}: {run_testcase()} ==")
    card_info_list = run_api()

    print(card_info_list)
    for card in card_info_list:
        print(card)