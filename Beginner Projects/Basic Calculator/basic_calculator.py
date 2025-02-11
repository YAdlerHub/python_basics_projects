import math

def calculator():
    while True:
        try:
            print("\n📌 בחר פעולה:")
            print("➕ חיבור (+)  |  ➖ חיסור (-)  |  ✖️ כפל (*)  |  ➗ חילוק (/)")
            print("📏 אחוזים (%)  |  🔢 חזקה (^)  |  🏁 שורש ריבועי (√)")
            
            operation = input("➡️ הכנס פעולה: ").strip()

            if operation in ['+', '-', '*', '/']:
                num1 = float(input("📌 הכנס מספר ראשון: "))
                num2 = float(input("📌 הכנס מספר שני: "))

                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        print("❌ שגיאה: לא ניתן לחלק באפס!")
                        continue
                    result = num1 / num2
            
            elif operation == '%':  # אחוזים
                num1 = float(input("📌 הכנס מספר: "))
                num2 = float(input("📌 הכנס את האחוז: "))
                result = (num1 * num2) / 100

            elif operation == '^':  # חזקה
                num1 = float(input("📌 הכנס מספר: "))
                num2 = float(input("📌 הכנס חזקה: "))
                result = num1 ** num2
            
            elif operation == '√':  # שורש ריבועי
                num1 = float(input("📌 הכנס מספר: "))
                if num1 < 0:
                    print("❌ שגיאה: לא ניתן לחשב שורש ריבועי למספר שלילי!")
                    continue
                result = math.sqrt(num1)
            
            else:
                print("❌ פעולה לא חוקית, נסה שוב.")
                continue

            print(f"✅ התוצאה: {result}")

        except ValueError:
            print("❌ שגיאה: יש להזין מספרים תקינים.")
            continue
        
        again = input("🔁 האם תרצה לבצע חישוב נוסף? (y/n): ").lower()
        if again != 'y':
            print("👋 תודה ולהתראות!")
            break

# הפעלת המחשבון
if __name__ == "__main__":
    calculator()
