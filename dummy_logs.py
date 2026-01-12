import random
from datetime import datetime, timedelta

# 1. Configuration: Generate 500 lines of logs
log_count = 500
log_file = "server.log"

# 2. Mock Message List
messages = [
    ("INFO", "User logged in successfully"),
    ("INFO", "Data sync completed"),
    ("WARNING", "High memory usage detected (85%)"),
    ("ERROR", "Database connection timeout (Code: 504)"),
    ("ERROR", "NullPointerException in auth module (Code: 500)"),
    ("CRITICAL", "Server crash imminent! Shutting down.")
]

# 3. Log Generation Logic
print(f"🛠️ Generating dummy logs... ({log_file})")

with open(log_file, "w", encoding="utf-8") as f:
    base_time = datetime.now()
    
    for _ in range(log_count):
        # Generate random timestamp (simulate past events)
        time_offset = random.randint(0, 10000)
        log_time = base_time - timedelta(seconds=time_offset)
        timestamp = log_time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Randomly select a log level and message
        level, msg = random.choice(messages)
        
        # Write to file format: [Timestamp] [Level] Message
        f.write(f"{timestamp} [{level}] {msg}\n")

print(f"✅ Generation Complete! Generated {log_count} lines in '{log_file}'.")