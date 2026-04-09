class Solution:

    def encode(self, strs: List[str]) -> str:
        print(len(strs))
        if len(strs) == 0: return 'é'
        return 'ñ'.join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return ['']
        if s == 'é': return []
        return s.split('ñ')
