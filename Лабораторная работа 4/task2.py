def get_count_char(str_):
    str_symbol_dict = {}
    count = 0
    str_lower = str_.lower()
    str_lower_words = str_lower.split()
    str_lower_words.sort()
    str_separated = " ".join(str_lower_words)
    str_list = list(str_separated)
    str_list =  [i  for i in str_list if i.isalpha() == True]
    for symbol in str_list:
        str_symbol_dict[symbol] = str_symbol_dict.get(symbol, count) + 1
    return str_symbol_dict

def ratio(main_dict):
    symbol_ratio_dict = {}
    for symbol, count in main_dict.items():
        symbol_ratio_dict[symbol] = count * 100/sum(main_dict.values())
    return symbol_ratio_dict



main_str = """Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!"""
print(get_count_char(main_str))
print(ratio(get_count_char(main_str)))
