api_name = 'ClearCardConnectionByID'
description = f'{api_name}: Remove connection by ID'
prompt = '''
-Goal-
從畫布上刪除指定ID的連接。此 API 用於清理不需要的連接。

-Step-
1. 提供要刪除的連接ID
2. API 會驗證連接是否存在
3. 如果連接存在，則刪除該連接
4. 如果連接不存在，則返回錯誤信息

-Example-
# 基本刪除
{
    "ID": "connection_id_to_delete"
}

-Expected Output-
- 成功：無返回值，連接刪除成功
- 失敗：拋出異常，可能的錯誤包括：
  * "Connection ID not found" - 連接ID不存在
'''

try:
    from utils import api_hit
    from dummy import create_dummy_card, create_dummy_connection, remove_dummy_card
    from getConnectionByID import run_api as getConnectionByID
except:
    from api.utils import api_hit
    from api.dummy import create_dummy_card, create_dummy_connection, remove_dummy_card
    from api.getConnectionByID import run_api as getConnectionByID

def run_api(id: str, verbose=False):
    """
    刪除指定ID的連接
    
    參數:
        id: 要刪除的連接ID
        verbose: 是否顯示詳細日誌，默認為 False
    """
    msg = {"ID": id}
    if getConnectionByID(id, verbose=verbose):
        api_hit(api_name, msg, no_return=True, verbose=verbose)

def run_testcase(input=None, expect_output=None):
    """
    測試刪除連接功能
    
    參數:
        input: 測試輸入，默認為 None（使用默認測試數據）
        expect_output: 期望輸出，默認為 None
    
    返回:
        bool: 測試是否成功
    """
    try:
        if input is None:  # 使用默認測試數據
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
                    # 測試刪除
                    run_api(connection["ID"], verbose=False)
                    # 驗證連接是否已被刪除
                    success = getConnectionByID(connection["ID"], verbose=False) is None
                    
                    # 清理測試卡片
                    remove_dummy_card(card1["ID"])
                    remove_dummy_card(card2["ID"])
                    
                    return success
        else:
            # 使用提供的測試數據
            run_api(input, verbose=False)
            return getConnectionByID(input, verbose=False) is None

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
