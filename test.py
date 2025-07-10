import requests
import time

def access_app(endpoint, n_requests=6, delay=0.1):
    for i in range(n_requests):
        try:
            response = requests.get(endpoint)
            status = response.status_code

            try:
                content = response.json()
            except Exception:
                content = response.text.strip()

            print(f"[{endpoint}] → {status} | {content}")

        except Exception as e:
            print(f"[{endpoint}] → ERROR: {e}")

        time.sleep(delay)

if __name__ == "__main__":
    base_url = "http://localhost:8080"

    print("📥 Gửi nhiều request đến app1:")
    access_app(f"{base_url}/app1/")

    print("\n📥 Gửi nhiều request đến app2:")
    access_app(f"{base_url}/app2/")

'''
Gửi 6 request đến app1 đúng lúc Nginx còn đủ burst, còn khi đến app2, burst đã hết → bị chặn 429.
📊 Nginx không chia burst đều cho từng app — mỗi route là 1 location block, nhưng dùng chung zone (req_limit_per_ip).
'''