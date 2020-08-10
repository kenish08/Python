text = "X-DSPAM-Confidence:    0.8475";
ipos=text.find(":")
p=text[ipos+1:]
print(p)
a=float(p)
print(a)