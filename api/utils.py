import requests
import json
import sys
import os
import hashlib
from typing import Literal


# 將項目根目錄添加到 Python 路徑
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger import setup_logger

# 创建logger实例
logger = setup_logger(__name__)

url = "https://tilemapwebapi.azurewebsites.net/TextCardApi/{}"

def api_hit(action_name: str, 
            msg: dict = None, 
            no_return: bool = False, 
            verbose: bool = True) -> str:
    '''
    action_name: API name
    msg: for API contains input value
    no_return: for API contains no return value

    return: 
      None: for API contains no return value
      json: for API contains return value
    '''
    def get_action(action_name: str) -> bool:
        if 'get' in action_name.lower():
            return True
        return False

    action_url = url.format(action_name)
    method = "GET" if get_action(action_name) else "POST"
    
    # 記錄請求信息
    if verbose:
        logger.info(f"API Request - {method} {action_name}")
        #logger.info(f"URL: {action_url}")
        #logger.info(f"Request Body: {msg}")

    if get_action(action_name): # GET
        r = requests.get(
            url=action_url,
            json=msg,
        )
    else: # POST
        r = requests.post(
            url=action_url,
            json=msg,
        )
    r.encoding = "utf_8"  # other encoding: utf_8 utf_16 gbk gb18030 big5hkscs
    ret = r.text

    # 記錄響應狀態和結果
    if verbose:
        logger.info(f"Response Status: {r.status_code}")
#    logger.info(f"Response Body: {ret[:200]}..." if len(ret) > 200 else f"Response Body: {ret}")

    if r.status_code != 200:
        if verbose:
            logger.error(f"Failed Status: {r.status_code} - {action_name}: {r.text}")
        return None
    
    if no_return: # for API contains no return value
        return None
    
    try:
        ret_json = json.loads(ret)
        return ret_json
    except:
        logger.error(f"{__file__} - {action_name} - {ret}")
        return ret

def remove_duplicate(list_obj):
    seen = set()
    unique_list = []
    for obj in list_obj:
        key = obj['ID']
        if key not in seen:
            seen.add(key)
            unique_list.append(obj)
    return unique_list

def get_hash_id(text: str, algorithm: Literal["sha256", "md5"] = "md5") -> str:
    """
    將輸入字串轉換為指定算法的 hash
    
    參數:
        text: 要進行哈希的字串
        algorithm: 使用的哈希算法，可選 "sha256" 或 "md5"，默認為 "sha256"
    
    返回:
        str: 哈希值（小寫十六進制）
            - SHA-256: 64位
            - MD5: 32位
    """
    try:
        # 確保輸入是字串類型
        text = str(text)
        
        # 選擇哈希算法
        if algorithm.lower() == "md5":
            hash_obj = hashlib.md5()
        elif algorithm.lower() == "sha256":
            hash_obj = hashlib.sha256()
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}. Use 'sha256' or 'md5'")
        
        # 將字串編碼為 UTF-8 並更新 hash
        hash_obj.update(text.encode('utf-8'))
        # 獲取十六進制的 hash 值
        hash_id = hash_obj.hexdigest()
        
        logger.debug(f"Generated {algorithm.upper()} hash for '{text}': {hash_id}")
        return hash_id
    except Exception as e:
        logger.error(f"Error generating {algorithm.upper()} hash for '{text}': {str(e)}")
        return None


if __name__ == "__main__":
    # 測試兩種哈希算法
    test_text = "test"
    print(f"Convert to hash: {test_text}")
    print(f"SHA-256: {get_hash_id(test_text)}")
    print(f"MD5: {get_hash_id(test_text, algorithm='md5')}")