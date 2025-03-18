# 🔄 Keep Server Alive (Render)

This project ensures that a server hosted on **Render** remains active by periodically pinging it using a **Python script** and an additional route to handle external requests.

---

## 🚀 Problem Statement
Render automatically stops free-tier servers after a period of inactivity. To prevent this, we:
1. Created a **Python script** that periodically pings the server with a POST request.
2. Added an **extra route** in the backend to respond to status checks.

---

## 🛠️ Solution Implementation

### 1️⃣ **Creating a Status Route**
Add the following route in your **Node.js/Express** backend:

```javascript
app.post("/api/v1/status", (req, res) => {
    res.status(200).json({ message: "Server is active" });
});
```

### 2️⃣ **Using a Python Script to Ping the Server**
Use the Python script mentioned above to periodically ping the server and keep it active.

### 3️⃣ **Automating the Script**
Use a **cron job** (Linux/macOS) or **Task Scheduler** (Windows) to run the script automatically.

#### Example (Linux/macOS):
```sh
crontab -e
```
Add this line to run the script every 9 minutes:
```sh
*/9 * * * * python3 /path/to/keep_alive.py
```

---

## 🔧 Requirements

- Python 3.x
- Requests library (`pip install requests`)
- Node.js & Express backend

---

## 👨‍💻 Contributors

- **[Prathamesh Prabhakar Devrukhakar](https://github.com/im-prathamesh-dev)**


---

## 📜 License

This project is licensed under the **MIT License**.

🚀 **Now your Render server stays active without interruptions!**
