# Network Security Design Anki Cards

## Basic Components

Q: What are the main components of network security design?
A: 1. Threat defense
   2. Endpoint security
   3. Next-generation firewall
   4. TrustSec and MACsec
   5. Network access control (802.1X, MAB, WebAuth)

Q: What are the key aspects of network security design?
A: - Endpoint Security: Protects devices from threats
   - Access Control: Validates user identities
   - Cisco Cyber Threat Defense (CTD): Tools for threat detection and mitigation
   - Threat Visibility & Control: Monitoring and management of network threats

## Endpoint Security

Q: What devices are considered endpoints in network security?
A: Desktops, laptops, mobile devices, tablets, and printers.

Q: What are the main endpoint security tools?
A: - Personal firewalls
   - Antivirus software
   - Antispyware software

Q: What Cisco security solutions protect endpoints?
A: - ESA (Email Security Appliance): Blocks email threats
   - WSA (Web Security Appliance): Monitors web traffic
   - AMP (Advanced Malware Protection): Advanced threat detection
   - Additional solutions: Cisco Threat Grid, AnyConnect, Umbrella

Q: How does firewall protection work for endpoints?
A: - Controls host traffic
   - Defines security policies
   - Is integrated into modern operating systems

Q: How is data encryption used for endpoint security?
A: Protects endpoint data using tools like BitLocker, TrueCrypt, and macOS disk utility.

## Firewall Technology

Q: What is a firewall?
A: A security system (hardware, software, or cloud-based) that monitors and filters incoming/outgoing traffic based on security rules.

Q: Where is a firewall typically placed?
A: Between a trusted and untrusted network to prevent unauthorized access.

Q: What are the different types of firewalls?
A: Hardware, software, virtual, and cloud-based.

Q: What was the evolution of firewall generations?
A: - First Generation: Used packet filtering techniques
   - Second Generation: Introduced application-layer filtering
   - Third Generation (Next-Gen): Layer 7 filtering, user/content policies
   - Fourth Generation: Cloud-based security and control

## Stateful Firewall

Q: How does a stateful firewall work?
A: - Maintains connection states in a state table
   - Forwards packets after storing connection details
   - Checks replay packets against the state table
   - Accepts matching packets and drops unmatched ones

## Next-Generation Firewall (NGFW)

Q: What features enhance a next-generation firewall beyond traditional firewalls?
A: - Application awareness
   - Intrusion prevention
   - Cloud-based threat intelligence
   - Layer 7 filtering
   - User/content policies

## TrustSec

Q: What is TrustSec?
A: A next-generation access control solution for managing firewall rules and ACLs.

Q: What is SGT in TrustSec and how is it used?
A: Security Group Tag (SGT) is used for ingress tagging and egress filtering to enforce access policies.

Q: How does TrustSec handle authentication and authorization?
A: Cisco ISE assigns SGT tags via 802.1x, MAB, or WebAuth.

Q: How is policy enforcement implemented in TrustSec?
A: Access control (Allow/Drop) is applied at the egress point based on SGT tags.

## MACsec (Media Access Control Security)

Q: What is MACsec?
A: A Layer 2 encryption method (IEEE 802.1AE) that encrypts traffic hop-by-hop between MACsec peers.

Q: What is the encryption scope of MACsec?
A: Traffic is encrypted only on the wire but decrypted inside switches for packet enforcement and QoS.

Q: How does MACsec perform encryption/decryption?
A: Uses onboard ASICs for hardware acceleration instead of offloading to a crypto engine like IPsec.

Q: What does MACsec add to frame format?
A: Adds a 16-byte MACsec Security Tag and a 16-byte Integrity Check Value (ICV).

Q: What security mechanisms does MACsec use?
A: GMAC for authentication and AES-GCM for authenticated encryption.

## 802.1X Authentication

Q: What is 802.1X (Dot1x)?
A: A port-based authentication method used for network access control at the Data Link Layer (Layer 2).

Q: What protocol is used to encapsulate authentication messages in 802.1X?
A: EAPOL (Extensible Authentication Protocol over LANs)

Q: At what OSI layer does 802.1X operate?
A: Data Link Layer (Layer 2)

Q: What type of traffic is allowed before 802.1X authentication is successful?
A: Only EAPoL traffic (used for authentication); all other traffic is blocked until successful authentication.

## 802.1X Components

Q: What are the three main components in 802.1X authentication?
A: 1. Supplicant
   2. Authenticator
   3. Authentication Server

Q: What is a Supplicant in 802.1X?
A: The user or device requesting access to the network (could be a PC, printer, fax machine, or IP phone).

Q: What is required for a device to function as a Supplicant?
A: The device must run 802.1X client software.

Q: What is the Authentication Server's role in 802.1X?
A: It processes authentication requests, validates the Supplicant's identity, and informs the Authenticator whether to allow or deny network access.

Q: What is an example of an Authentication Server?
A: RADIUS servers like Cisco ACS.

## Web Authentication

Q: What is Web Authentication?
A: Authentication and authorization via an HTTP/HTTPS portal that automatically redirects users.

Q: When is Web Authentication typically used?
A: For guests, visitors, and as a fallback for 802.1X.

Q: What's required for Web Authentication to function?
A: - The switch must support HTTP/HTTPS services
   - A redirect ACL must be configured
   - Proper ISE authentication/authorization rules

Q: At what OSI layer does Web Authentication operate?
A: Layer 3 (L3), as it requires an IP address.

## MAC Authentication Bypass (MAB)

Q: What is MAB?
A: Network access control at Layer 2 using a device's MAC address instead of 802.1X authentication.

Q: When is MAB typically used?
A: For devices like printers and IP phones that don't support 802.1X.

Q: How does MAB work?
A: The switch learns the MAC address from the first frame, then checks it with the authentication server (e.g., ISE).

Q: What is a security weakness of MAB?
A: It can be bypassed by MAC address spoofing, making it less secure than other methods.
