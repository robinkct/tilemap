api_name = "UPDATECONNECTION"
description = f'{api_name}: Update a exist connection.'
prompt = '''
-Goal-

-Step-

-Example-

-Expected Output-

'''
try:
    from utils import api_hit
    from dummy import create_dummy_card, create_dummy_connection, remove_dummy_connection, remove_dummy_card
    from getConnectionByID import run_api as getConnectionByID
except:
    from api.utils import api_hit
    from api.dummy import create_dummy_card, create_dummy_connection, remove_dummy_connection, remove_dummy_card
    from api.getConnectionByID import run_api as getConnectionByID

def run_api(id: str, description: str, verbose=False):
    msg = {
        "ID": id,
        "Description": description,
    }
    if id is None or description is None:
        return None

    api_hit("UpdateCardConnection", msg, no_return=True, verbose=verbose)

def run_testcase(input=None, expect_output=None, verbose=False):
    """
    測試更新連接功能
    
    參數:
        input: 測試輸入（連接ID），默認為 None（使用默認測試數據）
        expect_output: 期望的更新描述，默認為 None
        verbose: 是否輸出詳細信息，默認為 False
    
    返回:
        bool: 測試是否成功
    """
    try:
        if input is None and expect_output is None:  # 使用默認測試數據
            # 首先创建两个测试卡片
            start_card = create_dummy_card()
            end_card = create_dummy_card()
            
            # 使用卡片ID创建测试连接
            connection = create_dummy_connection(start_card["ID"], end_card["ID"])
            
            if verbose:
                print(f"Created test connection: {connection['ID']}")
            
            if connection:
                # 更新連接描述
                new_description = "Updated Test Connection"
                run_api(id=connection["ID"], description=new_description, verbose=verbose)
                
                # 驗證更新結果
                updated_connection = getConnectionByID(connection["ID"])
                success = (updated_connection is not None and 
                         updated_connection["Description"] == new_description)
                
                if verbose:
                    print(f"Updated connection description: {new_description}")
                
                # 清理測試數據
                remove_dummy_connection(connection["ID"])
                remove_dummy_card(start_card["ID"])
                remove_dummy_card(end_card["ID"])
                
                return success
            
            # 如果連接創建失敗，也要清理卡片
            remove_dummy_card(start_card["ID"])
            remove_dummy_card(end_card["ID"])
            return False
            
        else:
            # 使用提供的測試數據
            if verbose:
                print(f"Updating connection {input} with description: {expect_output}")
            
            run_api(id=input, description=expect_output, verbose=verbose)
            
            # 驗證更新結果
            updated_connection = getConnectionByID(input)
            success = (updated_connection is not None and 
                      updated_connection["Description"] == expect_output)
            
            return success
            
    except Exception as e:
        if verbose:
            print(f"Error in test case: {str(e)}")
        return False

if __name__ == "__main__":
    print(f"== {api_name} ==")
    verbose = False  # 設置為 True 可以看到詳細輸出
    
    # 運行默認測試用例
    print("Running default testcase...")
    print("Result:", run_testcase(verbose=verbose))
    
    # 運行自定義測試用例
    # print("\nRunning custom testcase...")
    # start_card = create_dummy_card()
    # end_card = create_dummy_card()
    
    # connection = create_dummy_connection(start_card["ID"], end_card["ID"])
    
    # if connection:
    #     new_description = "Custom updated description"
    #     result = run_testcase(
    #         input=connection["ID"],
    #         expect_output=new_description,
    #         verbose=verbose
    #     )
    #     print("Result:", result)
        
    #     # 清理測試數據
    #     remove_dummy_connection(connection["ID"])
    #     remove_dummy_card(start_card["ID"])
    #     remove_dummy_card(end_card["ID"])
    # else:
    #     remove_dummy_card(start_card["ID"])
    #     remove_dummy_card(end_card["ID"])
    #     print("Failed to create test connection")
