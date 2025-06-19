# แยกข้อความ
radio_data = "HS1ABC,14.205,100,USB,Normal"
# แยกข้อมูล
parts = radio_data.split(",")
# 0 1 2 3 >>>>
# List []
call_sing = str(parts[0])
frequency = float(parts[1])
power = int(parts[2])
mode = str(parts[3])
status = str(parts[4])

print(F"นามเรียกขาน : {call_sing}")
