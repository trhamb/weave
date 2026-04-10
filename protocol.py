def build_response(parsed_request):
    is_valid, result = parsed_request
    if is_valid:
        return(f"Valid request, accessing {result}")
    else:
        return("Invalid request")

def parse_request(request_text):
    stripped = request_text.strip()
    if not stripped:
        return (False, "Incorrect request format")

    parts = stripped.split()
    
    if len(parts) != 2:
        print(f"{stripped} - Invalid protocol: rejected")
        return (False, "Invalid request format")

    if parts[0] == "WEAVE/1":
        print(f"{stripped} - Valid protocol: accepted")
        if parts[1][0] == '/':
            print(f"{stripped} - address prefix correct")
            return (True, parts[1])
        else:
            print(f"{stripped} - Invalid address")
            return (False, "Invalid request")
    else:
        print(f"{stripped} - Invalid protocol: rejected")



