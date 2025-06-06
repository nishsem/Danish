# Lab 1: Cryptographic Attacks – Brute Force & Traffic Analysis

**Time Allocated:** 3 Hours  
**Total Marks:** 15  
**Protocols:** FTP, TELNET, SSH, HTTP  
**Tools Used:** Hydra, Medusa, Burp Suite, Wireshark

---

## A. Objective

To explore vulnerabilities in common network protocols (FTP, TELNET, SSH, HTTP) by:

- Performing brute force attacks to recover passwords.
- Sniffing traffic using recovered credentials.
- Analyzing security of plaintext vs encrypted protocols.
- Proposing effective mitigation strategies.

---

## B. Lab Tasks

---

### 1. Username Enumeration

**Goal:** Identify valid usernames to perform brute force attacks.

**Tools:** `nmap` & `enum4linux`

**Commands:**
```bash
nmap -sV -p 21,23,22,80 192.168.43.137
```

![alt text](screenshots/nmap.png)

```bash
enum4linux -a 192.168.43.137
```
**Username Found:**

![alt text](screenshots/enum4linux.png)

**Result:**  
The output from `enum4linux` revealed the following username:

- `msfadmin`

This username is commonly found on Metasploitable2 and was confirmed through SMB enumeration using `enum4linux`.

---

## 2. Brute Force Attacks

---

### 2.1 FTP, TELNET, SSH

- **FTP Brute Force**

**Tool Used:** `Hydra`
**Username:** `msfadmin`
**Password List:** `password.txt`

**Commands:**

```bash
hydra -l msfadmin -P /usr/share/wordlists/password.txt ftp://192.168.43.137
```
 **Valid Credentials Found:**
 
![alt text](screenshots/ftp.png)

- **TELNET Brute Force**

**Tool Used:** `Hydra`  
**Username:** `msfadmin`  
**Password List:** `password.txt`

**Commands:**

```bash
hydra -l msfadmin -P /usr/share/wordlists/password.txt telnet://192.168.43.137
```
 **Valid Credentials Found:**
 ![alt text](screenshots/telnet.png)

- **SSH Brute Force**

**Tool Used:** `medusa`  
**Username:** `msfadmin`  
**Password List:** `password.txt`

**Commands:**

```bash
medusa -h 192.168.43.137 -u msfadmin -P /usr/share/wordlists/password.txt -M ssh
```
 **Valid Credentials Found:**
 
![alt text](screenshots/ssh.png)

## 2.2 HTTP Brute Force

**Tool Used:** `Burp Suite → Intruder`  
**Target URL:** `http://192.168.43.137/dvwa/vulnerabilities/brute/`  

---

### Steps:

1. **Access DVWA:**
   - Go to `http://192.168.43.137/`
   - Click on **DVWA**

![alt text](screenshots/web.png)

   - Login using the default credentials:
     - **Username:** `admin`
     - **Password:** `password`
    
![alt text](screenshots/login.png)

   - Navigate to **DVWA Security** → Set **Security Level** to **Low**

![alt text](screenshots/security.png)

2. **Navigate to Brute Force Page:**
   - Go to **Brute Force**

![alt text](screenshots/bruteforce.png)

   - This is a page with a form to enter **username** and **password** to brute-force a login system.

3. **Intercept with Burp Suite:**
   - Set your browser to use Burp's proxy.

![alt text](screenshots/proxy.png)

   - open burpsuite and turn on intercept option

![alt text](screenshots/turnon.png)

   - Fill in sample credentials (e.g., `admin:1234`) and submit the form.
   - Burp will intercept the POST request.

![alt text](screenshots/dummy.png)

4. **Send to Intruder:**
   - Right-click the intercepted request → **Send to Intruder**

![alt text](screenshots/sendtointruder.png)

   - Set the attack type to **Cluster Bomb**

![alt text](screenshots/clusterbomb.png)

5. **Set Payload Positions:**
   - In the request:

![alt text](screenshots/position.png)

```bash
GET /dvwa/vulnerabilities/brute/?username=admin&password=123&Login=Login HTTP/1.1
```
     
   - Highlight the value of `username` and `password` to mark them as payload positions.


5. **Load Password Wordlist:**
   - Load username and password list in **Payload Options**

![alt text](screenshots/userpayload.png)


![alt text](screenshots/passpayload.png)

6. **Launch Attack:**
   - Click **Start Attack**
   - Look through the results for a request with a noticeably **larger content length**.
   - This indicates a different (likely successful) response compared to the others.

![alt text](screenshots/attack.png)

---

### Verifying the Successful Login:

- **Steps to Verify:**
  1. Right-click the highlighted response.
  2. Select **"Show response in browser"**.
  3. Copy the temporary URL provided by Burp.
  4. Paste the URL into your browser.

![alt text](screenshots/response.png)

![alt text](screenshots/copyresponse.png)

- **Expected Output:**
  You should see the message:  
  > **Welcome to the password protected area admin**

![alt text](screenshots/welcome.png)

---
## 3. Sniffing and Traffic Analysis

**Goal:** Use Wireshark to analyze how credentials are transmitted over different protocols, comparing plaintext and encrypted traffic.

**Tool Used:** Wireshark  
**Target IP:** `192.168.43.137`

---

### 3.1 Capturing FTP Credentials

1. Open **Wireshark** on your attacker machine.
2. Start capturing on the interface connected to the target network.

![image](https://github.com/user-attachments/assets/05d4965a-dfa6-4433-bae6-53354f200bfd)

3. On the attacker's terminal, connect to the FTP service and enter a command like `ls`:
```bash
ftp 192.168.43.137
```
- Username: `msfadmin`

- Password: `msfadmin`

![image](https://github.com/user-attachments/assets/303a950a-ea44-413c-83a7-94404d3e23c2)

4. Apply filter on Wireshark:
```bash
ftp || tcp.port == 21
```

![image](https://github.com/user-attachments/assets/9aef846e-049f-4951-ac76-41f63c88238e)

5. In Wireshark:

- Locate a packet with USER msfadmin in the Info column.
- Right-click it → Follow → TCP Stream.

![image](https://github.com/user-attachments/assets/1a567d3a-0df6-4772-8d88-fafc66f7c4da)

6. The TCP stream will show the full session including credentials:

![image](https://github.com/user-attachments/assets/398d62c8-c7ce-4e7c-9be3-fee95262bd6c)

### 3.2 Capturing TELNET Credentials

1. On the attacker's terminal, connect to the TELNET service adn enter a command:

```bash
telnet 192.168.43.137
```
- Username: `msfadmin`

- Password: `msfadmin`

![image](https://github.com/user-attachments/assets/ee1ddec3-43ac-4586-b5e0-e203927bb35e)

![image](https://github.com/user-attachments/assets/f09e689c-a26d-41a7-a4d1-2ca258d93981)

2. While typing the credentials, each keystroke is transmitted and captured in plaintext.

3. In Wireshark, apply the filter:
```bash
telnet || tcp.port == 23
```

![image](https://github.com/user-attachments/assets/4725d2e9-1aff-4765-addd-7d79221f817e)

- Look through the packet list for TELNET traffic.

- Right-click → Follow → TCP Stream

![image](https://github.com/user-attachments/assets/de8e502e-9986-47eb-9935-597530f40635)

![image](https://github.com/user-attachments/assets/dae81cb3-3fed-455c-84bd-a114f212e7fe)

### 3.3 SSH Traffic

1.  **Start an SSH session** from your terminal:

    `ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedKeyTypes=+ssh-rsa msfadmin@192.168.43.137`

    -   **Username**: `msfadmin`

    -   **Password**: `msfadmin`

    > 🛑 If you see this error:\
    > `Unable to negotiate with 192.168.43.137 port 22: no matching host key type found. Their offer: ssh-rsa,ssh-dss`\
    > Use the command above to force use of `ssh-rsa` which is supported by Metasploitable2.

![image](https://github.com/user-attachments/assets/f1ce378f-eaa1-4ae1-8f19-6d59ecbfce6d)

2.  **Open Wireshark** on your attacker machine.

3.  **Apply the filter** to display only SSH traffic:

```
ssh || tcp.port == 22
```

![image](https://github.com/user-attachments/assets/c03738f3-09db-47ee-aa80-3f0a02aa85dd)

4.  **In Wireshark**:

    -   Observe the captured SSH packets.

    -   Note that the contents are **fully encrypted**.

    -   No credentials or commands can be read in the packet data.

5.  **Optional**: Right-click on any SSH packet → `Follow` → `TCP Stream`.

    -   The stream will display **garbled** or **binary** data, confirming encryption.

![image](https://github.com/user-attachments/assets/29cabe20-b802-4330-9ad2-4ac6c7438b86)

## C. Analyze Problems Encounter

#### Issues Faced During Brute Force Attacks

- **Enumeration**: On Metasploitable 2, there were too many usernames, so it was important to carefully check valid usernames.
- **BurpSuite Bruteforce**: Had to be very careful with payload positions in Burp Intruder. A mistake in setting the payload position led to incorrect attack attempts.
- **Metasploitable2 uses an older SSH server version** that may not be compatible with newer OpenSSH clients.  
  To connect successfully, you may need to use the following command:
  
  ```bash
  ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedKeyTypes=+ssh-rsa username@ip
  ```
  This forces the SSH client to accept the older `ssh-rsa` algorithm, which is deprecated in recent OpenSSH versions.  

* * * * *

## D. Mitigation Strategies
----------------------------

## Mitigation Strategies

| **Problem**                                    | **How to Fix It (Mitigation)**                                                                 |
|------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Brute Force Attacks**                        | Stop users from trying too many wrong passwords. Lock the account or add a delay after several failed tries. Use CAPTCHA. |
| **Plaintext Protocols (FTP, TELNET)**          | Don’t use FTP or TELNET because they send data without protection. Use **SFTP** or **SSH** instead, which are encrypted and safe. |
| **Weak Login Pages (like DVWA HTTP)**          | Use **HTTPS** so data is protected while moving on the internet. |
| **Username is Easy to Find (Enumeration)**     | Don’t show error messages that say if a username is correct or not. Use a general message like “Invalid login” for all failed logins. |