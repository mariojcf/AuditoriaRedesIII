import nmap

def escanear_red(rango_red):
    scanner = nmap.PortScanner()
    print(f"Escaneando dispositivos en: {rango_red}...")
    scanner.scan(hosts=rango_red, arguments='-sP')
    hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
    for host, status in hosts_list:
        print(f"Host: {host} | Estado: {status}")

def escanear_puertos(ip):
    scanner = nmap.PortScanner()
    print(f"Escaneando puertos abiertos en {ip}...")
    scanner.scan(ip, '1-1024')
    for proto in scanner[ip].all_protocols():
        ports = scanner[ip][proto].keys()
        for port in ports:
            state = scanner[ip][proto][port]['state']
            print(f"Puerto: {port} | Estado: {state}")

if __name__ == "__main__":
    rango = input("Introduce el rango de red (ej: 192.168.1.0/24): ")
    escanear_red(rango)
    ip = input("Introduce una IP para escanear sus puertos: ")
    escanear_puertos(ip)
