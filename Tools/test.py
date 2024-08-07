import subprocess

package_name = "postgresql"
apt_command = ["sudo", "apt-get", "install", package_name]

try:
    subprocess.run(apt_command, check=True)
    print("Пакет успешно установлен")
except subprocess.CalledProcessError as e:
    print(f"Произошла ошибка: {e}")
