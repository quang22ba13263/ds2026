import xmlrpc.client
import os
import sys


PORT = 12345
# ------------------------

filename = "send_me.txt"


if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write(f"Hello RPC! This file was sent via port {PORT}")
    print(f"[!] Created dummy file '{filename}' for testing.")

print(f"[+] Connecting to RPC Server at localhost:{PORT}...")

try:
    
    proxy = xmlrpc.client.ServerProxy(f"http://localhost:{PORT}/")

    with open(filename, "rb") as handle:
        print(f"[+] Reading file '{filename}'...")
        binary_data = xmlrpc.client.Binary(handle.read())
        
        print("[+] Sending file via RPC...")
        
        success = proxy.upload_file(filename, binary_data)

    if success:
        print("[+] Success! File transferred.")
    else:
        print("[-] Server reported failure.")

except ConnectionRefusedError:
    print(f"[-] Error: Could not connect to port {PORT}. Is the server running?")
except Exception as e:
    print(f"[-] An error occurred: {e}")