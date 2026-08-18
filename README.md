# Network Monitor

Simulated multi-factor authentication system with network device monitoring and firewall threat detection.

---

## 🎯 What It Does

- **User Authentication**: Username/password validation with biometric fingerprint scanning
- **Firewall Monitoring**: Detects and blocks malicious traffic
- **Device Connection**: Tests router, server, switch, and wireless access point connectivity
- **Device Inventory**: Tracks 19 devices (7 core, 4 wired, 8 wireless) with IP addresses and serial numbers

---

## 📂 Project Structure

| File | Purpose |
|------|---------|
| `network.py` | Main orchestrator - instantiates all classes and executes flow |
| `access/access.py` | `Credentials` class (username/password auth) & `BiometricScan` class (fingerprint) |
| `server/server.py` | Device classes: `firewall`, `router`, `server`, `switch`, `WAP`, `DeviceCount` + device inventory (19 devices, IP range 192.168.1.x) |
| `test/test.py` | Unit tests for authentication and biometric scanning |

---

## ⚙️ Installation & Run

**Requirements**: Python 3.7+

```bash
# Run the application
python network.py

# Run tests
python -m unittest test.test -v
```

---

## 🚀 Usage

Execute `python network.py` to start the authentication flow:

1. Enter credentials from the predefined list (e.g., `name1` / `str1`)
2. Pass biometric fingerprint scan
3. Firewall checks for threats
4. Verify device connections (router, server, switch, WAP)

**Valid test credentials** (name/password must match index positions):
- `name1` / `str1`
- `name2` / `str2`
- `name3` / `str3`
- `name4` / `str4`
- `name5` / `str5`

---

## 📊 Execution Flow

```
Login (Credentials) → Fingerprint Scan → Firewall Check → Device Connectivity → Ready
```

---

## 🧪 Testing

```bash
python -m unittest test.test
```

Tests cover:
- Valid login with correct credentials
- Invalid login with wrong credentials
- Successful fingerprint authentication
- Failed fingerprint authentication
