# error handling
try:
    frequency = float(input("ความถี่ (MHz): "))
    if frequency < 0:
        print(f"ความถี่ต้องเป็นจำนวนบวก")
    else:
        print(f"ความถี่ที่ตั้งค่า: {frequency} MHz")
except ValueError :
    print("กรุณาใส่ตัวเลขเท่านั้น")