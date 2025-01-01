import requests
import json

from utils import timer
from action import Action

allow_gpt = False

from prompt.addCard import(
    ADDCARD_DESCRIPTION,
    ADDCARD_PROMPT,
)
from prompt.clearAllCard import(
    CLEARALLCARD_DESCRIPTION,
    CLEARALLCARD_PROMPT,
)
from prompt.ai_role import(
    AI_ROLE_PROMPT,
)

from openai import OpenAI

OPENAI_API_KEY = open('api_key', 'r').read()
client = OpenAI(api_key=OPENAI_API_KEY)



description = [ADDCARD_DESCRIPTION, CLEARALLCARD_DESCRIPTION]
dummy_gpt_reply = '''ADDCARD: 人們在「解決問題」時展現的原創性遠超過在「選擇問題」時
ADDCARD: 選擇問題時，即便是聰明的人也可能顯得保守
ADDCARD: 解決時髦問題通常吸引不追隨潮流的人
ADDCARD: 選擇問題的賭注高，可能花費數年時間，而解決問題可能只需幾天'''


guide = AI_ROLE_PROMPT.format("\n".join(description))
print("guide:", guide)


@timer
def chatgpt_do_msg(user_msg):
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
  print(f"gpt reply (dummy={allow_gpt}): {chatgpt_ret}\n")

  action = chatgpt_ret.split(":")[0]
  content = chatgpt_ret.split(": ")[-1]

  a = Action(action, content)
  a.doAction()


### Example
msg = """【流行】
人們在「解決問題」時展現的原創性遠超過在「選擇問題」時。就算是最聰明的人，選擇工作內容時也可能令人驚訝的保守。一些生活中不追隨潮流的人，會忍不住去解決時髦的問題。
人們選擇問題較保守，原因之一是選問題的賭注較大。一個問題可能花費你數年，而探索其解決方案可能只需要幾天。
"""
chatgpt_do_msg(msg)


# msg = "把卡片都刪除"
# chatgpt_do_msg(msg)