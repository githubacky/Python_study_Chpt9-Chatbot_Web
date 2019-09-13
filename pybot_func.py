def nagasa_command(command):
    cmd, text = command.split()
    length = len(text)
    response = '文字列 {} ノ長サハ {} 文字デス'.format(text, length)
    return response

def seireki_command(command):
    seireki, year_str = command.split()
    #try:
    if year_str.isdigit():
        year = int(year_str)
        if year >= 1989:
            gengo_year = year - 1988
            response = '西暦{}年ハ、平成{}年デス'.format(year, gengo_year)
        else:
            gengo_year = year - 1925
            response = '西暦{}年ハ、昭和{}年デス'.format(year, gengo_year)
    #except ValueError:
    else:
        response = '数値ヲ指定シテクダサイ'
    return response
