from pathlib import Path


def build_response(parsed_request):
    is_valid, result = parsed_request
    if is_valid:
        return {
            "status": "OK",
            "body": "Welcome to my Space"
        }
    else:
        return {
            "status": "FAILED",
            "body": "Invalid request"
        }


def parse_request(request_text):
    stripped = request_text.strip()
    if not stripped:
        return (False, "Incorrect request format")

    parts = stripped.split()
    
    if len(parts) != 2:
        print(f"{stripped} - Invalid protocol: rejected")
        return (False, "Invalid request format")

    if parts[0] != "WEAVE/1":
        return (False, "Unsupported version")

    if parts[1][0] != "/":
        return (False, "Invalid path")

    return (True, parts[1])


def resolve_page(path):
    pass

