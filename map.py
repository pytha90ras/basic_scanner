def n_mapper():
    import socket
    try:
        from udpayloads import udp_payloads
    except ModuleNotFoundError:
        print("Can't find dependency: udpayloads.py")
        return
    def scan_tcp(ip,ports):
        confirmation=input(f'Starting TCP scan on {ip}, press enter to continue ')
        if len(confirmation)!=0:
            return '\n\n'+'Cancelled'
        ports_res={}
        for i in ports:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                s.connect((ip,i))
                ports_res[i]={'open'}
            except (socket.timeout, socket.error):
                pass
            s.close()
        return ports_res
    def scan_udp(ip,ports):
        confirmation=input(f'Starting UDP scan on {ip}, press enter to continue ')
        if len(confirmation)!=0:
            return '\n\n'+'Cancelled'
        ports_res={}
        for i in ports:
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.settimeout(2)
            try:
                if i in udp_payloads:
                    s.sendto(udp_payloads[i],(ip,i))
                    s.recvfrom(1024)
                    ports_res[i]='open'
                else:
                    s.sendto(b'',(ip,i))
                    s.recvfrom(1024)
                    ports_res[i]='open'
            except socket.timeout:
                ports_res[i]='open or filtered'
            except socket.error:
                pass
            s.close()
        return ports_res
    ip_addr=input('Enter IP address to scan: ')
    print('Please enter the ports you would like to scan\nIn the format x-y for a range of ports or x,y,z... for specific ports')
    p_type=input('What protocol would you like to scan for?\n    1. UDP\n    2. TCP\n    3. BOTH\nInput here: ')
    if p_type!='1' and p_type !='2' and p_type !='3':
        print("Invalid choice")
        return
    p_in=input('Enter port list or range: ')
    if '-' in p_in:
        start,end=p_in.split('-')[0],p_in.split('-')[1]
        p_list=[i for i in range(int(start),int(end)+1)]
    else:
        p_list=[int(i) for i in p_in.split(',')]
    if p_type=='1':
        print(f'\n\n UDP scan result on {ip_addr}: ',scan_udp(ip_addr,p_list))
    elif p_type=='2':
        print(f'\n\n TCP scan result on {ip_addr}: ',scan_tcp(ip_addr,p_list))
    elif p_type=='3':
        print(f'\n\n UDP scan result on {ip_addr}: ',scan_udp(ip_addr,p_list))
        print(f'\n\n TCP scan result on {ip_addr}: ',scan_tcp(ip_addr,p_list))
n_mapper()
