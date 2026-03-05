import httpx

def vuln_check(url):
    result = {
        "findings": [],
        "total_headers": 0,
        "error": None
    }

    try:
        with httpx.Client(timeout=10) as client:
            response = client.get(url)

        headers = response.headers
        result["total_headers"] = len(headers)

        server = headers.get("Server")
        if server:
            result["findings"].append(f"Server header exposed: {server}")

    except Exception as e:
        result["error"] = str(e)

    return result
