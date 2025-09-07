import socket
import pytest
from portscan import scan_ports  # adjust if your file is named differently

def test_scan_known_open_port(monkeypatch):
    # Mock socket to simulate port 80 is open
    def fake_connect_ex(addr):
        host, port = addr
        return 0 if port == 80 else 1  # 0 means success
    
    monkeypatch.setattr(socket.socket, "connect_ex", lambda self, addr: fake_connect_ex(addr))
    
    open_ports = scan_ports("127.0.0.1", 79, 81)
    assert 80 in open_ports
    assert 79 not in open_ports
    assert 81 not in open_ports

def test_scan_no_open_ports(monkeypatch):
    # Mock socket to simulate all ports closed
    monkeypatch.setattr(socket.socket, "connect_ex", lambda self, addr: 1)
    
    open_ports = scan_ports("127.0.0.1", 20, 22)
    assert open_ports == []
