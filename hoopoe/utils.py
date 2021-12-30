
def handle_response(response):
    if not response.status_code: 
        raise Exception("Response is not valid")
    
    if response.status_code in range(200, 300):
        return response.json()
    elif response.status_code < 500:
        raise Exception(response.json())
    else:
        raise Exception("Unknown error")