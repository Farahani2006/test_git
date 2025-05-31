import random

# دریافت ورودی از کاربر
num_participants = int(input("تعداد شرکت‌کنندگان را وارد کنید: "))
num_winners = int(input("تعداد برندگان را وارد کنید: "))

# بررسی اینکه تعداد برندگان از شرکت‌کنندگان بیشتر نباشد
if num_winners > num_participants:
    print("تعداد برندگان نمی‌تواند بیشتر از تعداد شرکت‌کنندگان باشد!")
else:
    # ساخت لیست شرکت‌کنندگان با شماره تلفن تصادفی
    participants = []
    for i in range(1, num_participants + 1):
        phone_number = "09" + "".join(random.choices("0123456789", k=9))
        participants.append((i, phone_number))  # (شماره شرکت‌کننده، شماره تلفن)

    # انتخاب تصادفی برندگان
    winners = random.sample(participants, num_winners)

    # نمایش نتایج
    print("\nبرندگان قرعه‌کشی:")
    for winner in winners:
        participant_id, phone = winner
        # مخفی کردن سه رقم وسط
        hidden_phone = phone[:4] + "***" + phone[7:]
        print(f"شرکت‌کننده شماره {participant_id} - شماره تلفن20: {hidden_phone}")

