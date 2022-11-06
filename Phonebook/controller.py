import model
import view

def run():
    option = view.show_menu()
    if option == '1':
        res = model.readFile()
        print(res)
    elif option == '2':
        res = model.read_csv()
        view.show_res(res)
    elif option == '3':
        in_info = view.add_txt()
        res = model.writeFile(in_info)
        print(res)
    elif option == '4':
        in_info = view.add_info()
        model.write_csv(in_info)