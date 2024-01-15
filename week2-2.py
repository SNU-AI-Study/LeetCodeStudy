class Solution:
    def decodeString(self, s: str) -> str:
  
        tmp = []
        for string in s:
            ans = ""
            if string == ']':
                while tmp[-1] != '[':
                    ans += tmp.pop()
                tmp.pop()
                c = []
                while len(tmp) > 0:
                    if tmp[-1].isdigit():
                        c.append(int(tmp.pop()))
                    else: break
                tmp.extend(list(ans[::-1]) * sum([x*(10**i) for i,x in enumerate(c)]))
            else:
                tmp.append(string)
            
        return "".join(tmp)
