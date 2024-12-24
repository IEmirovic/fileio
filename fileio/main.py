from func import (
    listed_files,
    create_file,
    add_data,
    analyze_file,
    delete_file,
    display_menu,
)


def main():
    while True:
        try:
            choice = display_menu()

            if choice == '0':
                print('Kapatiliyor...')
                raise SystemExit
            elif choice == '1':
                create_file()
            elif choice == '2':
                listed_files()
            elif choice == '3':
                add_data()
            elif choice == '4':
                analyze_file()
            elif choice == '5':
                delete_file()
            else:
                print('Gecerli Bir Deger Giriniz.')

        except Exception as error:
            print(f'Beklenmeyen Hata: {error}')


if __name__ == "__main__":
    main()
