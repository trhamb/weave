from pathlib import Path


def build_response(parsed_request):
    is_valid, result = parsed_request
    if is_valid:
        return {
            "status": "OK",
            "body": result
        }
    else:
        return {
            "status": "FAILED",
            "body": result
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

    if not parts[1].startswith("/"):
        return (False, "Invalid path")

    return (True, parts[1])


def resolve_page(path):
    pass

