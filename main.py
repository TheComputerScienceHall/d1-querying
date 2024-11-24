import requests
import env
from env import logic

def l3(val, database_id, api_token, type):
    account_id = env.account_id
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/d1/database/{database_id}/query"

    payload = {
    "sql": f"SELECT * FROM main WHERE id = {val}",
    "bindings": [val]
    }

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    if type == logic.q_f2:
        mem_d = response.json()
        mem_l1 = mem_d["result"][0]["results"][0][logic.l1]
        mem_l2 = mem_d["result"][0]["results"][0][logic.l2]
        return [mem_l1, mem_l2]
    elif type == logic.q_f1:
        mem_d = response.json()
        mem_l3 = mem_d["result"][0]["results"][0][logic.l1]
        return mem_l3
    else:
        print("Isnt Valid")



mem_u_l1 = l3(1, env.db_key, env.api_key, logic.q_l1)
mem_u_l2 = l3(1, env.db_data, env.api_key, logic.q_l2)
mem_u_l3 = mem_u_l2[0]
mem_u_l4 = mem_u_l2[1]
print(mem_u_l1, mem_u_l3, mem_u_l4)
