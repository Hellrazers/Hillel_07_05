from jinja2.lexer import operator_re

string = "Це приклад для Це пошуку у рядку. Це" #[0 ....],

# Пошук індексу першого входження підстрічки
index = string.find("Це", 13 , 25) # повертає індекс елменту де починаєтся перша літера
if index != -1:
    print(f"Знайдено на позиції {index}.")
else:
    print("Підстрічка не знайдена.")
    print(index)


#STRIP

row_ = "!    Привіт, світ!    !"
row_clear = row_.strip('!').strip()

print("Оригінальний рядок:", row_)
print("Очищений рядок:", row_clear)  # > Привіт, світ!


print(f'lstrip = {row_.lstrip('!').lstrip()}')

print(f'rstrip = {row_.rstrip('!').rstrip()}')



#