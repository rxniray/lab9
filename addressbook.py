import sqlite3

base = sqlite3.connect('addressbook.db')
cur = base.cursor()

#base.execute('CREATE TABLE IF NOT EXISTS {}(id, name, lastname, surname, mail, phone, address)'.format('addbook'))
base.execute('CREATE TABLE IF NOT EXISTS {}(id PRIMARY KEY, name text, lastname text, surname text, mail text, phone text, address text)'.format('addbook'))
base.commit()
while True:
    v = int (input('Яку операцюю бажаєте виконати? \n 1. Додати рядок; \n 2. Подивитися рядки; \n 3. Оновити рядок; \n 4. Видалити рядок;\n 5. Вийти з програми.\n\n'))

    if v == 1:
        print('\nВведiть первинний ключ: \n')
        n1 = input()
        print('\nВведiть iмя: \n')
        n2 = input()
        print('\nВведiть призвище: \n')
        n3 = input()
        print('\nВведiть по батькові: \n')
        n4 = input()
        print('\nВведiть пошту: \n')
        n5 = input()
        print('\nВведiть номер телефону: \n')
        n6 = input()
        print('\nВведiть адрес: \n')
        n7 = input()

        cur.execute('INSERT INTO addbook VALUES(?, ?, ?, ?, ?, ?, ?)', (n1, n2, n3, n4, n5, n6, n7))
        base.commit()

        print('\nВставка успішно виконена!\n')

    if v == 2:
        q = int (input('Ви бажаєте глянути всі рядки чи тільки один рядок? \n 1. Всі рядки; \n 2. Один рядок. \n'))
        
        if q == 1:

            s = cur.execute('SELECT * FROM addbook').fetchall()
            print(s)
        
        if q == 2:
            n = input('Введіть первинний ключ: \n')

            s = cur.execute('SELECT * FROM addbook WHERE id == ?',(n,)).fetchall()
            print(s)

    if v == 3:

        print('\nВведiть первинний ключ ряка якого хочете замінити: \n')
        n1 = input()

        print('\nВведiть нове iмя: \n')
        n2 = input()
        print('\nВведiть нове призвище: \n')
        n3 = input()
        print('\nВведiть по батькові: \n')
        n4 = input()
        print('\nВведiть нову пошту: \n')
        n5 = input()
        print('\nВведiть новий номер телефону: \n')
        n6 = input()
        print('\nВведiть новий адрес: \n')
        n7 = input()

        cur.execute('UPDATE addbook SET name == ?, lastname == ?, surname == ?, mail == ?, phone == ?, address == ?  WHERE id == ?', (n2, n3, n4, n5, n6, n7, n1))
        base.commit()

        print('\nЗміна рядка успішно виконена!\n')

    if v == 4:
        
        print('\nВведiть первинний ключ ряка якого хочете видалити: \n')
        
        n1 = input()

        cur.execute('DELETE FROM addbook WHERE id == ?', (n1,))
        base.commit()

        print('\nВидалення рядка успішно виконано!\n')

    if v == 5:
        break

    