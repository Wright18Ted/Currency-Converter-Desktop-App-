import requests

#function to fetch live currenecy rates from the API for caluction/displaying exchange rates. 
def fetch_live_rates(base_currency):
    
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() 
        
        data = response.json()
        
        if data.get("result") == "success":
            return data["rates"]
        else:
            print(f"API Error: {data.get('error-type')}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Network Pipeline Error: {e}")
        return None

