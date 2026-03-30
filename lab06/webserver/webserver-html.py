import socket

import socket

def handle_request(client_socket, request_data):
    # Kiểm tra đường dẫn trong request_data
    if "GET /admin" in request_data:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        # Mở và đọc nội dung file admin.html
        with open("admin.html", "r", encoding="utf-8") as file:
            response += file.read()
    else:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        # Mở và đọc nội dung file index.html cho các trường hợp còn lại
        with open("index.html", "r", encoding="utf-8") as file:
            response += file.read()
    
    # Gửi toàn bộ phản hồi (Header + Body) về client
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def main():
    # Khởi tạo socket (Sửa lỗi SOCK_STREAM từ ảnh trước)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(5)
    
    print("Server listening on port 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Nhận dữ liệu từ trình duyệt
        request_data = client_socket.recv(1024).decode('utf-8')
        
        # Xử lý và gửi file tương ứng
        handle_request(client_socket, request_data)

if __name__ == '__main__':
    main()