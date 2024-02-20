import netifaces
import psutil
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api')
def home():
    return 'Resources API'


@app.route('/api/memory')
def memory_stat():
    memory_data = {}
    memoire = psutil.virtual_memory()
    total_ram = f"{memoire.total / (1024 * 1024 * 1024):.2f} Go"
    available_ram = f"{memoire.available / (1024 * 1024 * 1024):.2f} Go"
    used_ram = f"{memoire.used / (1024 * 1024 * 1024):.2f} Go"
    percentage_used_ram = f"{memoire.percent:.2f}%"

    memory_data["total_ram"] = total_ram
    memory_data["available_ram"] = available_ram
    memory_data["used_ram"] = used_ram
    memory_data["percentage_used_ram"] = percentage_used_ram

    return jsonify(memory_data)


@app.route('/api/cpu')
def cpu_stat():
    cpu = {}
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu['cpu_usage'] = f"{cpu_usage}%"

    return jsonify(cpu)


@app.route('/api/disk')
def disk_stat():
    disk_statistics = psutil.disk_usage('/')
    disk_data = {}
    total_disk = disk_statistics.total / (1024 ** 3)
    used_disk = disk_statistics.used / (1024 ** 3)
    available_disk = disk_statistics.free / (1024 ** 3)
    percentage_used_disk = disk_statistics.percent

    disk_data['total_disk'] = f"{total_disk:.2f} Go"
    disk_data['used_disk'] = f"{used_disk:.2f} Go"
    disk_data['available_disk'] = f"{available_disk:.2f} Go"
    disk_data['percentage_used_disk'] = f"{percentage_used_disk:.2f}%"

    return jsonify(disk_data)


@app.route('/api/interfaces')
def interfaces_stat():
    interfaces_info = []

    interfaces = netifaces.interfaces()
    for interface in interfaces:
        interface_details = {'name': interface}
        inet_addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in inet_addresses:
            ipv4_info = inet_addresses[netifaces.AF_INET][0]
            if ipv4_info['addr']:
                interface_details['addr'] = ipv4_info['addr']
                interface_details['netmask'] = ipv4_info['netmask']
                interfaces_info.append(interface_details)

    return jsonify(interfaces_info)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
