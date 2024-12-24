import os


def display_menu():  # MENU
    menu = [
        'Cik',
        'Dosya Olustur',
        'Dosya Listesi',
        'Dosyaya Veri ekle',
        'Dosya Icerigi Analizi',
        'Dosya Sil',
    ]
    for queue, option in enumerate(menu):
        print(f'{queue}. {option}')
    target = input('Secim Yapiniz:')
    return target


def exit_program(var):  # EXIT
    if var == '0':
        print('Kapatiliyor...')
        raise SystemExit


def listed_files():  # LISTED FILES
    path = 'C:\\Users\\lorem\\Desktop\\fileio\\files\\'  # YOU CAN CHANGE PATH FOR TXT FILES
    for files in os.listdir(path):
        print(files)

    files = len(files)

    if not files:
        print('Klasorde dosya yok. Menuye donduruluyorsunuz...')
        return

    return path


def request_file_name():  # USER'S INPUT FOR FILE NAME
    file_name = input('Cikis --> 0 / Dosya adi giriniz:')

    exit_program(file_name)

    if file_name.endswith('.txt'):
        return file_name

    else:
        file_name = f'{file_name}.txt'
        return file_name


def create_file():
    try:
        path = listed_files()
        file_name = request_file_name()
        real_path = os.path.join(path, file_name)
        with open(real_path, 'x'):
            print('Dosya Basariyla Olusturuldu. Menuye Donduruluyorsunuz.')
            return

    except FileExistsError:
        print(f'{file_name} zaten var. Tekrar deneyiniz')
        return


def add_data():
    while True:
        path = listed_files()
        file_name = request_file_name()
        exit_program(file_name)
        real_path = os.path.join(path, file_name)  # COMBINES PATH AND FILE NAME

        if os.path.exists(path + file_name):
            try:
                with open(real_path, 'a') as file:
                    content = input('Icerigi Giriniz:')
                    file.write(content)
                    print('Ekleme Basarili. Eklenen Icerik: ' + content)
                    return

            except IOError:
                print('Hata: Ekleme islemi basarisiz. Tekrar deneyiniz.')
                continue

        else:
            print(f'{file_name} dosyasi bulunamadi. Tekrar deneyin.')
            continue


def analyze_file():
    while True:
        path = listed_files()
        file_name = request_file_name()
        real_path = os.path.join(path, file_name)
        exit_program(file_name)

        if os.path.exists(real_path):
            try:
                with open(real_path, 'r') as file:
                    chars = file.read()
                    chars = chars.splitlines()
                    char_count = 0
                    for char in chars:
                        char_count += len(char)

                    file.seek(0)  # CURSOR GOING BACK TO BEGGINING

                    rows = file.readlines()
                    rows_count = len(rows)

                    file.seek(0)  # CURSOR GOING BACK TO BEGGINING

                    words = file.read()
                    words = words.split()
                    words_count = len(words)

                    print(f'Karakter Sayisi: {char_count}')
                    print(f'Satir Sayisi: {rows_count}')
                    print(f'Kelime Sayisi: {words_count}')
                    print('Menuye Donduruluyorsunuz.')

            except Exception as error:
                print(f'Beklenmeyen Hata: {error} Tekrar Deneyin.')
                continue

        else:
            print(f'{file_name} dosyasi bulunamadi. Tekrar deneyin. Cikis --> 0')
            continue


def delete_file():
    while True:
        path = listed_files()
        file_name = request_file_name()
        exit_program(file_name)
        real_path = os.path.join(path, file_name)

        if os.path.exists(real_path):
            os.remove(real_path)
            print('Silme Islemi Basarili. Menuye Donduruluyorsunuz.')
            return
        else:
            print(f'{file_name} dosyasi bulunamadi. Tekrar deneyin. Cikis --> 0')
            continue
