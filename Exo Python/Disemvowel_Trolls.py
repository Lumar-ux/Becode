import re
str = "This website is for losers LOL!"
def disemvowel(str):
    result = re.findall("[^aeiouAEIOU]", str)
    return(''.join(result))
print(disemvowel(str))