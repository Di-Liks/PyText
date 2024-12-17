import hashlib
import os
import subprocess

# Функция для получения серийного номера диска
def get_disk_serial():
    try:
        result = subprocess.check_output("wmic diskdrive get SerialNumber", shell=True, text=True)
        serial = result.splitlines()[1].strip()
        return serial
    except Exception as e:
        return "DiskSerialNotFound"

# Функция для получения информации о процессоре
def get_cpu_info():
    try:
        result = subprocess.check_output("wmic cpu get ProcessorId", shell=True, text=True)
        cpu_id = result.splitlines()[1].strip()
        return cpu_id
    except Exception as e:
        return "CPUNotFound"

# Функция для получения тактовой частоты процессора
def get_cpu_frequency():
    try:
        result = subprocess.check_output("wmic cpu get MaxClockSpeed", shell=True, text=True)
        frequency = result.splitlines()[1].strip()
        return frequency
    except Exception as e:
        return "FrequencyNotFound"

# Функция для генерации HWID (хеша уникальных данных)
def generate_hwid():
    # Получаем характеристики компьютера
    cpu_id = get_cpu_info()
    disk_serial = get_disk_serial()
    cpu_frequency = get_cpu_frequency()

    # Объединяем данные в строку
    unique_data = f"{cpu_id}-{disk_serial}-{cpu_frequency}"
    
    # Генерируем хеш
    hwid_hash = hashlib.sha256(unique_data.encode()).hexdigest()
    return hwid_hash

# Функция для проверки HWID
def check_hwid():
    saved_hwid_file = "hwid.txt"

    # Генерируем HWID текущего компьютера
    current_hwid = generate_hwid()

    # Если файл с сохранённым HWID существует, проверяем его
    if os.path.exists(saved_hwid_file):
        with open(saved_hwid_file, "r") as file:
            saved_hwid = file.read().strip()
            if current_hwid == saved_hwid:
                print("Программа успешно запущена на привязанном компьютере.")
            else:
                print("Ошибка: программа не может быть запущена на этом компьютере!")
                exit()
    else:
        # Если файла нет, сохраняем HWID
        with open(saved_hwid_file, "w") as file:
            file.write(current_hwid)
        print("Привязка к текущему компьютеру выполнена успешно. Перезапустите программу.")

# Основная функция
if __name__ == "__main__":
    check_hwid()
