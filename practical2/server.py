from xmlrpc.server import SimpleXMLRPCServer
import os


PORT = 12345 
# ------------------------

def save_file_rpc(filename, file_data):
    
    save_name = "received_" + filename
    with open(save_name, "wb") as handle:
        handle.write(file_data.data)
    print(f"[+] Received file: {filename} -> Saved as: {save_name}")
    return True


print(f"[+] Starting RPC Server on port {PORT}...")
server = SimpleXMLRPCServer(("localhost", PORT))

print("[+] Ready to receive files. Press Ctrl+C to stop.")
server.register_function(save_file_rpc, "upload_file")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\n[-] Server stopped.")