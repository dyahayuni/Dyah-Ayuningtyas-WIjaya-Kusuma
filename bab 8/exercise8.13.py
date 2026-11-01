def build_profile(first, last, **user_info):
    """Membuat dictionary berisi informasi tentang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'kim', 'doyoung',
    city='Surakarta',
    hobby='membaca',
    field='kedokteran',
)
print(user_profile)