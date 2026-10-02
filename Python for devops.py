# Hands on: disk usage calculation
server_name = "webserver-03"
cpu_cores = 4
memory_gb = 8.0
disk_total_gb = 500.0
disk_used_gb = 350.0
disk_free_gb = disk_total_gb - disk_used_gb
disk_usage_percent = (disk_used_gb / disk_total_gb) * 100
print(disk_usage_percent)

summary = f"Server {server_name.upper()} ({cpu_cores} cores, {memory_gb}GB RAM) Disk usage: {disk_usage_percent}%" 
print(summary)

summary_formated = f"Server {server_name.upper()} ({cpu_cores} cores, {memory_gb}GB RAM) Disk usage: {disk_usage_percent: .2f}%" 
print(summary_formated)