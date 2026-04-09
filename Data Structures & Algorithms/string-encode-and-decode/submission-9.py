class Solution:

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
        count_str = 0
        cur_str_len = ''
        cur_str = ''
        while i < len(s):
            if s[i] == '#' and not is_count:
                cur_str_len = int(cur_str_len)
                if cur_str_len == 0:
                    decoded_strs.append("")
                    cur_str_len = ''
                    is_count = False
                else:
                    is_count = True
                i += 1
                continue
            
            if is_count:

                if count_str < cur_str_len:
                    count_str += 1
                    cur_str += s[i]
                
                if count_str == cur_str_len:
                    is_count = False
                    count_str = 0
                    decoded_strs.append(cur_str)
                    cur_str_len = ''
                    cur_str = ''
                    
            else:
                cur_str_len += s[i]
            i += 1
            

        return decoded_strs
