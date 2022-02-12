from docxtpl import DocxTemplate


def make_marks(*args):
    args = sorted(args, key=lambda x: x[0])
    args = map(lambda a, b: (a, ) + b, range(1, len(args) + 1), args)
    args = map(lambda x: dict(zip(('num', 'fio', 'mark'), x)), args)
    return list(args)


def create_training_sheet(class_name, subject_name, tpl_name, *marks):
    marks = make_marks(*marks)
    doc = DocxTemplate(tpl_name)
    context = {
        'class_name': class_name,
        'subject_name': subject_name,
        'marks': marks
    }
    doc.render(context)
    doc.save('res.docx')


create_training_sheet("3И", "Математика", "tpl.docx",
                      ("Петров Петр", "5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла"),
                      ("Иванов Иван", "5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла"),
                      ("Сергеев Сергей", "3"),
                      ("Никитин Никита", "4. QT 1. Что такое QT и PyQT. Знакомство"))