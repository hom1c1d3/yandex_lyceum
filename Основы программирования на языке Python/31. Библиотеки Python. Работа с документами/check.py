import xlsxwriter


def export_check(text):
    workbook = xlsxwriter.Workbook('res.xlsx')
    worksheet = workbook.add_worksheet()

    row = 1
    col = 1
    for row, data in enumerate(text.splitlines()):
        for col, data_col in enumerate(data.split('\t')):
            worksheet.write(row, col, int(data_col) if col > 0 else data_col)
        worksheet.write(row, col + 1,
                        f'={chr(ord("A") + col - 1)}{row + 1}*{chr(ord("A") + col)}{row + 1}')
    worksheet.write(row + 1, 0, 'Итого')
    worksheet.write(row + 1, col + 1,
                    f'=SUM({chr(ord("A") + col + 1)}{1}:{chr(ord("A") + col + 1)}{row + 1})')

    workbook.close()


export_check('''товар 1	100	5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла
товар 2	200	6
товар 3	7	500''')
