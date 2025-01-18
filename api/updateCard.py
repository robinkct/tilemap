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
    from dummy import create_dummy_card, remove_dummy_card
    from getCardInfoByID import id_exist as id_exist
    from getCardInfoByID import run_api as getCardInfoByID
except:
    from api.utils import api_hit
    from api.dummy import create_dummy_card, remove_dummy_card
    from api.getCardInfoByID import id_exist as id_exist
    from api.getCardInfoByID import run_api as getCardInfoByID

def run_api(id: str, msg: str, verbose=False):
    if not id_exist(id):
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
    api_hit("UpdateCard", msg, no_return=True, verbose=verbose)

def run_testcase(input=None, expect_output=None, verbose=False):
    """
    測試更新卡片功能
    
    參數:
        input: 測試輸入，默認為 None（使用默認測試數據）
        expect_output: 期望的更新內容，默認為 None
    
    返回:
        bool: 測試是否成功
    """
    try:
        if input is None and expect_output is None:  # 使用默認測試數據
            # 創建測試卡片
            card = create_dummy_card(
                position=(100, 100),
                text="Original Text",
            )
            
            if not card:
                return False
                
            # 更新卡片內容
            update_text = "Updated Text"
            run_api(id=card["ID"], msg=update_text, verbose=verbose)
            
            # 驗證更新結果
            updated_card = getCardInfoByID(card["ID"])
            success = (updated_card is not None and 
                       update_text in str(updated_card))
            
            # 清理測試數據
            remove_dummy_card(card["ID"])
            
            return success
            
        else:
            # 使用提供的測試數據
            run_api(id=input, msg=expect_output, verbose=verbose)
            
            # 驗證更新結果
            updated_card = getCardInfoByID(input)
            return (updated_card is not None and 
                   updated_card["TextInfo"]["Text"] == expect_output)
            
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
    # # 創建一個測試卡片
    # test_card = create_dummy_card(
    #     position=(200, 200),
    #     text="Original test card", 
    #     tags=["test"]
    # )
    
    # if test_card:
    #     # 更新卡片內容
    #     new_text = "Updated test card"
    #     print(f"Original card: {test_card}")
    #     print(f"Updating text to: {new_text}")
        
    #     # 運行測試
    #     result = run_testcase(input=test_card["ID"], expect_output=new_text)
    #     print("Update Result:", result)
        
    #     # 清理測試卡片
    #     remove_dummy_card(test_card["ID"])
    # else:
    #     print("Failed to create test card")
