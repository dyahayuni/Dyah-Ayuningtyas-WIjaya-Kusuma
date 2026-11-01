usernames = ['admin', 'kdy', 'yjh', 'kjk', 'ysh']
for username in usernames:
    if username == 'admin':
        print("halo admin, apakah kamu ingin melihat laporan sistem hari ini?")
    else:
        print(f"halo {username}, terima kasih telah masuk ke sistem.")
else:
    print("kita perlu mencari beberapa pengguna!")
