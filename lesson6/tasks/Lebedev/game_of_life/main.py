from game_manager import GameManager
from initialize_strategy import InitializeRandomStrategy

manager = GameManager()
manager.start(15, 10, InitializeRandomStrategy())
