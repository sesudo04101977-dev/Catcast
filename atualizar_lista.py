import re
import requests

def obter_token():
    url_publica = "https://catcast.tv"
    cabecalhos = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://catcast.tv'
    }
    
    try:
        resposta = requests.get(url_publica, headers=cabecalhos, timeout=15)
        if resposta.status_code == 200:
            match = re.search(r'token=([a-f0-9]{32})', resposta.text)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Erro ao buscar token: {e}")
    return None

def gerar_m3u():
    token = obter_token()
    if not token:
        print("Não foi possível capturar um novo token.")
        return
        
    conteudo_m3u = f"""#EXTM3U
#EXTINF:-1 tvg-id="" tvg-name="" tvg-logo="", Canal Catcast
https://catcast.tv{token}&server=v2.catcast.tv
"""
    
    with open("lista.m3u", "w", encoding="utf-8") as f:
        f.write(conteudo_m3u)
    print("Arquivo lista.m3u atualizado com sucesso!")

if __name__ == "__main__":
    gerar_m3u()
