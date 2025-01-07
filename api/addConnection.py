api_name = "ADDCONNECTION"
description = f'{api_name}: Add a new connection between two cards.'
prompt = '''
-Goal-
建立兩張卡片之間的連接關係。此 API 允許指定連接的起始點、終點及描述。

-Step-
1. 提供起始卡片 ID 和連接方向（top/bottom/left/right）
2. 提供目標卡片 ID 和連接方向（top/bottom/left/right）
3. 選擇性提供連接的描述文字
4. API 會驗證卡片存在性和方向的合法性
5. 建立連接並生成唯一的連接 ID

-Example-
# 建立從卡片 1 的下側到卡片 2 的上側的連接
{"start_card_id": "1", "start_anchor": "bottom", "end_card_id": "2", "end_anchor": "top", "description": "針對連結的描述"}

# 不帶描述的簡單連接
{"start_card_id": "1", "start_anchor": "bottom", "end_card_id": "2", "end_anchor": "top"}

-Expected Output-
- 成功：無返回值，連接建立成功
- 失敗：拋出 ValueError，可能的錯誤包括：
  * "Start card ID {id} not found" - 起始卡片不存在
  * "End card ID {id} not found" - 目標卡片不存在
  * "Invalid anchor direction: {direction}" - 無效的連接方向
'''
#description = f'{api_name}: Add a new connection between two cards. {prompt}'

try:
    from utils import api_hit
    from getCardInfoByID import id_exist as id_exist
    from addCard import create_dummy_card as create_dummy_card # for testcase
except:
    from api.utils import api_hit
    from api.getCardInfoByID import id_exist as id_exist
    from api.addCard import create_dummy_card as create_dummy_card # for testcase

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


