from pathlib import Path


def build_response(parsed_request):
    status, result = parsed_request
    if status == "WOVEN":
        return {
                "status": status,
                "body": result
                }

    if status == "MISWOVEN":
        return {
                "status": status,
                "body": result
                }

    if status == "TANGLED":
        return {
                "status": status,
                "body": result
                }


def parse_request(request_text):
    stripped = request_text.strip()
    if not stripped:
        return ("MISWOVEN", "Incorrect request format")

    parts = stripped.split()
    
    if len(parts) != 2:
        print(f"{stripped} - Invalid protocol: rejected")
        return ("MISWOVEN", "Invalid request format")

    if parts[0] != "WEAVE/1":
        return ("TANGLED", "Unsupported version")

    if not parts[1].startswith("/"):
        return ("MISWOVEN", "Invalid path")

    return ("WOVEN", parts[1])


def resolve_page(path):
    stripped_path = path.strip("/")
    filename = stripped_path + ".txt"
    content_root = Path('content')
    full_path = content_root / filename
    
    if full_path.is_file():
        page_contents = full_path.read_text()
        return (True, page_contents)
    else:
        return (False, "Page not found")


