import psutil


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

    return memory_data


print(memory_stat())