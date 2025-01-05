api_name = "UPDATECARD"
description = f'{api_name}: Update a exist card on the board.'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''

from api.utils import api_hit
from api.getCardInfoByID import run_api as getCardInfoByID

def run_api(id: str, msg: str):
    if type(msg) is str:
        msg = {
            "ID": id,
            "TextInfo": [
                {
                    "Text": msg,
                }
            ]
        }
    api_hit("UpdateCard", msg, no_return=True)

def run_testcase(id=None, expect_output=None):
    if input is None and expect_output is None: # Dummy testcase
        id = "1"
        expect_output = "UpdateCard"

    run_api(id=id, msg=expect_output) # update msg as UpdateCard
    card_info = getCardInfoByID(id)
    update_msg = card_info["TextInfo"][0]["Text"]

    if update_msg == expect_output:
        return True

if __name__ == "__main__":
    id = "1"
    expect_output = "UpdateCard"
    print(f"{api_name}: {run_testcase(id=id, expect_output=expect_output)}")

