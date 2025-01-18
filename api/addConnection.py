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
    from getCardInfoByID import id_exist
    from dummy import create_dummy_card, create_dummy_connection, remove_dummy_connection, remove_dummy_card  # 改用 dummy.py 中的函數
except:
    from api.utils import api_hit
    from api.getCardInfoByID import id_exist
    from api.dummy import create_dummy_card, create_dummy_connection, remove_dummy_connection, remove_dummy_card  # 改用 dummy.py 中的函數

anchor_directions = ["top", "left", "right", "bottom"]

def run_api(start_card_id: str, start_anchor: str, end_card_id: str, end_anchor: str, description: str = None, verbose=False):
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
    api_hit("AddCardConnection", msg, no_return=True, verbose=verbose)


def run_testcase(input=None, expect_output=None, verbose=False):
    """
    測試添加連接功能
    
    參數:
        input: 測試輸入，默認為 None（使用默認測試數據）
        expect_output: 期望輸出，默認為 None
    
    返回:
        bool: 測試是否成功
    """
    try:
        if input is None:  # 使用默認測試數據
            # 創建兩張測試卡片
            card1 = create_dummy_card(
                position=(0, 0),
                text="Test Card 1",
                tags=["test", "dummy"]
            )
            card2 = create_dummy_card(
                position=(400, 0),
                text="Test Card 2",
                tags=["test", "dummy"]
            )
            
            if card1 and card2:
                # 創建連接
                connection = create_dummy_connection(
                    start_card_id=card1["ID"],
                    end_card_id=card2["ID"],
                    start_anchor="right",
                    end_anchor="left",
                    description="Test connection between cards"
                )
                
                success = connection is not None
                
                # 清理測試數據
                if connection:
                    remove_dummy_connection(connection["ID"])
                remove_dummy_card(card1["ID"])
                remove_dummy_card(card2["ID"])
                
                return success
        else:
            # 使用提供的測試數據
            ret = run_api(**input)
            return ret == expect_output

        return False
        
    except Exception as e:
        print(f"Error in test case: {str(e)}")
        return False

if __name__ == "__main__":
    print(f"== {api_name} ==")
    
    # 運行默認測試用例
    print("Running default testcase...")
    print("Testcase Result:", run_testcase())


