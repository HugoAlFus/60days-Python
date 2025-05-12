import re
log_file = "../../assets/example/otros/app_example.log"

error_lines = 0
warning_lines = 0
info_lines = 0
debug_lines = 0
total_lines = 0

ips = set()

with open(log_file, "r") as file:
    for line in file:
        total_lines += 1

        if "ERROR" in line:
            error_lines += 1
        elif "WARNING" in line:
            warning_lines += 1
        elif "INFO" in line:
            info_lines += 1
        elif "DEBUG" in line:
            debug_lines += 1

        match = re.search(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', line)
        if match:
            ips.add(match.group())

print("📊 Estadísticas del Log:")
print(f"Total de entradas: {total_lines}")
print(f"Entradas con ERROR: {error_lines}")
print(f"Entradas con WARNING: {warning_lines}")
print(f"Entradas con INFO: {info_lines}")
print(f"Entradas con DEBUG: {debug_lines}")
print(f"IPs únicas encontradas: {len(ips)}")
print("Listado de IPs únicas:", ", ".join(ips))