def build_response(request_text):
    return "Test Response!"

def parse_request(request_text):
    stripped = request_text.strip()
    if not stripped:
        return (False, "Incorrect request format")

    split = stripped.split()
    
    if len(split) > 2:
        print(f"{stripped} - Invalid protocol: rejected")
        return (False, "Invalid request format")

    if split[0] == "WEAVE/1":
        print(f"{stripped} - Valid protocol: accepted")
        if split[1][0] == '/':
            print(f"{stripped} - address prefix correct")
            return (True, split[1])
        else:
            print(f"{stripped} - Invalid address")
            return (False, "Invalid request")
    else:
        print(f"{stripped} - Invalid protocol: rejected")


parse_request("WEAVE/1 /")              # should be accepted
parse_request("WAEVE/2 /")              # rejected
parse_request("WEAVE/1 / about")        # rejected
