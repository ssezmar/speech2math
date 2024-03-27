from parsing_nums import text2latex
from draw_formula import show_formula
from recognize import recognize_speech

text = "открывается икс плюс икс закрывается умножить икс степени открывается корень открывается дробь числитель открывается икс закрывается знаменатель открывается пять миллионов пятьсот сорок пять тысяч семьсот пятьдесят три закрывается закрывается закрывается"
text = recognize_speech().lower()

latex = text2latex(text)
show_formula(latex, 'integral_formula.png')


