import urllib.request

UA = "Mozilla/5.0 (kurzy-srovnani; +https://kurzy.thugsclub.eu)"


def get(url: str, timeout: float = 15) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")
