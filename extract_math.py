def text_to_latex(text):
    # Словарь для соответствия слов и математических символов
    replacements = {
        "интеграл": r"\int",
        "открывается": "(",
        "закрывается": ")",
        "плюс": "+",
        "минус": "-",
        "умножить": "*",
        "делить": "/",
        "и": ",",
        "д": "d",
        "икс": "x",
        "степени": "^`",
        "дробь": r"\frac",
        "знаменатель": "`",
        "числитель": "`",
        "√": r"\sqrt`"

        # добавьте другие соответствия по мере необходимости
    }

    # Преобразование текста в список слов
    words = text.split()

    # Преобразование каждого слова
    latex_formula = ""
    for word in words:
        if word.lower() in replacements:
            latex_formula += replacements[word.lower()]
        else:
            latex_formula += word

    for sym_open in range(0, len(latex_formula)):
        if latex_formula[sym_open-1] == "`" and latex_formula[sym_open] == "(":
            latex_formula = latex_formula[:sym_open] + "{" + latex_formula[sym_open+1:]
            for sym_close in range(sym_open, len(latex_formula)):
                if latex_formula[sym_close] == ")":
                    latex_formula = latex_formula[:sym_close] + "}" + latex_formula[sym_close+1:]
                    break

    latex_formula = latex_formula.replace("`", "")


    print(latex_formula)

    return "$" + latex_formula + "$"

