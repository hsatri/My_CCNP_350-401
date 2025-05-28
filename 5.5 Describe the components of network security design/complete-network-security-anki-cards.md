# Complete Network Security Design Anki Cards

## 5.5 Network Security Design Components

Q: What are the main components of network security design as described in section 5.5?
A: 5.5.a Threat defense
   5.5.b Endpoint security
   5.5.c Next-generation firewall
   5.5.d TrustSec and MACsec
   5.5.e Network access control with 802.1X, MAB, and WebAuth

## Network Security Design Basics

Q: What are the key aspects of network security design?
A: 🔹EndPoint Security: Protects devices (mobile, laptops) from malware, ransomware, phishing, threats.
   🔹Access Control: Validates user identities before granting network access.
   🔹Cisco Cyber Threat Defense (CTD): provides tools to detect and mitigate advanced threats.
   🔹Threat Visibility & Control: Helps security analysts monitor and manage network threats effectively.

## Endpoint Security

Q: What devices are considered endpoints in network security?
A: Desktops, laptops, mobile devices, tablets, printers.

Q: What are the endpoint security tools mentioned in the document?
A: - Personal firewalls 
   - Antivirus
   - Antispyware software

Q: What threats do endpoint security tools protect against?
A: Malware, spyware, and malicious traffic.

Q: What Cisco security solutions protect endpoints?
A: - ESA (Email Security Appliance): Blocks Email threats like (spam, malware, phishing).
   - WSA (Web Security Appliance): Monitors web traffic to detect and block malware.
   - AMP (Advanced Malware Protection): Provides advanced threat detection and IP reputation-based blocking.

Q: What additional Cisco security solutions are mentioned for endpoint protection?
A: - Cisco Threat Grid
   - AnyConnect
   - Umbrella

Q: How does firewall protection work for endpoints?
A: - Controls host traffic
   - Defines security policies
   - Integrated into modern OS

Q: What tools are mentioned for data encryption on endpoints?
A: - BitLocker
   - TrueCrypt
   - macOS disk utility

## Firewall Technology

Q: What is a firewall?
A: A security system (hardware, software, or cloud-based) that monitors and filters incoming/outgoing traffic based on security rules.

Q: Where is a firewall typically placed?
A: Between a trusted and an untrusted network to prevent unauthorized access.

Q: What is the main function of a firewall?
A: Traffic Control: Grants or blocks access based on predefined firewall policies.

Q: What types of firewalls are mentioned in the document?
A: - Hardware
   - Software
   - Virtual
   - Cloud-based

Q: What was the evolution of firewall generations?
A: - First Generation: Used packet filtering techniques
   - Second Generation: Introduced application-layer filtering

Q: What environments use firewalls for protection?
A: Both home and corporate networks to protect from cyber threats.

## Stateful Firewall

Q: What is state tracking in a stateful firewall?
A: Maintains connection states in a state table.

Q: How does a stateful firewall handle packets?
A: Forwards packets after storing connection details.

Q: What is replay matching in a stateful firewall?
A: Checks replay packets against the state table.

Q: How does a stateful firewall implement security control?
A: - Accepts matching packets
   - Drops unmatched ones

## Next-Generation Firewall (NGFW)

Q: What features enhance a next-generation firewall (NGFW)?
A: - Application awareness
   - Intrusion prevention
   - Cloud-based threat intelligence

Q: What are the four generations of firewalls?
A: - First Gen: Packet filtering
   - Second Gen: Deep packet inspection
   - Third Gen (Next-Gen): Layer 7 filtering, user/content policies
   - Fourth Gen: Cloud-based security and control

## TrustSec

Q: What is TrustSec?
A: A next-generation access control solution for managing firewall rules and ACLs.

Q: What is SGT in TrustSec and how is it used?
A: SGT (Security Group Tag): Used for ingress tagging and egress filtering to enforce access policies.

Q: How does TrustSec handle authentication and authorization?
A: Cisco ISE assigns SGT tags via 802.1x, MAB, or WebAuth.

Q: How is policy enforcement implemented in TrustSec?
A: Access control (Allow/Drop) is applied at the egress point based on SGT tags.

## MACsec (Media Access Control Security)

Q: What is MACsec according to the document?
A: A Layer 2 encryption method (IEEE 802.1AE) that encrypts traffic hop-by-hop between MACsec peers.

Q: What is the encryption scope of MACsec?
A: Traffic is encrypted only on the wire but decrypted inside switches for packet enforcement and QoS.

Q: How does MACsec perform encryption/decryption compared to IPsec?
A: Uses onboard ASICs for hardware acceleration instead of offloading to a crypto engine like IPsec.

Q: What does MACsec add to frame format?
A: Adds a 16-byte MACsec Security Tag and a 16-byte Integrity Check Value (ICV).

Q: What is required for MACsec to work in a communication path?
A: All devices in the communication path must support MACsec for encryption to work.

Q: What security mechanisms does MACsec use?
A: Uses GMAC for authentication and AES-GCM for authenticated encryption.

## 802.1X Authentication

Q: What is 802.1X (Dot1x)?
A: A standard developed by the IEEE 802.1 working group. It is a port-based authentication method used for network access control at the Data Link Layer (Layer 2) of the OSI model.

Q: What protocol is used to encapsulate authentication messages in 802.1X?
A: EAPOL (Extensible Authentication Protocol over LANs)

Q: What protocol does 802.1X rely on for communication between devices?
A: EAP (Extensible Authentication Protocol)

Q: What type of authentication does 802.1X provide?
A: Port-level authentication that ensures only authenticated devices can access the network.

Q: What type of traffic is allowed before 802.1X authentication is successful?
A: Only EAPoL traffic (used for authentication); all other traffic is blocked until successful credential verification.

Q: What networks can 802.1X secure?
A: Both wired and wireless networks at the Data Link Layer (Layer 2).

## 802.1X Components - Supplicant

Q: What is a Supplicant in 802.1X?
A: The user or device requesting access to the network (wired or wireless).

Q: What types of devices can be a Supplicant?
A: A client, host, or workstation connected through a network access switch. Examples include PCs, printers, fax machines, or IP phones.

Q: What is required for a device to function as a Supplicant?
A: The device must run 802.1X client software.

Q: What operating systems include a native supplicant?
A: All Windows operating systems come with a native supplicant for wired network connections.

## 802.1X Components - Authentication Server

Q: What is the Authentication Server's role in 802.1X?
A: It processes authentication requests, authenticates the Supplicant (client or device), validates its identity, and informs the Authenticator whether to allow or deny network access.

Q: What protocol does the Authentication Server typically use?
A: RADIUS

Q: What is an example of an Authentication Server?
A: RADIUS servers like ACS (Access Control Server)

## Web Authentication

Q: What is Web Authentication?
A: Authentication and authorization via an HTTP/HTTPS portal that automatically redirects users to the portal.

Q: When is Web Authentication typically used?
A: Primarily for guests, visitors, and as a fallback for 802.1X. Works with both wired and wireless access.

Q: How does the authentication flow work in Web Authentication?
A: Users are redirected to Cisco ISE for authentication, after which Cisco ISE sends a CoA (Change of Authorization) request to the Network Access Device.

Q: What type of users is Web Authentication ideal for?
A: Interactive users with a web browser who manually enter credentials.

Q: What's required for Web Authentication to function?
A: Proper configuration, such as redirection ACL and ISE authentication/authorization rules.

Q: When is a client typically redirected to the web portal?
A: When clients fail authentication via Dot1x or MAB.

Q: What determines guest login access in Web Authentication?
A: The authorization profile on the Authentication Server.

Q: What authentication methods can work alongside CWA (Centralized Web Authentication)?
A: Dot1x and MAB

Q: What must a switch support for CWA to function?
A: HTTP/HTTPS services and have a redirect ACL.

Q: What is CWA often used for?
A: Centralized guest authentication and authorization.

Q: At what OSI layer does Web Authentication operate?
A: Layer 3 (L3), as it requires an IP address.

## MAC Authentication Bypass (MAB)

Q: What is MAB (MAC Authentication Bypass)?
A: Network access control at Layer 2 using a device's MAC address instead of 802.1X authentication.

Q: When is MAB typically used?
A: For devices like printers and IP phones that don't support 802.1X.

Q: What security weakness does MAB have?
A: It is less secure than other methods because it can be bypassed by MAC address spoofing.

Q: How does MAB work?
A: When enabled, the switch learns the MAC address from the first frame, then checks it with the authentication server (e.g., ISE).

Q: What are the two ways authentication can be based on in MAB?
A: Calling Station ID or Username & Password.

Q: What is MAB typically used for and what can it integrate?
A: Typically used for single endpoint devices and can integrate dynamic settings like ACLs or VLANs.

Q: Can MAB be used with other authentication methods?
A: Yes, it can be used alone or alongside other authentication methods like 802.1X.
