# # Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# # Декілька правил:
# # ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# # підсумкова довжина hashtag має бути не більше 140 символів.
# # кожне слово починається з великої літери.
# # якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

# import string

# user_string = input('Введите строку: ').title()

# hashtag = ''.join(c for c in user_string if c not in string.punctuation and c != ' ')

# if len(hashtag) > 140:
#     hashtag = hashtag[:140]

# print(f'#{hashtag}')
