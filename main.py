import platform

from LinuxCore.LinuxInstaller import offline_install_linux, online_install_linux
from WindowsCore.WindowsInstaller import online_install_windows, offline_install_windows
from Tools.logger import log_to_file


# Запрашиваем формат установки (с инетом или без)
def installation_method_prompt():
    question = "Как будем устанавливать программу: 1 - Оффлайн, 2 - Онлайн? "
    while True:
        try:
            choice = int(input(question))
            if choice == 1:
                print("Вы выбрали оффлайн установку.")
                log_to_file("Пользователь выбрал оффлайн установку.")
                return 1
            elif choice == 2:
                print("Вы выбрали онлайн установку.")
                log_to_file("Пользователь выбрал онлайн установку.")
                return 2
            else:
                print("Неверный выбор, пожалуйста, введите 1 или 2.")
                log_to_file("Пользователь еблан и не смог выбрать 1 или 2 при выборе типа установки")
        except ValueError:
            print("Пожалуйста, введите число 1 или 2.")


def main():
    installation_type = installation_method_prompt()  # Получаем тип установки

    # Создаем словарь действий в зависимости от типа установки
    actions = {
        1: {"message": "Оффлайн установка", "Windows": offline_install_windows, "Linux": offline_install_linux},
        2: {"message": "Онлайн установка", "Windows": online_install_windows, "Linux": online_install_linux}
    }

    # Выполняем соответствующее действие
    action = actions.get(installation_type)
    if action:
        #print(action["message"])
        #Определяем ОС
        system = platform.system()
        install_func = action.get(system)
        if install_func:
            install_func()
        else:
            print("Неизвестная операционная система")
            log_to_file("Неизвестная операционная система")
    else:
        print("Неверный выбор, пожалуйста, введите 1 или 2.")


if __name__ == "__main__":
    log_to_file("-------------------------------------------------")
    log_to_file("Запуск программы")
    main()
