import httpx

URL = 'https://covid19-brazil-api.vercel.app/api/report/v1/'

def getALL():
    return api(URL)


def getState(uf: str):
    url = f"{URL}brazil/uf/{uf}"
    state = api(url)
    return state

def getDate(time: str):
    url = f"{URL}brazil/{time}"
    date = api(url)
    return date

def getStatus():
    return api('https://covid19-brazil-api.vercel.app/api/status/v1/')
    
def api(url):
    request = httpx.get(url)
    response = request.json()
    return response