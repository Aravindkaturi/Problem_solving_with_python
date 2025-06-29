#Written by K.Aravind
s="oneminusthree"
d={"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","zero":"0","plus":"+","minus":"-"}
r=[]
j=0
for i in range(1,len(s)+1):
    if s[j:i] in d:
        r.append(d[s[j:i]])
        j=i
r=''.join(r)
e=eval(r)
e=str(e)
for digit in e:
    for word, val in d.items():
        if val == digit:
            if digit == "-":
                print("negative",end="")
            else:
                print(word,end="")