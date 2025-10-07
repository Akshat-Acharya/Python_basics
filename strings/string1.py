s1="Hello"
s2=""
for i in range (len(s1)) :
    if(97<=ord(s1[i])<=122) :
        s2=s2+((chr)(ord(s1[i])-32))
    else :
        s2=s2+s1[i];
print(s2)
s3=""
for i in s1 :
    if 65<=ord(i)<=90 :
        s3=s3+((chr)(ord(i)+32))
    else :
        s3=s3+i
print(s3)