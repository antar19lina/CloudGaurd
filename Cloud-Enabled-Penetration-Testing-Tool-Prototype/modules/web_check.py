import httpx

def check_headers(url):
    result = {
        "present": [],
        "missing": [],
        "total_headers": 0,
        "error": None
    }

    security_headers = [
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Strict-Transport-Security"
    ]

    try:
        with httpx.Client(
            follow_redirects=True,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        ) as client:
            response = client.get(url)

        headers = response.headers
        result["total_headers"] = len(headers)

        for header in security_headers:
            if header in headers:
                result["present"].append(header)
            else:
                result["missing"].append(header)

    except Exception as e:
        result["error"] = str(e)

    return result


    return result
