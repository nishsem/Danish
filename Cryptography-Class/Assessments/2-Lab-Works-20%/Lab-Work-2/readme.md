# Lab 2: Cracking Weak Password Hashes & Exploiting Poor Authentication

**Time Allocated:** 3 Hours  
**Total Marks:** 15  

---

## 1. Service Enumeration and Initial Access

**Problem Faced:**  
When I tried to connect to the database using:

```
mysql -h 192.168.43.137 -u root
```

It showed this error:

```
ERROR 2026 (HY000): TLS/SSL error: wrong version number
```

**How I Fixed It:**  
I turned off SSL using this command:

```
mysql -h 192.168.43.137 -u root --ssl=OFF
```

Now I could successfully connect. I used `--ssl=OFF` because the server doesn’t support SSL/TLS properly.

* * *