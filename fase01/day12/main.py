exit = False
task_list = []


def _action_choose(option_choose, task_list):
    match option_choose:
        case 1:
            print("\n".join(task_list))
        case 2:
            task_list.append(input("¿Que tarea quiere añadir?: "))
        case 3:
            return True


while not exit:
    try:
        option = int(input(
            "--Indique una acción--\n1.Visualizar lista\n2.Añadir tarea\n3.Salir\nPor favor indiquelo con un número "
            "de (1,3): "))
        exit = _action_choose(option, task_list)
    except ValueError:
        print("Introduzca un valor válido")
        print("--------------------------------------------------")
