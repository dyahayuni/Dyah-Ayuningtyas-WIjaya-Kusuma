users_terbaru = ['admin', 'kdy', 'yjh', 'kjk', 'ysh']
users_baru = ['admin', 'kdy', 'ash', 'bmg', 'kth']

users_terbaru_lower = [user.lower() for user in users_terbaru]

for user_baru in users_baru:
    if user_baru.lower() in users_terbaru_lower:
        print(f"Maaf {user_baru}, username sudah digunakan. Silakan pilih username lain.")
    else:
        print(f"Selamat {user_baru}, username tersedia.")