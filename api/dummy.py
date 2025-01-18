from typing import Optional, List, Dict, Union

try:
    from utils import api_hit, get_hash_id
except:
    from api.utils import api_hit, get_hash_id


def create_dummy_card(
    position: tuple[int, int] = (0, 0),
    text: Optional[str] = None,
    card_id: Optional[str] = None,
    tags: Optional[List[str]] = None
) -> Dict[str, Union[str, int, dict]]:
    """
    創建測試用卡片
    
    參數:
        position: (x, y) 坐標元組，默認 (0, 0)
        text: 卡片文本，默認為 None（將自動生成）
        card_id: 卡片ID，默認為 None（將自動生成）
        tags: 標籤列表，默認為 None
    
    返回:
        dict: 卡片數據
    """
    try:
        x, y = position
        
        # 如果沒有提供文本，生成一個基於ID的文本
        if text is None:
            text = f"Dummy Card at ({x}, {y})"
        # 如果沒有提供ID，生成一個基於位置的ID
        if card_id is None:
            card_id = get_hash_id(f"{text}", algorithm="md5")
            
        # 構建卡片數據
        card_data = {
            "ID": card_id,
            "X": x,
            "Y": y,
            "TextInfo": {
                "Text": text,
            }
        }
        
        # 如果提供了標籤，添加到卡片數據中
        if tags:
            card_data["Tags"] = tags
            
        # 調用API創建卡片
        api_hit("AddCard", card_data, no_return=True)
        print(f"Created dummy card: {card_data}")
        
        return card_data
        
    except Exception as e:
        print(f"Error creating dummy card: {str(e)}")
        return None

def create_dummy_connection(
    start_card_id: str,
    end_card_id: str,
    start_anchor: str = "right",
    end_anchor: str = "left",
    description: Optional[str] = None
) -> Dict[str, str]:
    """
    創建測試用連接
    
    參數:
        start_card_id: 起始卡片ID
        end_card_id: 目標卡片ID
        start_anchor: 起始錨點，默認 "right"
        end_anchor: 目標錨點，默認 "left"
        description: 連接描述，默認為 None
    
    返回:
        dict: 連接數據
    """
    try:
        # 生成連接ID
        connection_id = get_hash_id(f"dummy_conn_{start_card_id}_{end_card_id}", algorithm="md5")
        
        # 如果沒有提供描述，生成一個默認描述
        if description is None:
            description = f"Connection from {start_card_id} to {end_card_id}"
            
        # 構建連接數據
        connection_data = {
            "ID": connection_id,
            "StartCardID": start_card_id,
            "StartAnchor": start_anchor,
            "EndCardID": end_card_id,
            "EndAnchor": end_anchor,
            "Description": description
        }
        
        # 調用API創建連接
        api_hit("AddCardConnection", connection_data, no_return=True)
        print(f"Created dummy connection: {connection_data}")
        
        return connection_data
        
    except Exception as e:
        print(f"Error creating dummy connection: {str(e)}")
        return None

def create_dummy_graph(num_cards: int = 3, layout: str = "horizontal") -> tuple[List[Dict], List[Dict]]:
    """
    創建測試用圖形（多個卡片和連接）
    
    參數:
        num_cards: 要創建的卡片數量，默認 3
        layout: 佈局方式，"horizontal" 或 "vertical"，默認 "horizontal"
    
    返回:
        tuple: (卡片列表, 連接列表)
    """
    try:
        cards = []
        connections = []
        spacing = 250  # 卡片間距
        
        # 創建卡片
        for i in range(num_cards):
            position = (i * spacing, 0) if layout == "horizontal" else (0, i * spacing)
            card = create_dummy_card(
                position=position,
                text=f"Card {i}",
                tags=["dummy", "auto"]
            )
            if card:
                cards.append(card)
        
        # 創建連接（連接相鄰的卡片）
        for i in range(len(cards) - 1):
            if layout == "horizontal":
                start_anchor, end_anchor = "right", "left"
            else:
                start_anchor, end_anchor = "bottom", "top"
                
            connection = create_dummy_connection(
                cards[i]["ID"],
                cards[i + 1]["ID"],
                start_anchor,
                end_anchor,
                f"Connection {i} to {i + 1}"
            )
            if connection:
                connections.append(connection)
        
        return cards, connections
        
    except Exception as e:
        print(f"Error creating dummy graph: {str(e)}")
        return [], []

def remove_dummy_card(card_id: str) -> bool:
    """
    刪除測試用卡片
    
    參數:
        card_id: 要刪除的卡片ID
    
    返回:
        bool: 是否成功刪除
    """
    try:
        # 調用 ClearCardByID API
        api_hit("ClearCardByID", {"ID": card_id}, no_return=True)
        print(f"Removed dummy card: {card_id}")
        return True
        
    except Exception as e:
        print(f"Error removing dummy card {card_id}: {str(e)}")
        return False

def remove_dummy_connection(connection_id: str) -> bool:
    """
    刪除測試用連接
    
    參數:
        connection_id: 要刪除的連接ID
    
    返回:
        bool: 是否成功刪除
    """
    try:
        # 調用 ClearCardConnectionByID API
        api_hit("ClearCardConnectionByID", {"ID": connection_id}, no_return=True)
        print(f"Removed dummy connection: {connection_id}")
        return True
        
    except Exception as e:
        print(f"Error removing dummy connection {connection_id}: {str(e)}")
        return False

def remove_dummy_graph(cards: List[Dict], connections: List[Dict]) -> tuple[bool, bool]:
    """
    刪除測試用圖形（包括所有卡片和連接）
    
    參數:
        cards: 要刪除的卡片列表
        connections: 要刪除的連接列表
    
    返回:
        tuple: (卡片是否全部刪除成功, 連接是否全部刪除成功)
    """
    try:
        # 先刪除所有連接
        connections_success = True
        for connection in connections:
            if not remove_dummy_connection(connection["ID"]):
                connections_success = False
                print(f"Failed to remove connection: {connection['ID']}")
                
        # 再刪除所有卡片
        cards_success = True
        for card in cards:
            if not remove_dummy_card(card["ID"]):
                cards_success = False
                print(f"Failed to remove card: {card['ID']}")
                
        print(f"Removed dummy graph: {len(cards)} cards and {len(connections)} connections")
        return cards_success, connections_success
        
    except Exception as e:
        print(f"Error removing dummy graph: {str(e)}")
        return False, False

if __name__ == "__main__":
    # 測試創建和刪除單個卡片
    print("Testing single card creation and removal...")
    card1 = create_dummy_card((0, 100), "Test Card 1")
    print(f"Created card: {card1}")
    if card1:
        success = remove_dummy_card(card1["ID"])
        print(f"Card removal {'successful' if success else 'failed'}")
    
    # 測試創建和刪除連接
    print("\nTesting connection creation and removal...")
    card1 = create_dummy_card((0, 100), "Card 1")
    card2 = create_dummy_card((250, 100), "Card 2")
    if card1 and card2:
        connection = create_dummy_connection(card1["ID"], card2["ID"])
        print(f"Created connection: {connection}")
        if connection:
            success = remove_dummy_connection(connection["ID"])
            print(f"Connection removal {'successful' if success else 'failed'}")
        
        # 清理卡片
        remove_dummy_card(card1["ID"])
        remove_dummy_card(card2["ID"])
    
    # 測試創建和刪除圖形
    print("\nTesting graph creation and removal...")
    cards, connections = create_dummy_graph(3, "horizontal")
    print(f"Created {len(cards)} cards and {len(connections)} connections")
    if cards and connections:
        cards_success, connections_success = remove_dummy_graph(cards, connections)
        print(f"Graph removal: cards {'successful' if cards_success else 'failed'}, "
              f"connections {'successful' if connections_success else 'failed'}")
