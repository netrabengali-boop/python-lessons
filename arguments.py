def total_calc(bill_amount,tip_percentage):
    total=bill_amount*(1+0.01*tip_percentage) 
    total=round(total,2)
    print(f"Please Pay: ${total}")

total_calc(100,25)