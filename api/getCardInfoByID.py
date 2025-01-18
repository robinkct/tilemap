api_name = "GetCardInfoByID"
description = f'{api_name}: Get card info by ID'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''

try:
    from utils import api_hit
except:
    from api.utils import api_hit

import json
def run_api(id: str, verbose=True):
    action_with_id = "".join([api_name, "?ID={}".format(id)])

    ret = api_hit(action_with_id, verbose=verbose)

    if ret is None:
        if verbose:
            print(f"Error: {api_name}: return None (Maybe ID is not found?)")
    return ret

def id_exist(id: str, verbose=False):
    card_info = run_api(id=id, verbose=verbose)
    if card_info is None:
        return False
    else:
        return True

def run_testcase(input=None, expect_output=None):
    if input is None:
        testcase_id = "dummy0"
    else:
        testcase_id = input

    if id_exist(testcase_id):
        card_info = run_api(id=testcase_id)

    # card_info example
    # card_info = {
    #     'ID': 'dummy', 'X': 10.0, 'Y': 10.0, 'Title': None, 
    #     'TextInfo': [{'Text': 'dummy0', 'ID': 'XX'}]
    # }
    if type(card_info) is dict and card_info["ID"]==testcase_id:
        return True
    
    return None

if __name__ == "__main__":
    print(f"== {api_name} ==")

    testcase_id = "dummy0"
    print("Input (Card ID):", testcase_id)

    print("Result:")
    card_info = run_api(id=testcase_id)
    print(type(card_info), card_info)

    print("Testcase Result:", run_testcase(input=testcase_id))