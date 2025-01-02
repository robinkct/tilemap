import requests

url = "https://tilemapwebapi.azurewebsites.net/TextCardApi/{}"

def get_action(action_name: str) -> bool:
    if 'get' in action_name.lower():
        return True
    return False

def api_hit(action_name: str, msg: dict = None) -> str:
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
        print(f"Error: {action_name} - {r.status_code}: {r.text}")
        return None
    
    print("Response:\n", ret)
    return ret
