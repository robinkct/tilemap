api_name = "ADDCARD"
description = f'{api_name}: Add a new card to the board.'
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


def run_api(msg: str):
    if type(msg) is str:
        msg = {
            "X": 10,
            "Y": 10,
            "TextInfo": {
                "Text": msg,
            }
        }
    api_hit("AddCard", msg, no_return=True)

def create_dummy_card(i: int):
    dummy_msg = {
        "ID": 'dummy{}'.format(i),
        "X": i*250,
        "Y": i*250,
        "TextInfo": {
            "Text": "dummy{}".format(i),
        }
    }
    run_api(dummy_msg)

def run_testcase(input=None, expect_output=None):
    if input is None and expect_output is None: # Dummy testcase
        ret = create_dummy_card(0)
    else:
        ret = run_api(input)

    if ret == expect_output:
        return True

if __name__ == "__main__":
    print(f"== {api_name} ==")

    msg = {
        "ID": '1',
        "X": 200,
        "Y": 200,
        "TextInfo": {
            "Text": "AddCard2",
        }
    }
    print("Input:", msg)
    print("Testcase Result:", run_testcase(input=msg))


