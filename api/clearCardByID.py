api_name = "ClearCardByID"
description = f'{api_name}: Clear card by ID'
prompt = '''
-Goal-
從畫布上刪除指定ID的卡片。此 API 用於清理不需要的卡片。

-Step-
1. 提供要刪除的卡片ID
2. API 會驗證卡片是否存在
3. 如果卡片存在，則刪除該卡片
4. 如果卡片不存在，則返回錯誤信息

-Example-
# 基本刪除
{
    "ID": "card_id_to_delete"
}

-Expected Output-
- 成功：無返回值，卡片刪除成功
- 失敗：拋出異常，可能的錯誤包括：
  * "Card ID not found" - 卡片ID不存在
'''

try:
    from utils import api_hit
    from dummy import create_dummy_card
    from getCardInfoByID import run_api as getCardInfoByID
except:
    from api.utils import api_hit
    from api.dummy import create_dummy_card
    from api.getCardInfoByID import run_api as getCardInfoByID

def run_api(id: str, verbose=False):
    """
    刪除指定ID的卡片
    
    參數:
        id: 要刪除的卡片ID
        verbose: 是否顯示詳細日誌，默認為 False
    """
    msg = {"ID": id}
    if getCardInfoByID(id, verbose=verbose):
        api_hit(api_name, msg, no_return=True, verbose=verbose)

def run_testcase(input=None, expect_output=None, verbose=False):
    """
    測試刪除卡片功能
    
    參數:
        input: 測試輸入，默認為 None（使用默認測試數據）
        expect_output: 期望輸出，默認為 None
    
    返回:
        bool: 測試是否成功
    """
    try:
        if input is None:  # 使用默認測試數據
            # 創建測試卡片
            card = create_dummy_card(
                position=(100, 100),
                text="Test Card for Deletion",
                tags=["test", "dummy"]
            )
            
            if card:
                # 測試刪除
                run_api(card["ID"], verbose=False)
                # 驗證卡片是否已被刪除
                success = getCardInfoByID(card["ID"], verbose=False) is None
                return success
        else:
            # 使用提供的測試數據
            run_api(input, verbose=False)
            return getCardInfoByID(input, verbose=False) is None

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
#    print("\nRunning custom testcase...")
#    test_input = "custom_test_card_id"
#    print("Input:", test_input)
#    print("Testcase Result:", run_testcase(input=test_input))


