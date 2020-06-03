class SpokenLanguage:
    def translate(self, text) -> str:
        raise NotImplementedError()
    
class MathematicsTheLanguageOfTheUniverse(SpokenLanguage):
    def translate(self, text) -> int:
        return len(text)
    
with open('test.py', 'w') as f:
    f.write(In[-1])