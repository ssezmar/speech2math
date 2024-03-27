import words2numsrus
from extractor import NumberExtractor
from extract_math import text_to_latex

def text2latex(text):
    extractor = NumberExtractor()
    for match in extractor(text):
        match.fact
    latex_text = text_to_latex(extractor.replace_groups(text))
    print(latex_text)
    return latex_text












