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
def run_api(id: str):
    action_with_id = "".join([api_name, "?ID={}".format(id)])

    ret = api_hit(action_with_id)

    # todo: if id is not found
    #if ret == "[]":
    #    print(f"{api_name}: No card")
    return ret

def run_testcase(input=None, expect_output=None):
    testcase_id = "1"
    card_info = run_api(id=testcase_id)

    # card_info example
    # card_info = {
    #     'ID': '1', 'X': 10.0, 'Y': 10.0, 'Title': None, 
    #     'TextInfo': [{'Text': 'AddCard1', 'ID': 'XX'}]
    # }
    if type(card_info) is dict and card_info["ID"]==testcase_id:
        return True
    else:
        return None

if __name__ == "__main__":

    testcase_id = "1"
    card_info = run_api(id=testcase_id)
    print(type(card_info), card_info)

    print(run_testcase()) # expect True