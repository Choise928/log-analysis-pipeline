import pandas as pd
import re
import matplotlib.pyplot as plt

# File Configuration
log_path = "server.log"
csv_path = "processed_logs.csv"
img_path = "log_analysis_chart.png"

# 1. Define Regex Pattern (parsing unstructured text)
# Pattern: Timestamp [Level] Message
log_pattern = re.compile(r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] (?P<message>.*)')

data = []

print("🔄 Starting Log Parsing & Analysis Pipeline...")

# 2. Read and Parse the Log File
try:
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                data.append(match.groupdict())
except FileNotFoundError:
    print("❌ Error: 'server.log' not found. Please run dummy_logs.py first!")
    exit()

# 3. Convert to Pandas DataFrame
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp']) # Convert string to datetime object

print(f"✅ Parsing Complete! Structured {len(df)} log entries.")

# 4. Data Analysis (Filter specific error events)
error_df = df[df['level'].isin(['ERROR', 'CRITICAL'])]
print(f"🚨 Critical Errors Detected: {len(error_df)}")

# 5. Export to CSV (Automated Reporting)
df.to_csv(csv_path, index=False)
print(f"💾 CSV Report Saved: {csv_path}")

# 6. Visualization (Generate Chart for README)
plt.figure(figsize=(10, 6))
# Set colors for each log level
colors = {'INFO': 'blue', 'WARNING': 'orange', 'ERROR': 'red', 'CRITICAL': 'black'}
level_counts = df['level'].value_counts()

# Plot bar chart
level_counts.plot(kind='bar', color=[colors.get(x, 'gray') for x in level_counts.index])
plt.title('System Log Level Distribution')
plt.xlabel('Log Level')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save chart as image
plt.savefig(img_path)
print(f"📈 Chart Image Saved: {img_path}")