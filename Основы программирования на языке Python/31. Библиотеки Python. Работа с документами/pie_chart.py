import sys
import xlsxwriter


workbook = xlsxwriter.Workbook('res.xlsx')
worksheet = workbook.add_worksheet()

parameters, values = list(zip(*map(lambda x: (x.split()[0], int(x.split()[1])), sys.stdin)))
worksheet.write_column('A1', parameters)
worksheet.write_column('B1', values)

chart = workbook.add_chart({'type': 'pie'})
chart.add_series({
    'categories': f"=Sheet1!{'A1:A'+str(len(parameters))}",
    'values': f"=Sheet1!{'B1:B'+str(len(parameters))}"
})
worksheet.insert_chart('C3', chart)

workbook.close()