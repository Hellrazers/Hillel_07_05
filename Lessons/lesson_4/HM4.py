from itertools import count
from shlex import split

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

# task 02 ==
""" Замініть .... на пробіл
"""
task = adwentures_of_tom_sawer.replace("\n", " ")
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

# for word in list_of_word.split()

    # if  word.istitle():
    #     count_of_word +=1
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""


# task 07
"""adwentures_of_tom_sawer Розділіть змінну  по кінцю речення. stip -> ['', ' Розділіть змінну  по кінцю речення...'
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр. '.' -> '. '  1.2  ...
"""


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
# not_ask = .count("!")  = 5
# if not_ask > 0:
#     split()



# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
import re

sentences = 'Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.'

list_of_re = re.findall( '\\w+',sentences)

print(list_of_re)
print(len(list_of_re))