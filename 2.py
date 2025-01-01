#String --> Duplicates Removal

def removeDuplicates(s):
    result=[]
    s1=set()

    for item in s:
        if item not in s1:
            result.append(item)
            s1.add(item)
    return "".join(result)

s="geEksforGEeks"
print(removeDuplicates(s))