import ctypes
import pyshark
import signal
import sys

# Initialize nDPI library
ndpi = ctypes.CDLL('/home/ibtissam/Desktop/Internship/nDPI-dev/src/lib/libndpi.so')

# Custom Scoring Function (extended)
def score_protocol(protocol):
    # Scoring based on importance, frequency of use, and vulnerability
    scoring = {
        'HTTP': 10,  # High score for frequent use but insecure
        'HTTPS': 9,  # High score for frequent use and secure
        'FTP': 8,    # High score due to frequent use, but lower than HTTPS
        'TLS': 7,    # Secure, often used for encrypted connections
        'TCP': 6,    # Base transport protocol, less directly risky
        'ARP': 3,    # Lower score, fundamental network protocol but with spoofing risks
        'SSDP': 4,   # Lower score but can be involved in DDoS attacks
        'MDNS': 4,   # Lower score, used for network service discovery
        # Add more protocols and their associated scores here...
    }
    return scoring.get(protocol, 5)  # Default score is 5 if not found

# Custom Risk Classification Function (extended)
def classify_risk(protocol):
    # Classification based on potential threat level and security posture
    risk_categories = {
        'HTTP': 'Medium',  # Medium risk due to lack of encryption
        'HTTPS': 'Low',    # Low risk due to encryption
        'FTP': 'High',     # High risk due to lack of encryption
        'TLS': 'Medium',   # Medium risk, generally secure but with potential vulnerabilities
        'TCP': 'Low',      # Low risk, essential for communication but not risky on its own
        'ARP': 'Low',      # Low risk, but can be exploited via spoofing
        'SSDP': 'Medium',  # Medium risk, can be exploited in amplification attacks
        'MDNS': 'Medium',  # Medium risk, can expose internal services if misconfigured
        # Add more protocols and their associated risks here...
    }
    return risk_categories.get(protocol, 'Unknown')  # Default is 'Unknown'

# Custom Scoring for Non-Secure Ports
def score_ports(src_port, dst_port):
    non_secure_ports = {21, 23, 80, 110, 143}  # Example of non-secure ports (FTP, Telnet, HTTP, POP3, IMAP)
    score = 0
    
    if int(src_port) in non_secure_ports:
        score += 10  # Assign a high score for non-secure ports
    if int(dst_port) in non_secure_ports:
        score += 10  # Assign a high score for non-secure ports
    
    return score

def process_packet(packet):
    try:
        # Extract protocol and port information from the packet
        protocol = packet.highest_layer
        src_port = packet[packet.transport_layer].srcport
        dst_port = packet[packet.transport_layer].dstport
        
        # Scoring and risk classification
        protocol_score = score_protocol(protocol)
        port_score = score_ports(src_port, dst_port)
        total_score = protocol_score + port_score
        risk = classify_risk(protocol)
        
        # Display the information
        print(f"Detected Protocol: {protocol}")
        print(f"Source Port: {src_port} -> Destination Port: {dst_port}")
        print(f"Protocol Score: {protocol_score}")
        print(f"Port Score: {port_score}")
        print(f"Total Score: {total_score}")
        print(f"Risk: {risk}")
        print("----------------------------------------")
    except Exception as e:
        print(f"Error processing packet: {e}")

def signal_handler(sig, frame):
    print("\nStopping the capture...")
    sys.exit(0)

def main():
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)

    # Start capturing live traffic (replace 'wlp1s0' with your network interface)
    capture = pyshark.LiveCapture(interface='wlp1s0')

    print("Starting real-time traffic analysis...")
    
    for packet in capture.sniff_continuously():
        process_packet(packet)

if __name__ == "__main__":
    main()







