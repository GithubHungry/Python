paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
for ch in letters[:6]:
    print('\t', ch)
for ch in letters[-7:]:
    print('\t' * 2, ch)  # Двойной символ (*)
for ch in letters[12:20]:
    print('\t' * 3, ch)  # Тройной символ (*)
