videos = [
"How To Make a Concrete Fire Bowl http://youtu.be/DwJpy48GZF0",
"Making a table top FIRE PIT http://youtu.be/DwJpy48GZF0",
"MODERN Outdoor Concrete and Wood http://youtu.be/zD-lSfDSKn0",
"Diy LED Desk Lamp With Concrete Base http://youtu.be/a5yiMhJaGCo"
]
playlists = [
"Оборудование для мастерской своими руками",
"Литье металла",
"Работа по дереву"
]
count_seek = 0  # Счетчик найденных результатов поиска

while True:
    menu = input("\nПривет, это Stepik ***, портал по видео про ****.\n"
                 "Введите 1, чтобы посмотреть видео, 2 чтобы найти видео,"
                 "3 чтобы посмотреть плейлисты"
                 "exit или 0 чтобы выйти\n")
    if menu == "1":
        print(f"У нас нашлось {len(videos)} видео\n")
        for i in videos:
            print(i)
    elif menu == "2":
        seek = input("Введите слово для поиска:\n")
        for i in videos:
            if seek.lower() in i.lower():
                count_seek += 1
        if count_seek > 0:
            print(f"У нас нашлось {count_seek} видео по запросу {seek}\n")
            for i in videos:
                if seek.lower() in i.lower():
                    print(i)
            count_seek = 0
    elif menu == "3":
        print(f"У нас нашлось {len(playlists)} плейлиста(ов)\n")
        for i in playlists:
            print(i)
    elif menu == "0" or menu == "exit":
        break