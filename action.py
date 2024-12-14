
import requests

class Action:
    def __init__(self, action: str, content: str):
        self.action = action
        self.content = content
        self.url_clearAllCard = "https://tilemapwebapi.azurewebsites.net/TextCardApi/ClearAllCard"
        self.url_addCard = "https://tilemapwebapi.azurewebsites.net/TextCardApi/AddCard"
        self.card_cnt = 0

    def doAction(self):
        if self.action == "ADDCARD":
            self.call_addCard(self.content)
        elif self.action == "CLEARALLCARD":
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

def main():
    # Example usage
    action = "AddCard"  # Define your action here
    content = "Sample Card Content"  # Define your content here

    # Create an instance of Action and perform the action
    a = Action(action, content)
    a.doAction()

if __name__ == "__main__":
    main()