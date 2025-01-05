api_name = "GetAllCardInfo"
description = f'{api_name}: Get all card info'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''

try:
    from utils import api_hit, remove_duplicate
    from addCard import run_api as addCard
except:
    from api.utils import api_hit, remove_duplicate
    from api.addCard import run_api as addCard


def run_api():
    card_info_list = api_hit("GetAllCardInfo")
    card_info_list = remove_duplicate(card_info_list)
    if card_info_list == "[]":
        print(f"{api_name}: No card")
    return card_info_list

def run_testcase(input=None, expect_output=None):
    ret = run_api()
    #print("getAllCardInfo ret:", type(ret)) # ret is list

    if type(ret) is list:
        return True
    else:
        return None

if __name__ == "__main__":
    print(f"== {api_name} ==")

    print("Result:")
    card_info_list = run_api()
    for card in card_info_list:
        print(card)

    print("Testcase Result:", run_testcase())