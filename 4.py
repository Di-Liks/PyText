import hashlib
import subprocess
import sys

# Зашитые данные о компьютере (полученные заранее)
HARD_CODED_CPU_ID = "BFEBFBFF000306C3"  # Пример ProcessorId
HARD_CODED_DISK_SERIAL = "WD-WCC6Y0XXXXX"  # Пример серийного номера диска
HARD_CODED_CPU_FREQ = "2700"  # Пример тактовой частоты в МГц

# Функция для получения ProcessorId
def get_cpu_id():
    try:
        result = subprocess.check_output("wmic cpu get ProcessorId", shell=True, text=True)
        cpu_id = result.splitlines()[1].strip()
        if cpu_id == "":
            raise ValueError("ProcessorId пустой")
        return cpu_id
    except Exception as e:
        print(f"Ошибка при получении ProcessorId: {e}")
        return None

# Функция для получения серийного номера диска
def get_disk_serial():
    try:
        result = subprocess.check_output("wmic diskdrive get SerialNumber", shell=True, text=True)
        serial = result.splitlines()[1].strip()
        if serial == "":
            raise ValueError("SerialNumber пустой")
        return serial
    except Exception as e:
        print(f"Ошибка при получении серийного номера диска: {e}")
        return None

# Функция для получения тактовой частоты процессора
def get_cpu_frequency():
    try:
        result = subprocess.check_output("wmic cpu get MaxClockSpeed", shell=True, text=True)
        frequency = result.splitlines()[1].strip()
        if frequency == "":
            raise ValueError("MaxClockSpeed пустой")
        return frequency
    except Exception as e:
        print(f"Ошибка при получении тактовой частоты процессора: {e}")
        return None

# Проверка данных системы
def check_system():
    cpu_id = get_cpu_id()
    disk_serial = get_disk_serial()
    cpu_freq = get_cpu_frequency()

    if cpu_id is None or disk_serial is None or cpu_freq is None:
        print("Ошибка: Не удалось получить необходимые данные о системе!")
        sys.exit(1)

    # Проверяем, совпадают ли данные с зашитыми значениями
    if cpu_id != HARD_CODED_CPU_ID:
        print("Ошибка: Несовпадение ProcessorId!")
        sys.exit(1)
    if disk_serial != HARD_CODED_DISK_SERIAL:
        print("Ошибка: Несовпадение серийного номера диска!")
        sys.exit(1)
    if cpu_freq != HARD_CODED_CPU_FREQ:
        print("Ошибка: Несовпадение тактовой частоты процессора!")
        sys.exit(1)

    print("Программа успешно запущена на привязанном компьютере.")

# Основная функция
if __name__ == "__main__":
    check_system()
