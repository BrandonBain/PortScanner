import socket
import threading

def scan_port(ip, port, results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            results.append((port, "open"))
        else:
            results.append((port, "closed"))
    except Exception as e:
        results.append((port, f"error: {e}"))
    finally:
        sock.close()

def scan_ports(ip, start_port, end_port):
    threads = []
    results = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Sort the results by port number
    results.sort()

    # Print the results
    for port, status in results:
        print(f"Port {port} is {status} on")

if __name__ == "__main__":
    target_ip = input("IP: ")
    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))

    scan_ports(target_ip, start_port, end_port)