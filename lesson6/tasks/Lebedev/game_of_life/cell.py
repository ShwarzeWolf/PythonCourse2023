class Cell:
    def __init__(self, is_alive: bool) -> None:
        self.is_alive = is_alive
    
    def get_is_alive(self):
        return self.is_alive
    
    def set_is_alive(self, is_alive: bool):
        self.is_alive = is_alive
    
    def __repr__(self) -> str:
        return "■" if self.is_alive else "□"
