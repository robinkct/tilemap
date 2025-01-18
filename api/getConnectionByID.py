api_name = "GetCardConnectionInfoByID"
description = f'{api_name}: Get card connection info by ID'
prompt = '''
-Goal-
獲取指定ID的連接信息。

-Step-
1. 提供連接ID
2. API 會返回該連接的詳細信息
3. 如果連接不存在，返回 None

-Example-
# 基本查詢
GetCardConnectionInfoByID?ID=connection_id_to_query

-Expected Output-
- 成功：返回連接信息字典
- 失敗：返回 None
'''

try:
    from utils import api_hit
    from dummy import create_dummy_card, create_dummy_connection, remove_dummy_card
except:
    from api.utils import api_hit
    from api.dummy import create_dummy_card, create_dummy_connection, remove_dummy_card

def run_api(id: str, verbose=True):
    """
    獲取指定ID的連接信息
    
    參數:
        id: 連接ID
        verbose: 是否顯示詳細日誌，默認為 False
    
    返回:
        dict 或 None: 連接信息或 None（如果未找到）
    """
    action_with_id = f"{api_name}?ID={id}"
    ret = api_hit(action_with_id, verbose=verbose)

    if ret is None and verbose:
        print(f"Error: {api_name}: return None (Maybe ID is not found?)")
    return ret

def id_exist(id: str, verbose=False):
    """檢查連接ID是否存在"""
    connection_info = run_api(id=id, verbose=verbose)
    return connection_info is not None

def run_testcase(input=None, expect_output=None):
    """
    測試獲取連接信息功能
    
    參數:
        input: 測試輸入，默認為 None（使用默認測試數據）
        expect_output: 期望輸出，默認為 None
    
    返回:
        bool: 測試是否成功
    """
    try:
        if input is None:
            # 創建測試卡片
            card1 = create_dummy_card(
                position=(0, 100),
                text="Test Card 1",
                tags=["test", "dummy"]
            )
            card2 = create_dummy_card(
                position=(250, 100),
                text="Test Card 2",
                tags=["test", "dummy"]
            )
            
            if card1 and card2:
                # 創建測試連接
                connection = create_dummy_connection(
                    card1["ID"],
                    card2["ID"],
                    description="Test Connection"
                )
                
                if connection:
                    # 測試獲取連接信息
                    connection_info = run_api(connection["ID"], verbose=False)
                    success = (
                        isinstance(connection_info, dict) and 
                        connection_info["ID"] == connection["ID"]
                    )
                    
                    # 清理測試數據
                    remove_dummy_card(card1["ID"])
                    remove_dummy_card(card2["ID"])
                    
                    return success
        else:
            # 使用提供的測試數據
            connection_info = run_api(input, verbose=False)
            return (
                isinstance(connection_info, dict) and 
                connection_info["ID"] == input
            )
            
        return False
        
    except Exception as e:
        print(f"Error in test case: {str(e)}")
        return False

if __name__ == "__main__":
    print(f"== {api_name} ==")
    
    # 運行默認測試用例
    print("Running default testcase...")
    print("Testcase Result:", run_testcase())
    
    # 運行自定義測試用例
    # print("\nRunning custom testcase...")
    # test_input = "custom_test_connection_id"
    # print("Input:", test_input)
    # print("Testcase Result:", run_testcase(input=test_input))