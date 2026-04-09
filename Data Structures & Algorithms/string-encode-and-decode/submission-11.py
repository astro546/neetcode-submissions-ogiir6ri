class Solution:
    #O(n^2) Because the operator += takes O(n) to execute because strings in python are inmutable
    #So, when += executes, actually python creates a copy of the string with the character inserted, and deletes the old string
    #In another languages, if the += works in mutable strings, the += takes O(1), and the overall time complexity is O(n)
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""

        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"
        
        return encoded_str 

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "": return []
        if s == "0#": return [""]

        i = 0
        decoded_strs = []
        is_count = False
        cur_len = 0
        while i < len(s):
            if not is_count:
                mark_idx = s.find('#', i)
                cur_len = int(s[i:mark_idx])
                if cur_len == 0: 
                    decoded_strs.append("")
                    is_count = False
                else:
                    is_count = True
                i = mark_idx + 1

            else:
                decoded_strs.append(s[i: i + cur_len ])
                is_count = False
                i += cur_len
        
        return decoded_strs

