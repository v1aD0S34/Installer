from Tools.logger import log_to_file


def online_install_linux():
    # ППРОВЕРИТЬ НАЛИЧИЕ ИНЕТА
    log_to_file("Выполняется установка компонентов под управлением Линукса Онлайн ")
    print("Код запущен под управлением Linux С ИНЕТОМ")


def offline_install_linux():
    log_to_file("Выполняется установка компонентов под управлением Линукса Оффлайн ")
    print("Код запущен под управлением Linux БЕЗ ИНЕТА ")