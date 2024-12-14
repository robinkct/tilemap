from openai import OpenAI

OPENAI_API_KEY = open('api_key', 'r').read()
client = OpenAI(api_key=OPENAI_API_KEY)
import requests
import json

class Action:
    def __init__(self, action: str, content: str):
        self.action = action
        self.content = content
        self.url_clearAllCard = "https://tilemapwebapi.azurewebsites.net/TextCardApi/ClearAllCard"
        self.url_addCard = "https://tilemapwebapi.azurewebsites.net/TextCardApi/AddCard"
        self.card_cnt = 0

    def doAction(self):
        if self.action == "AddCard":
            self.call_addCard(self.content)
        elif self.action == "ClearAllCard":
            self.call_clearAllCard()
        else:
            print(f"Unknown action: {self.action}")

    def call_clearAllCard(self):
        try:
            response = requests.post(
                url=self.url_clearAllCard,
                json={},
            )
            response.raise_for_status()
            print("All cards cleared successfully.")
        except requests.RequestException as e:
            print(f"Error clearing cards: {e}")

    def call_addCard(self, text):
        demo_format = {
            "X": 100 + 100 * self.card_cnt,
            "Y": 100 + 100 * self.card_cnt,
            "TextInfo": {
                "Text": text,
            },
        }
        self.card_cnt += 1
        try:
            response = requests.post(
                url=self.url_addCard,
                json=demo_format,
            )
            response.raise_for_status()
            print("Card added successfully.")
        except requests.RequestException as e:
            print(f"Error adding card: {e}")


# Example usage
action = "AddCard"  # Define your action here
content = "Sample Card Content"  # Define your content here

# Create an instance of Action and perform the action
a = Action(action, content)
a.doAction()


guide = '''
AddCard：將卡片拆解並呼叫 API 產生卡片
ClearAllCard：清除所有卡片
輸出格式：
{function}: {input text}
ex:
input: "我想學數學"
AddCard: {我想學數學}

input: "刪除所有卡片"
output: ClearAllCard:{None}

規則：
將內容拆解成一張張卡片，並選擇 AddCard。
若內容中明確要求清空或刪除所有卡片時，選擇 ClearAllCard。
'''


def chatgpt_do_msg(user_msg):
  completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
      {"role": "assistant", "content": guide},
      {"role": "user", "content": user_msg}
    ]
  )
  chatgpt_ret = completion.choices[0].message.content
  print(chatgpt_ret)
#   action = chatgpt_ret.split(":")[0]
#   content = chatgpt_ret.split(": ")[-1]

#   a = Action(action, content)
#   a.doAction()


### Example
msg = """【流行】
人們在「解決問題」時展現的原創性遠超過在「選擇問題」時。就算是最聰明的人，選擇工作內容時也可能令人驚訝的保守。一些生活中不追隨潮流的人，會忍不住去解決時髦的問題。
人們選擇問題較保守，原因之一是選問題的賭注較大。一個問題可能花費你數年，而探索其解決方案可能只需要幾天。
"""

chatgpt_do_msg(msg)


# msg = "把卡片都刪除"
# chatgpt_do_msg(msg)