import requests
import json
import sys
import os

# 將項目根目錄添加到 Python 路徑
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger import setup_logger

# 创建logger实例
logger = setup_logger(__name__)

url = "https://tilemapwebapi.azurewebsites.net/TextCardApi/{}"

def api_hit(action_name: str, msg: dict = None, no_return: bool = False) -> str:
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
    logger.info(f"API Request - {method} {action_name}")
    logger.info(f"URL: {action_url}")
    logger.info(f"Request Body: {msg}")

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
    logger.info(f"Response Status: {r.status_code}")
    logger.info(f"Response Body: {ret[:200]}..." if len(ret) > 200 else f"Response Body: {ret}")

    if r.status_code != 200:
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