import requests
import json
from collections import deque
from openai import OpenAI

from utils import timer, load_description_from_folder
#from utils import timer, load_description_from_folder, load_prompt_from_folder
from logger import setup_logger
from action import Action
from api.ai_role import AI_ROLE_PROMPT

OPENAI_API_KEY = open('api_key', 'r').read()
client = OpenAI(api_key=OPENAI_API_KEY)

description_dict = load_description_from_folder('api')
descriptions = [description_dict[name] for name in description_dict]

#prompt_dict = load_prompt_from_folder('api')
#prompts = [prompt_dict[name] for name in prompt_dict]

dummy_gpt_reply = '''ADDCARD: 人們在「解決問題」時展現的原創性遠超過在「選擇問題」時
ADDCARD: 選擇問題時，即便是聰明的人也可能顯得保守
ADDCARD: 解決時髦問題通常吸引不追隨潮流的人
ADDCARD: 選擇問題的賭注高，可能花費數年時間，而解決問題可能只需幾天'''

getinfo_prompt = "如果需要先取得資料，請先執行 getAllCardInfo 取得資料，再執行其他動作。"
getinfo_example = "# 範例 0 \n## 敘述\n敘述:\'幫我合併卡片中所有「流行」的卡片。\'\n## 輸出  \nGetAllCardInfo: "
api_list = "\n".join(descriptions)

# 创建logger实例
logger = setup_logger(__name__)

@timer
def chatgpt_do_msg(user_msg, allow_gpt=False, launch_api=False, getinfo=True):
    if getinfo: 
        guide = AI_ROLE_PROMPT.format(api_list=api_list, getinfo_prompt=getinfo_prompt, getinfo_example=getinfo_example)
    else:
        guide = AI_ROLE_PROMPT.format(api_list=api_list, getinfo_prompt="", getinfo_example="")
    print("guide:", guide)

    if allow_gpt:
        completion = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
            {"role": "assistant", "content": guide},
            {"role": "user", "content": user_msg}
            ]
        )
        chatgpt_ret = completion.choices[0].message.content
    else:
        chatgpt_ret = dummy_gpt_reply
    logger.info(f"gpt reply (allow_gpt={allow_gpt}) (launch_api={launch_api}): \n{chatgpt_ret}\n")
    

    actions_queue = deque(chatgpt_ret.split("\n"))
    while actions_queue:
        reply = actions_queue.popleft()

        action = reply.split(":")[0]
        content = reply.split(": ")[-1]

        if launch_api:
            a = Action(action, content)
            ret = a.doAction()
            if ret:
                return ret

def chatgpt_do_msg_with_getinfo(msg, allow_gpt, launch_api, getinfo):
  if getinfo:
    ret = chatgpt_do_msg(msg, allow_gpt, launch_api, getinfo)

  print("ret msg:", ret)

  if ret:
    msg_and_retinfo = msg + "\n" + str(ret)

    print("【 Msg and GetAllCardInfo 】", msg_and_retinfo)
    chatgpt_do_msg(msg_and_retinfo, allow_gpt, launch_api, False)

if __name__ == "__main__":
  msg = """【流行】
  人們在「解決問題」時展現的原創性遠超過在「選擇問題」時。就算是最聰明的人，選擇工作內容時也可能令人驚訝的保守。一些生活中不追隨潮流的人，會忍不住去解決時髦的問題。
  人們選擇問題較保守，原因之一是選問題的賭注較大。一個問題可能花費你數年，而探索其解決方案可能只需要幾天。
  """

  allow_gpt = True
  launch_api = True
  getinfo = True

  chatgpt_do_msg_with_getinfo(msg, allow_gpt, launch_api, getinfo)

# msg = "把卡片都刪除"
# chatgpt_do_msg(msg)