from __future__ import absolute_import, annotations


def decode_string(s):
    stack = []  # מחסנית לאחסון מצב
    current_string = ""  # מחרוזת פעילה
    current_number = 0  # מספר פעיל

    for char in s:
        if char.isdigit():
            # בניית מספר במקרה של יותר מספרה אחת
            current_number = current_number * 10 + int(char)
        elif char == "[":
            # דוחפים למחסנית את המחרוזת והמספר הנוכחיים
            stack.append((current_string, current_number))
            current_string = ""  # מאפסים מחרוזת פעילה
            current_number = 0  # מאפסים מספר פעיל
        elif char == "]":
            # שולפים מהמחסנית את המחרוזת והמספר
            last_string, repeat_number = stack.pop()
            # בונים מחרוזת על בסיס חזרות
            current_string = last_string + (current_string * repeat_number)
        else:
            # מוסיפים תו למחרוזת הפעילה
            current_string += char

    return current_string


# דוגמה לשימוש
ENCODED = "2[L[2[FF]]]"
decoded = decode_string(ENCODED)
print(decoded)  # אמור להדפיס "LFFLFF"
