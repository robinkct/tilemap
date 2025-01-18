api_name = "GetCardInfoByID"
description = f'{api_name}: Get card info by ID'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''

try:
    from utils import api_hit
    from dummy import create_dummy_card, remove_dummy_card
except:
    from api.utils import api_hit
    from api.dummy import create_dummy_card, remove_dummy_card

import json
def run_api(id: str, verbose=True):
    action_with_id = "".join([api_name, "?ID={}".format(id)])

    ret = api_hit(action_with_id, verbose=verbose)

    if ret is None:
        if verbose:
            print(f"Error: {api_name}: return None (Maybe ID is not found?)")
    return ret

def id_exist(id: str, verbose=False):
    card_info = run_api(id=id, verbose=verbose)
    if card_info is None:
        return False
    else:
        return True

def run_testcase(input=None, expect_output=None, verbose=False):
    """
    測試獲取卡片信息功能
    
    參數:
        input: 測試輸入，默認為 None（使用默認測試數據）
        expect_output: 期望輸出，默認為 None
    
    返回:
        bool: 測試是否成功
    """
    try:
        if input is None:
            # 創建測試卡片
            test_card = create_dummy_card(
                position=(100, 100),
                text="Test Card",
                tags=["test", "dummy"]
            )
            
            if test_card:
                # 測試獲取卡片信息
                card_info = run_api(test_card["ID"], verbose=verbose)
                success = (
                    isinstance(card_info, dict) and 
                    card_info["ID"] == test_card["ID"]
                )
                
                # 清理測試數據
                remove_dummy_card(test_card["ID"])
                
                return success
        else:
            # 使用提供的測試數據
            card_info = run_api(input, verbose=verbose)
            return (
                isinstance(card_info, dict) and 
                card_info["ID"] == input
            )
            
        return False
        
    except Exception as e:
        if verbose:
            print(f"Error in test case: {str(e)}")
        return False

if __name__ == "__main__":
    print(f"== {api_name} ==")
    
    # 運行默認測試用例
    print("Running default testcase...")
    print("Testcase Result:", run_testcase(verbose=True))
    
    # 運行自定義測試用例
    # print("\nRunning custom testcase...")
    # test_input = "custom_test_card_id"
    # print("Input:", test_input)
    # print("Testcase Result:", run_testcase(input=test_input, verbose=True))