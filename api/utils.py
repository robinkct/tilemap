import requests
import json
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

#    print("Action:", action_name)
#    print("Status:", r)

    if r.status_code != 200:
        print(f"Error: Failed Status: {r.status_code} - {action_name}: {r.text}")
        return None
    
    if no_return: # for API contains no return value
        return None
    
    #print("Response:\n", ret)
    try:
        ret_json = json.loads(ret)
        return ret_json
    except:
        print(f"Error: {__file__} - {action_name} - {ret}")
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