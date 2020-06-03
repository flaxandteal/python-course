class Prisoner:
    def __init__(self, name: str):
        self.name = name
        
    def get_number(self) -> str:
        if self.name == 'Valjean':
            return 24601
        elif self.name == 'Number Six':
            return 6
        elif self.name == 'Bird man of Alcatraz':
            return '#594'
        else:
            return None

        
cell_content = In[-1]