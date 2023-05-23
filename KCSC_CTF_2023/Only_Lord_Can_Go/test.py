import socket

# Địa chỉ IP và cổng của máy chủ
server_ip = '188.166.220.129'
server_port = 60123

# Tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Kết nối đến máy chủ
    client_socket.connect((server_ip, server_port))
    response = client_socket.recv(1024)
    print(response)

    # Nhập dữ liệu từ người dùng
    data1 = [1249143710, 1875630609, 443821967, 509749366, 1715122798, 1212830748, 925224918, 753558452, 1226638920, 611882139, 1158993845,
            1636921130, 1041373683, 1312190863, 663212578, 1063693719, 1055650996, 195965914, 1141443519, 2139533974, 1092297343, 490498390, 1663309706]
    data = "1249143710"
    # Gửi dữ liệu đến máy chủ
 
    client_socket.sendall(data.encode())

        # Nhận phản hồi từ máy chủ
    response = client_socket.recv(1024)
    print(response.decode())
    

except ConnectionRefusedError:
    print("Không thể kết nối đến máy chủ.")

finally:
    # Đóng kết nối
    client_socket.close()
