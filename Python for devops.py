# Hands on: disk usage calculation 
"""
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
"""

# Hands on: Working with lists
"""
deployment_targets = ['us-east1', 'eu-west1', 'ap-southeast-2']
print(deployment_targets[0]) # prints 'us-east1'
deployment_targets.append('sa-east2') # adds 'sa-east1' to the end of the list
print(deployment_targets) # prints ['us-east1', 'eu-west1', 'ap-southeast-2', 'sa-east2']
deployment_targets[1] = 'eu-central-1' # changes 'eu-west1' to 'eu-central-1'
print(deployment_targets) # prints ['us-east1', 'eu-central-1', '
"""

# Hands on: Working with sets

required_packages = set(['python3', 'pip', 'requests', 'bots3', 'pip'])
print(required_packages)
print('requests' in required_packages) # prints True
print('ansible' in required_packages) # prints False
print(f"Is 'requests' required? {'requests' in required_packages}")
print(f"Is 'ansible' required? {'ansible' in required_packages}")
required_packages.add("parmiko") # adds 'paramiko' to the set
required_packages.discard('pip') # removes 'pip' from the set
print(required_packages) # prints {'python3', 'requests', 'bots3', 'paramiko'}

installed = {'docker', 'python3', 'pip', }
missing_packages = required_packages - installed
extra_packages = installed - required_packages
common_packages = required_packages & installed

print(f"Missing packages: {missing_packages}")
print(f"Extra packages: {extra_packages}")
print(f"Common packages: {common_packages}")

# Hands on: Working with disctionaries