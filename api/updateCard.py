api_name = "UPDATECARD"
description = f'{api_name}: Update a exist card on the board.'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''
try:
    from utils import api_hit
    from getCardInfoByID import run_api as getCardInfoByID
except:
    from api.utils import api_hit
    from api.getCardInfoByID import run_api as getCardInfoByID

def run_api(id: str, msg: str):
    
    card_info = getCardInfoByID(id)
    if card_info is None:
        return None

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

    try:
        card_info = getCardInfoByID(id)
        update_msg = card_info["TextInfo"][0]["Text"]
        if update_msg == expect_output:
            return True
    except:
        return None


if __name__ == "__main__":
    print(f"== {api_name} ==")

    testcase_id = "1"
    expect_output = "UpdateCard"
    print(f"Input (Card ID): {testcase_id}, msg: {expect_output}")

    print("Result (Before Update):")
    card_info = getCardInfoByID(testcase_id)
    print("Card Info:", card_info)

    print(f"Testcase result: {run_testcase(id=testcase_id, expect_output=expect_output)}")

    print("Result (After Update):")
    card_info = getCardInfoByID(testcase_id)
    print("Card Info:", card_info)
