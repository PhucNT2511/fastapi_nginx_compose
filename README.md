# 🚀 FastAPI + Nginx + Docker Compose

Triển khai 2 ứng dụng FastAPI qua Nginx sử dụng Docker Compose.

## 📦 Cấu trúc thư mục

```
fastapi_nginx_compose/
├── app1/
│   ├── main.py
│   └── Dockerfile
├── app2/
│   ├── main.py
│   └── Dockerfile
├── nginx/
│   ├── default.conf
│   └── nginx.conf
├── docker-compose.yml
└── test.py  # Script kiểm tra request
```

## ▶️ Cách chạy

```bash
# 1. Clone project (nếu cần)
git clone <repo-url>
cd fastapi_nginx_compose

# 2. Build và chạy toàn bộ
docker-compose up --build
```

## 🌐 Truy cập ứng dụng
- App1: http://localhost:8080/app1/
- App2: http://localhost:8080/app2/

## 🧪 Test bằng script Python
```bash
python test.py
#Script sẽ gửi nhiều request đến 2 app để kiểm tra giới hạn truy cập (limit_req).
```

## 🧼 Dừng và xóa container
```bash
docker-compose down
```
