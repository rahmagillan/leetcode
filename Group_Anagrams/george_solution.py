class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        result = []
        
        for st in strs:
            count = 0
            myarr = [0] * 26
            for char in st:
                count += ord(char)
                myarr[ord(char)-97] += 1
                
            if count in mydict:
                tmp = mydict[count]
                i = 0
                while i < len(tmp):
                    if tmp[i] == myarr:
                        tmp[i+1]
                        tmp[i+1].append(st)
                        break
                    i+=2
                if i >= len(tmp):
                    tmp.append(myarr)
                    tmp.append([st])
            else:
                mydict[count] = [myarr, [st]]
        
        for i in mydict.values():
            count = 0
            while count < len(i):
                result.append(i[count+1])
                count+=2
        return result
