import xlsxwriter
from itertools import groupby


def export_check(text):
    workbook = xlsxwriter.Workbook('res.xlsx')

    for sheet in text.split('---\n'):
        worksheet = workbook.add_worksheet()
        row = 1
        col = 1
        sheet = [[j for j in i.split('\t')] for i in sheet.splitlines()]
        sheet = [[i[0]] + list(map(int, i[1:])) for i in sheet]
        sheet = sorted(sheet, key=lambda x: x[:2])
        sheet = [list(v) for k, v in groupby(sheet, lambda x: x[:2])]
        sheet = [i[0][:2] + [sum(list(zip(*i))[2])] for i in sheet]
        sheet = sorted(sheet, key=lambda x: [x[0]] + [x[2]])
        for row, data in enumerate(sheet):
            for col, data_col in enumerate(data):
                worksheet.write(row, col, int(data_col) if col > 0 else data_col)
            worksheet.write(row, col + 1,
                            f'={chr(ord("A") + col - 1)}{row + 1}*{chr(ord("A") + col)}{row + 1}')
        worksheet.write(row + 1, 0, 'Итого')
        worksheet.write(row + 1, col + 1,
                        f'=SUM({chr(ord("A") + col + 1)}{1}:{chr(ord("A") + col + 1)}{row + 1})')

    workbook.close()


export_check('''товар 1	100	5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла
товар 2	200	6
товар 3	7	500
товар 1	5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла	23
яблоко	10	10
банан	20	15
товар 1	100	5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла
товар 2	200	6
товар 3	7	500
товар 1	5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла	23
яблоко	10	10
банан	20	15
---
товар 1	100	5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла
товар 2	200	6
товар 3	7	500
товар 1	5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла	23
яблоко	10	10
груша	20	15
---
товар 1	100	5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла
товар 2	200	6
товар 3	7	500
товар 1	100	5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла
товар 2	200	6
товар 3	7	500''')