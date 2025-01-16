api_name = "ClearCardByID"
description = f'{api_name}: Clear card by ID'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''
try:
    from utils import api_hit
    from addCard import create_dummy_card as create_dummy_card
    from getCardInfoByID import run_api as getCardInfoByID
except:
    from api.utils import api_hit
    from api.addCard import create_dummy_card as create_dummy_card
    from api.getCardInfoByID import run_api as getCardInfoByID

def run_api(id: str):
    msg = {
        "ID": id,
    }
    if getCardInfoByID(id):
        api_hit(api_name, msg, no_return=True)
    else:
        print(f"Error: {api_name}: Card ID not found")

def run_testcase(input=None, expect_output=None):
    if input is None and expect_output is None: # Dummy testcase
        ret = create_dummy_card(0)
    else:
        ret = run_api(input)

    if ret == expect_output and getCardInfoByID(id) is None:
        return True

if __name__ == "__main__":
    print(f"== {api_name} ==")

    create_dummy_card(0)
    msg = "dummy0"
    print("Input:", msg)
    print("Testcase Result:", run_testcase(input=msg))


