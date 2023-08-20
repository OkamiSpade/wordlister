import time
ban=f"""
	\x1b[1;91m
\x1b[1;92m
\x1b[1;96m
█░█░█ █▀█ █▀█ █▀▄ █░░ █ █▀ ▀█▀   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
▀▄▀▄▀ █▄█ █▀▄ █▄▀ █▄▄ █ ▄█ ░█░   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄
\x1b[1;93m
\x1b[1;92m         OWNER BY OKAMISPADE
\x1b[1;91m-----------------------------------------------
\x1b[1;97m> Author : Spade Dy
\x1b[1;97m> Github : https://github.com/OkamiSpade (Original Code)
\x1b[1;97m> Facebok: Karque12
\x1b[1;97m> Version: Wordlist Generator
\x1b[0;97m-----------------------------------------------
"""
print(ban)
print("Fill in the complete data of the target below")
a = input(" Name: ")
file = open(a+".txt", 'w')
b=input(" Middle: ")
c=input(" Last: ")
d=input(" Nickname: ")
e=input("Date of birth > ex: |DDMMYY|: ")
f=e[0:2]
g=e[2:4]
h=e[4:]
print("If you are no having extra list, just SKIP :v")
i=input("Favorite[object/color/place]: ")
j=input("Pet nam: ")
k=input("2 add extra number > ex: |224505|: ")
print('Create...')
l=k[0:2]
m=k[2:4]
n=k[4:]
file.write("%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s" % (a,c,a,b,b,a,b,c,c,a,c,b,a,a,b,b,c,c,a,d,b,d,c,d,d,d,d,a,d,b,d,c,a,e,a,f,a,g,a,h,b,e,b,f,b,g,b,h,c,e,c,f,c,g,c,h,d,e,d,f,d,g,d,h,e,a,f,a,g,a,h,a,e,b,f,b,g,b,h,b,e,c,f,c,g,c,h,c,e,d,f,d,g,d,h,d,d,d,a,f,g,a,g,h,f,g,f,h,f,f,g,f,g,h,g,g,h,f,h,g,h,h,h,g,f,a,g,h,b,f,g,b,g,h,c,f,g,c,g,h,d,f,g,d,g,h,a,i,a,j,a,k,i,e,i,j,i,k,b,i,b,j,b,k,c,i,c,j,c,k,e,k,j,a,j,b,j,c,j,d,j,j,k,a,k,b,k,c,k,d,k,k,i,l,i,m,i,n,j,l,j,m,j,n,j,k))
wg = 0
while (wg < 10000):
	wg = wg + 1
	file.write(a + str(wg) + '\n')
en = 0
while (en < 10000):
	en = en + 1
	file.write(i + str(en) + '\n')
word = 0
while (word < 10000):
	word = word + 1
	file.write(d + str(word) + '\n')
gen = 0
while (gen < 10000):
	gen = gen + 1
	file.write(j + str(gen) + '\n')
file.close()
time.sleep(1.5)
print("Saved: %s.txt" %a)
