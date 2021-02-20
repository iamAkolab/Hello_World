import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

#get request status code 2000
print(res.status_code)

#print length of 
print(len(res.text))

#Print first 500 characters
print(res.text[:500])

#Ensure programs halts when download fold
res.raise_for_status()

#Bad Request
badRes = requests.get('https://automatetheboringstuff.com/files/fcjvdjrj.txt')
badRes.raise_for_status()

playFile = open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

#stop the pain
#https://nedbatchelder.com/text/unipain.html