class Solution:
    #O(n) for both
    #Note that in encode does not use += in strings, and in encode, instead of use += to build the encode string,
    #i use a list to add each encoded string, and finally, use join to chain all the encoded strings
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""

        encoded_list = []
        for s in strs:
            encoded_list.append(f"{len(s)}#{s}")
        
        return ''.join(encoded_list)

    #In decode, i use comprension lists to split both length of the string, and the decoded string
    #this takes O(k) where k is the size of the substring, but K <= N, N = len(s), so, the complexity is still O(n)
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

