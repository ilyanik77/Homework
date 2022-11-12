import model
import view

def run():
    option = view.show_menu()
    if option == '1':
        user = view.add_info()
        model.add_data( user)
        model.print_all_data()

    elif option == '2':
        lastname = view.apdate_info()
        index = view.get_index()
        model.update_data( index, lastname)
        model.print_all_data()

    elif option == '3':
        model.print_all_data()

    elif option == '4':
        index = view.get_index()
        model.print_user_data(index)

    elif option == '5':
        index = view.get_index()
        model.delete_user(index)
        model.print_all_data()

    elif option == '6':
        tel = view.get_tel()
        index = view.get_index()
        model.update_tel(index, tel)
        model.print_all_data()
