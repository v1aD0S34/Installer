from Tools.logger import log_to_file


def online_install_windows():
    # ППРОВЕРИТЬ НАЛИЧИЕ ИНЕТА
    log_to_file("Выполняется установка компонентов под управлением Windows Онлайн ")
    print("Такого функционала нет и не будет!")


def offline_install_windows():
    log_to_file("Выполняется установка компонентов под управлением Windows Оффлайн ")
    print("Код запущен под управлением Windows БЕЗ ИНЕТА")
