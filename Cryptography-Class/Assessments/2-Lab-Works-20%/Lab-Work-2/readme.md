# Lab 2: Cracking Weak Password Hashes & Exploiting Poor Authentication

**Time Allocated:** 3 Hours  
**Total Marks:** 15  

---

## A. Objectives

1. Find and exploit weak crypto in database login and password storage.
2. Do offline cracking of password hashes found in the database.
3. Learn from real-world crypto mistakes and suggest better ways.
4. Write a report in GitHub (Markdown) and show a short demo.

---

## B. Lab Tasks

### 1. Service Enumeration and Initial Access

**Problem Faced:**  
When I tried to connect to the database using:

```
mysql -h 192.168.43.137 -u root
```

It showed this error:

```
ERROR 2026 (HY000): TLS/SSL error: wrong version number
```

![alt text](screenshots/error.png)

This happened because the MySQL client on my Kali machine tried to use SSL by default, but the target machine doesn’t support or is misconfigured for SSL connections.

**How I Fixed It:**  
So I used this command instead:

```
mysql -h 192.168.43.137 -u root --ssl=OFF
```

By adding `--ssl=OFF`, I disabled SSL so the client could connect using plain TCP, which worked. This also shows a security weakness because the database accepts unencrypted connections, which is risky because data (including usernames and passwords) could be sniffed on the network.

![alt text](screenshots/login.png)

---

### 2. User Enumeration and Weak Authentication

After connecting, I used this command to list the databases:
```
SHOW DATABASES;
```

Then I selected the dvwa database:
```
USE dvwa;
```

I listed the tables:
```
SHOW TABLES;
```

I found a users table and ran:
```
SELECT * FROM users;
```

**Findings:**

- Users had password hashes in the `users` table.
 
- The hashes looked weak (MD5).
 
- This is a problem because MD5 is old and easy to crack.
   