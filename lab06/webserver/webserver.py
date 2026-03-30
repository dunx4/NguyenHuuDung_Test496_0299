import socket
#
def handle_request(client_socket, request_data):
    # Kiểm tra nếu request trỏ đến trang /admin
    if "GET /admin" in request_data:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nWelcome to the admin page!"
    else:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, this is a simple web server!"
    
    # Gửi phản hồi về cho client và đóng kết nối
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def main():
    # Tạo socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Liên kết socket với địa chỉ và cổng
    server_socket.bind(('127.0.0.1', 8080))
    
    # Lắng nghe các kết nối đến (tối đa 5 kết nối trong hàng đợi)
    server_socket.listen(5)
    
    print("Server listening on port 8080...")

    while True:
        # Chấp nhận kết nối mới
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Nhận dữ liệu request (tối đa 1024 bytes)
        request_data = client_socket.recv(1024).decode('utf-8')
        
        # Xử lý request
        handle_request(client_socket, request_data)

if __name__ == '__main__':
    main()