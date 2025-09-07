import socket
def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Timeout for the connection attempt
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports
if __name__ == "__main__":
    target_host = input("Enter the target host (IP or domain): ")
    start = int(input("Enter the start port number: "))
    end = int(input("Enter the end port number: "))
    print(f"Scanning ports {start} to {end} on {target_host}...")
    open_ports = scan_ports(target_host, start, end)
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found in the specified range.")