question = "Как дела? "
answer = input(question).lower()

if "не" in answer or "?" in answer:
    print("Просто без комментариев")

elif "хорош" in answer \
        or "прекрасн" in answer \
        or "отличн" in answer \
        or "супер" in answer:
    print("Отлично, у меня тоже всё хорошо :)")

elif "плох" in answer or "ужасн" in answer:
    print("Ничего, скоро всё наладится")

else:
    print("Просто без комментариев")
