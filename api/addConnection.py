api_name = "ADDCONNECTION"
description = f'{api_name}: Add a new connection between two cards.'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''
try:
    from utils import api_hit
    from getCardInfoByID import id_exist as id_exist
    from addCard import run_api as addCard # for testcase
except:
    from api.utils import api_hit
    from api.getCardInfoByID import id_exist as id_exist
    from api.addCard import run_api as addCard # for testcase

anchor_directions = ["top", "left", "right", "bottom"]

def run_api(start_card_id: str, start_anchor: str, end_card_id: str, end_anchor: str, description: str = None):
    if not id_exist(start_card_id):
        raise ValueError(f"Start card ID {start_card_id} not found")
    if not id_exist(end_card_id):
        raise ValueError(f"End card ID {end_card_id} not found")
    if start_anchor not in anchor_directions or end_anchor not in anchor_directions:
        raise ValueError(f"Invalid anchor direction: {start_anchor} or {end_anchor}")

    # 1. create connection
    msg = {
        "StartCardID":start_card_id,
        "StartAnchor":start_anchor,
        "EndCardID":end_card_id,
        "EndAnchor": end_anchor,
        "ID": "link"+str(start_card_id)+"_"+str(end_card_id),
        "Description": description if description is not None else ""
    }
    api_hit("AddCardConnection", msg, no_return=True)


def run_testcase(input=None, expect_output=None):
    def create_dummy_card(i: int):
        dummy_msg = {
            "ID": 'dummy{}'.format(i),
            "X": i*300,
            "Y": i*300,
            "TextInfo": {
                "Text": "dummy{}".format(i),
            }
        }
        addCard(dummy_msg)

    # 1. create dummy cards
    create_dummy_card(0)
    create_dummy_card(1)

    # 2. run api
    start_card_id = "dummy0"
    start_anchor = "right"
    end_card_id = "dummy1"
    end_anchor = "left"
    description = "connection between dummy0 and dummy1"
    ret = run_api(start_card_id, start_anchor, end_card_id, end_anchor, description)

    if ret == expect_output:
        return True

if __name__ == "__main__":
    print(f"== {api_name} ==")

    # print("Input:", msg)
    
    print("Testcase Result:", run_testcase())


