import psutil

cpu_percent = psutil.cpu_percent(interval=1)
cpu_freq = psutil.cpu_freq()

memory = psutil.virtual_memory()
mem_usage = memory.percent

net = psutil.net_io_counters()
net_sent = net.bytes_sent
net_recv = net.bytes_recv

print("Psutil System Fetch")
print("----------------------------------")
print(f"CPU Usage: {cpu_percent}%")
print(f"CPU Frequency: {int(cpu_freq.current)} MHz")
print("----------------------------------")
print(f"Memory Usage: {mem_usage}%")
print("----------------------------------")
print(f"Network Sent: {net_sent} bytes")
print(f"Network Received: {net_recv} bytes")
