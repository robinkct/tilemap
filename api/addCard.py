api_name = "ADDCARD"
description = f'{api_name}: Add a new card to the board.'
prompt = '''
-Goal-
在畫布上添加一張新的卡片。此 API 允許指定卡片的位置、內容和其他屬性。

-Step-
1. 提供卡片的位置坐標（X, Y）
2. 提供卡片的文本內容
3. 選擇性提供卡片的其他屬性（ID、標籤等）
4. API 會創建卡片並返回卡片的唯一標識符

-Example-
# 基本卡片創建
{
    "X": 100,
    "Y": 100,
    "TextInfo": {
        "Text": "新卡片"
    }
}

# 帶有完整屬性的卡片
{
    "ID": "custom_id",
    "X": 200,
    "Y": 200,
    "TextInfo": {
        "Text": "完整卡片"
    },
    "Tags": ["important", "draft"]
}

-Expected Output-
- 成功：無返回值，卡片創建成功
- 失敗：拋出異常，可能的錯誤包括：
  * "Invalid position" - 位置坐標無效
  * "Empty text content" - 文本內容為空
  * "Duplicate ID" - ID 已存在
'''

try:
    from utils import api_hit
    from dummy import create_dummy_card, remove_dummy_card
except:
    from api.utils import api_hit
    from api.dummy import create_dummy_card, remove_dummy_card


def run_api(msg: str, verbose=False):
    if type(msg) is str:
        msg = {
            "X": 10,
            "Y": 10,
            "TextInfo": {
                "Text": msg,
            }
        }
    api_hit("AddCard", msg, no_return=True, verbose=verbose)


def run_testcase(input=None, expect_output=None, verbose=False):
    """
    測試添加卡片功能
    
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
                text="Test Card",
                tags=["test", "dummy"]
            )
            
            success = card is not None
            
            # 清理測試數據
            if card:
                remove_dummy_card(card["ID"])
            
            return success
        else:
            # 使用提供的測試數據
            ret = run_api(input)
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
    
    # 運行自定義測試用例
    print("\nRunning custom testcase...")
    test_input = {
        "X": 200,
        "Y": 200,
        "TextInfo": {
            "Text": "Custom test card"
        },
        "Tags": ["test"]
    }
    print("Input:", test_input)
    print("Testcase Result:", run_testcase(input=test_input))


