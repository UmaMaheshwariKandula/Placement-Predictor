import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'placement_app.settings')
django.setup()

from placement_app.models import MockTest, MockTestQuestion

print("="*60)
print("CREATING COMPLETE MOCK TESTS")
print("="*60)

# ============================================================
# 1. APTITUDE TEST - 100 QUESTIONS
# ============================================================
print("\n📊 Creating Aptitude Master Test...")

aptitude_test = MockTest.objects.create(
    title="Aptitude Master Test",
    category="aptitude",
    time_limit=90,
    passing_score=50
)

aptitude_questions = []

# Quantitative Aptitude (50 questions)
qa_questions = [
    {"q": "If a shopkeeper sells at 20% profit, CP=₹500, SP=?", "a": "₹550", "b": "₹600", "c": "₹650", "d": "₹700", "ans": "B", "exp": "SP = 500 + 20% = ₹600"},
    {"q": "Next in sequence: 2, 6, 12, 20, ?", "a": "28", "b": "30", "c": "32", "d": "36", "ans": "B", "exp": "+4,+6,+8,+10 = 30"},
    {"q": "5 workers take 10 days. 10 workers take?", "a": "3", "b": "4", "c": "5", "d": "6", "ans": "C", "exp": "5×10=50, 50/10=5 days"},
    {"q": "15% of 200 = ?", "a": "20", "b": "25", "c": "30", "d": "35", "ans": "C", "exp": "15/100 × 200 = 30"},
    {"q": "x + 5 = 12, x = ?", "a": "5", "b": "6", "c": "7", "d": "8", "ans": "C", "exp": "x = 12-5 = 7"},
    {"q": "Average of 10,20,30,40,50 = ?", "a": "25", "b": "30", "c": "35", "d": "40", "ans": "B", "exp": "150/5 = 30"},
    {"q": "Train 60 km/h, distance in 2.5h = ?", "a": "120", "b": "140", "c": "150", "d": "180", "ans": "C", "exp": "60 × 2.5 = 150 km"},
    {"q": "20% of ₹800 = ?", "a": "₹120", "b": "₹140", "c": "₹160", "d": "₹180", "ans": "C", "exp": "800 × 0.2 = ₹160"},
    {"q": "Rectangle 10×5 cm area = ?", "a": "30", "b": "40", "c": "50", "d": "60", "ans": "C", "exp": "10×5 = 50 cm²"},
    {"q": "SI on ₹1000 at 5% for 2 years = ?", "a": "50", "b": "80", "c": "100", "d": "120", "ans": "C", "exp": "(1000×5×2)/100 = ₹100"},
    {"q": "Speed: 240 km in 4 hours = ?", "a": "50", "b": "60", "c": "70", "d": "80", "ans": "B", "exp": "240/4 = 60 km/h"},
    {"q": "√144 = ?", "a": "10", "b": "11", "c": "12", "d": "13", "ans": "C", "exp": "12×12 = 144"},
    {"q": "3x = 27, x = ?", "a": "3", "b": "6", "c": "9", "d": "12", "ans": "C", "exp": "27/3 = 9"},
    {"q": "25% of 400 = ?", "a": "50", "b": "75", "c": "100", "d": "125", "ans": "C", "exp": "400/4 = 100"},
    {"q": "Boys:Girls 3:2, total 50, boys = ?", "a": "20", "b": "25", "c": "30", "d": "35", "ans": "C", "exp": "3+2=5, 50/5=10, boys=30"},
    {"q": "8 workers 6 days, 12 workers = ?", "a": "4", "b": "5", "c": "6", "d": "8", "ans": "A", "exp": "8×6=48, 48/12=4 days"},
    {"q": "20% discount on ₹500 = ?", "a": "80", "b": "90", "c": "100", "d": "110", "ans": "C", "exp": "500×0.2 = ₹100"},
    {"q": "CI on ₹1000 at 10% for 2 years = ?", "a": "200", "b": "210", "c": "220", "d": "230", "ans": "B", "exp": "1000×1.1² = 1210, CI=210"},
    {"q": "a:b=2:3, b:c=4:5, a:c=?", "a": "8:15", "b": "6:15", "c": "8:12", "d": "6:12", "ans": "A", "exp": "2/3 × 4/5 = 8/15"},
    {"q": "Profit% if CP=200, SP=250", "a": "20%", "b": "25%", "c": "30%", "d": "35%", "ans": "B", "exp": "50/200×100=25%"},
    {"q": "Loss% if CP=500, SP=450", "a": "5%", "b": "10%", "c": "15%", "d": "20%", "ans": "B", "exp": "50/500×100=10%"},
    {"q": "SI on ₹500 at 8% for 3 years", "a": "100", "b": "120", "c": "140", "d": "160", "ans": "B", "exp": "(500×8×3)/100=₹120"},
    {"q": "Area of circle radius 7 cm", "a": "154", "b": "144", "c": "164", "d": "174", "ans": "A", "exp": "πr² = 22/7×49=154"},
    {"q": "Volume of cube side 5 cm", "a": "125", "b": "115", "c": "135", "d": "145", "ans": "A", "exp": "5³ = 125 cm³"},
    {"q": "15% of x = 45, x = ?", "a": "200", "b": "250", "c": "300", "d": "350", "ans": "C", "exp": "45×100/15=300"},
    {"q": "If 20% of a number is 40, number is?", "a": "180", "b": "200", "c": "220", "d": "240", "ans": "B", "exp": "40×100/20=200"},
    {"q": "A car covers 180 km in 3 hours. Speed?", "a": "50", "b": "55", "c": "60", "d": "65", "ans": "C", "exp": "180/3=60 km/h"},
    {"q": "What is 10% of 250?", "a": "20", "b": "25", "c": "30", "d": "35", "ans": "B", "exp": "250×0.1=25"},
    {"q": "If 2x + 3 = 11, x = ?", "a": "3", "b": "4", "c": "5", "d": "6", "ans": "B", "exp": "2x=8, x=4"},
    {"q": "Average of 5,10,15,20,25 = ?", "a": "12", "b": "13", "c": "14", "d": "15", "ans": "D", "exp": "75/5=15"},
    {"q": "Perimeter of square side 8 cm", "a": "28", "b": "30", "c": "32", "d": "34", "ans": "C", "exp": "4×8=32 cm"},
    {"q": "Area of square side 9 cm", "a": "72", "b": "81", "c": "90", "d": "99", "ans": "B", "exp": "9×9=81 cm²"},
    {"q": "Simple interest ₹2000 at 6% for 2 years", "a": "200", "b": "240", "c": "280", "d": "320", "ans": "B", "exp": "(2000×6×2)/100=₹240"},
    {"q": "Which is largest: 1/2, 2/3, 3/4, 4/5", "a": "1/2", "b": "2/3", "c": "3/4", "d": "4/5", "ans": "D", "exp": "0.5,0.67,0.75,0.8 → 4/5 largest"},
    {"q": "50% of 200 = ?", "a": "80", "b": "90", "c": "100", "d": "110", "ans": "C", "exp": "200/2=100"},
    {"q": "6 × 8 ÷ 2 = ?", "a": "20", "b": "24", "c": "28", "d": "32", "ans": "B", "exp": "48÷2=24"},
    {"q": "If a=2, b=3, a² + b² = ?", "a": "10", "b": "11", "c": "12", "d": "13", "ans": "D", "exp": "4+9=13"},
    {"q": "Which is prime: 21, 27, 29, 33", "a": "21", "b": "27", "c": "29", "d": "33", "ans": "C", "exp": "29 is prime"},
    {"q": "HCF of 12 and 18", "a": "4", "b": "5", "c": "6", "d": "7", "ans": "C", "exp": "6 divides both"},
    {"q": "LCM of 4 and 6", "a": "8", "b": "10", "c": "12", "d": "14", "ans": "C", "exp": "12 is multiple of both"},
    {"q": "0.75 as fraction", "a": "1/2", "b": "2/3", "c": "3/4", "d": "4/5", "ans": "C", "exp": "0.75=3/4"},
    {"q": "What is 2⁵?", "a": "16", "b": "24", "c": "32", "d": "40", "ans": "C", "exp": "2×2×2×2×2=32"},
    {"q": "√81 = ?", "a": "7", "b": "8", "c": "9", "d": "10", "ans": "C", "exp": "9×9=81"},
    {"q": "10% of 500 + 20% of 200 = ?", "a": "80", "b": "90", "c": "100", "d": "110", "ans": "B", "exp": "50+40=90"},
    {"q": "If price is ₹120 and tax is 10%, total?", "a": "126", "b": "130", "c": "132", "d": "135", "ans": "C", "exp": "120+12=₹132"},
    {"q": "Discount of 15% on ₹200", "a": "20", "b": "25", "c": "30", "d": "35", "ans": "C", "exp": "200×0.15=₹30"},
    {"q": "Profit if CP=300, SP=360", "a": "50", "b": "60", "c": "70", "d": "80", "ans": "B", "exp": "360-300=60"},
    {"q": "Ratio of 2 to 5 in percentage", "a": "20%", "b": "30%", "c": "40%", "d": "50%", "ans": "C", "exp": "2/5=0.4=40%"},
    {"q": "What is 30% of 300?", "a": "60", "b": "70", "c": "80", "d": "90", "ans": "D", "exp": "300×0.3=90"},
    {"q": "If a:b = 2:3 and b:c = 6:5, find a:c", "a": "4:5", "b": "5:4", "c": "3:4", "d": "4:3", "ans": "A", "exp": "a:c = 2:5 → 4:5"},
]

# Logical Reasoning (50 questions)
lr_questions = [
    {"q": "Series: 1,4,9,16,?", "a": "20", "b": "24", "c": "25", "d": "30", "ans": "C", "exp": "Squares: 1²,2²,3²,4²,5²=25"},
    {"q": "CAT coded as 3120, DOG = ?", "a": "4157", "b": "4156", "c": "4167", "d": "5147", "ans": "A", "exp": "C=3,A=1,T=20 → D=4,O=15,G=7=4157"},
    {"q": "Odd one: Apple, Mango, Orange, Carrot", "a": "Apple", "b": "Mango", "c": "Orange", "d": "Carrot", "ans": "D", "exp": "Carrot is vegetable"},
    {"q": "2+3=10, 4+5=36, 6+7=?", "a": "64", "b": "78", "c": "84", "d": "96", "ans": "B", "exp": "(2+3)×2=10, (4+5)×4=36, (6+7)×6=78"},
    {"q": "Missing: 2,6,12,20,?,42", "a": "28", "b": "30", "c": "32", "d": "36", "ans": "B", "exp": "+4,+6,+8,+10,+12=30"},
    {"q": "NORTH → OPSUI, SOUTH → ?", "a": "TPVUI", "b": "TPVUJ", "c": "TPVUK", "d": "TPVUL", "ans": "A", "exp": "Each letter+1"},
    {"q": "AZ, BY, CX, ?", "a": "DW", "b": "WD", "c": "DX", "d": "XD", "ans": "A", "exp": "A→Z, B→Y, C→X, D→W"},
    {"q": "Smallest: 0.5,0.25,0.75,0.125", "a": "0.5", "b": "0.25", "c": "0.75", "d": "0.125", "ans": "D", "exp": "0.125=1/8 smallest"},
    {"q": "Monday=1, Sunday=?", "a": "6", "b": "7", "c": "0", "d": "1", "ans": "B", "exp": "Sunday=7"},
    {"q": "3,6,11,18,?", "a": "25", "b": "27", "c": "29", "d": "31", "ans": "B", "exp": "+3,+5,+7,+9=27"},
    {"q": "RED=27, BLUE=?", "a": "40", "b": "42", "c": "44", "d": "46", "ans": "A", "exp": "R=18,E=5,D=4 sum=27; B=2,L=12,U=21,E=5=40"},
    {"q": "If pen=book, book=copy, copy=paper, write with?", "a": "Pen", "b": "Book", "c": "Copy", "d": "Paper", "ans": "D", "exp": "Pen=book, book=copy, copy=paper"},
    {"q": "5,7,11,17,25,?", "a": "35", "b": "37", "c": "39", "d": "41", "ans": "A", "exp": "+2,+4,+6,+8,+10=35"},
    {"q": "B2, D4, F6, H8, ?", "a": "J10", "b": "J9", "c": "I10", "d": "I9", "ans": "A", "exp": "B=2,D=4,F=6,H=8,J=10"},
    {"q": "Which is different? 11,13,17,19,23,25", "a": "11", "b": "17", "c": "23", "d": "25", "ans": "D", "exp": "25 is not prime"},
    {"q": "A, D, I, P, ?", "a": "T", "b": "U", "c": "V", "d": "Y", "ans": "D", "exp": "A+3=D, D+5=I, I+7=P, P+9=Y"},
    {"q": "If 1=ONE, 2=TWO, 3=THREE, 4=?", "a": "FOUR", "b": "FIVE", "c": "SIX", "d": "SEVEN", "ans": "A", "exp": "Spelling of number"},
    {"q": "Find next: Z, Y, X, W, ?", "a": "U", "b": "V", "c": "T", "d": "S", "ans": "B", "exp": "Alphabet reverse: V"},
    {"q": "If 8×5=40, 7×6=42, 6×7=42, 5×8=?", "a": "35", "b": "40", "c": "42", "d": "45", "ans": "B", "exp": "5×8=40"},
    {"q": "Statement: All roses are flowers. Some flowers are red.", "a": "Some roses are red", "b": "All roses are red", "c": "No roses are red", "d": "Cannot be determined", "ans": "D", "exp": "No definite conclusion"},
    {"q": "Which is the odd one: 2, 5, 10, 17, 26, 37, 50", "a": "2", "b": "10", "c": "26", "d": "50", "ans": "D", "exp": "Pattern: n²+1, 50 doesn't fit"},
    {"q": "If 3+4=21, 5+6=55, 7+8=?", "a": "77", "b": "89", "c": "91", "d": "99", "ans": "C", "exp": "3×4+3×4=12+9=21, 5×6+5×6=30+25=55"},
    {"q": "Find the next: 3, 8, 15, 24, ?", "a": "33", "b": "35", "c": "37", "d": "39", "ans": "A", "exp": "+5,+7,+9,+11=33"},
    {"q": "What comes next: 2, 3, 5, 7, 11, ?", "a": "13", "b": "15", "c": "17", "d": "19", "ans": "A", "exp": "Prime numbers: 13"},
    {"q": "If SOUTH is coded as TPVUI, NORTH is?", "a": "OPSUI", "b": "OPSUJ", "c": "OPSUK", "d": "OPSUL", "ans": "A", "exp": "Each letter+1: NORTH→OPSUI"},
    {"q": "What is the angle between hour and minute at 3:00?", "a": "60°", "b": "75°", "c": "90°", "d": "120°", "ans": "C", "exp": "3:00 = 90°"},
    {"q": "If 6 men can do work in 12 days, 8 men can do in?", "a": "8", "b": "9", "c": "10", "d": "11", "ans": "B", "exp": "6×12=72, 72/8=9 days"},
    {"q": "What is the total of 1+2+3+...+10?", "a": "45", "b": "50", "c": "55", "d": "60", "ans": "C", "exp": "10×11/2 = 55"},
    {"q": "Which is the smallest: 1/3, 1/4, 1/5, 1/6", "a": "1/3", "b": "1/4", "c": "1/5", "d": "1/6", "ans": "D", "exp": "1/6 is smallest"},
    {"q": "What is the value of 5! (5 factorial)?", "a": "60", "b": "80", "c": "100", "d": "120", "ans": "D", "exp": "5×4×3×2×1=120"},
    {"q": "If a train runs 180 km in 2 hours, speed in m/s?", "a": "25", "b": "30", "c": "35", "d": "40", "ans": "A", "exp": "180/2=90 km/h=25 m/s"},
    {"q": "Find the odd one: 8, 27, 64, 125, 216, 343, 512, 729", "a": "8", "b": "125", "c": "512", "d": "729", "ans": "No odd one", "exp": "All are cubes"},
    {"q": "If 2^3 = 8, 3^3 = 27, 4^3 = ?", "a": "36", "b": "48", "c": "64", "d": "72", "ans": "C", "exp": "4³ = 64"},
    {"q": "What is 7 × 8?", "a": "48", "b": "54", "c": "56", "d": "62", "ans": "C", "exp": "7×8=56"},
    {"q": "If a triangle has sides 3,4,5, what is the area?", "a": "6", "b": "8", "c": "10", "d": "12", "ans": "A", "exp": "Right triangle: 1/2×3×4=6"},
    {"q": "What is the sum of first 10 odd numbers?", "a": "50", "b": "80", "c": "90", "d": "100", "ans": "D", "exp": "n²=10²=100"},
    {"q": "If price is ₹500, 10% discount = ?", "a": "40", "b": "50", "c": "60", "d": "70", "ans": "B", "exp": "500×0.1=50"},
    {"q": "What is 6²?", "a": "30", "b": "36", "c": "42", "d": "48", "ans": "B", "exp": "6×6=36"},
    {"q": "If x:y = 4:5 and y:z = 10:7, find x:z", "a": "8:7", "b": "7:8", "c": "4:7", "d": "5:7", "ans": "A", "exp": "x:z = 4×10:5×7 = 40:35 = 8:7"},
    {"q": "Which number is missing: 5, 11, 23, 47, ?", "a": "85", "b": "90", "c": "95", "d": "100", "ans": "C", "exp": "×2+1: 47×2+1=95"},
]

# Add all aptitude questions
for q in qa_questions + lr_questions:
    aptitude_questions.append(q)
    MockTestQuestion.objects.create(
        mock_test=aptitude_test,
        question_text=q["q"],
        option_a=q["a"],
        option_b=q["b"],
        option_c=q["c"],
        option_d=q["d"],
        correct_answer=q["ans"],
        explanation=q["exp"],
        marks=1
    )

print(f"✅ Added {len(aptitude_questions)} questions to Aptitude Master Test")

# ============================================================
# 2. CODING MCQ TEST - 85 QUESTIONS (Multiple Languages)
# ============================================================
print("\n💻 Creating Coding MCQ Master Test...")

coding_test = MockTest.objects.create(
    title="Coding MCQ Master Test",
    category="coding",
    time_limit=90,
    passing_score=50
)

coding_questions = []

# Python (20 questions)
python_qs = [
    {"q": "What is the output of print(2**3)?", "a": "6", "b": "8", "c": "9", "d": "5", "ans": "B", "exp": "2**3 = 8"},
    {"q": "Which keyword defines a function in Python?", "a": "func", "b": "define", "c": "def", "d": "function", "ans": "C", "exp": "'def' is used"},
    {"q": "How to create a list in Python?", "a": "(1,2,3)", "b": "[1,2,3]", "c": "{1,2,3}", "d": "<1,2,3>", "ans": "B", "exp": "[] creates list"},
    {"q": "Which is mutable in Python?", "a": "tuple", "b": "string", "c": "list", "d": "int", "ans": "C", "exp": "List is mutable"},
    {"q": "What is the output of print(type([]))?", "a": "tuple", "b": "list", "c": "dict", "d": "set", "ans": "B", "exp": "[] is list"},
    {"q": "What is the output of 'Hello'[1]?", "a": "H", "b": "e", "c": "l", "d": "o", "ans": "B", "exp": "Index 1 = e"},
    {"q": "Which operator concatenates strings?", "a": "*", "b": "&", "c": "+", "d": "#", "ans": "C", "exp": "+ concatenates"},
    {"q": "Python file extension?", "a": ".pyth", "b": ".pt", "c": ".py", "d": ".p", "ans": "C", "exp": ".py extension"},
    {"q": "Which function prints output?", "a": "input()", "b": "output()", "c": "print()", "d": "display()", "ans": "C", "exp": "print() displays"},
    {"q": "bool(0) returns?", "a": "True", "b": "False", "c": "1", "d": "Error", "ans": "B", "exp": "0 is False"},
    {"q": "What is 10 // 3?", "a": "3.33", "b": "3", "c": "4", "d": "3.0", "ans": "B", "exp": "Floor division"},
    {"q": "What is the output of len('hello')?", "a": "4", "b": "5", "c": "6", "d": "3", "ans": "B", "exp": "5 characters"},
    {"q": "Which loop executes at least once?", "a": "for", "b": "while", "c": "do-while", "d": "None", "ans": "C", "exp": "do-while executes once"},
    {"q": "What is OOP?", "a": "Object Oriented Programming", "b": "Output Oriented", "c": "Operation Oriented", "d": "Object Optional", "ans": "A", "exp": "OOP definition"},
    {"q": "Which is a Python framework?", "a": "React", "b": "Django", "c": "Angular", "d": "Vue", "ans": "B", "exp": "Django is Python"},
    {"q": "What is the output of print(5 % 2)?", "a": "1", "b": "2", "c": "0", "d": "2.5", "ans": "A", "exp": "5 ÷ 2 remainder 1"},
    {"q": "How to take user input?", "a": "scan()", "b": "read()", "c": "input()", "d": "get()", "ans": "C", "exp": "input() function"},
    {"q": "What is None in Python?", "a": "0", "b": "null", "c": "Nothing", "d": "Empty string", "ans": "B", "exp": "None means null"},
    {"q": "Which is used for comments?", "a": "//", "b": "/*", "c": "#", "d": "<!--", "ans": "C", "exp": "# for comments"},
    {"q": "What is the output of print(2+3*4)?", "a": "20", "b": "14", "c": "24", "d": "18", "ans": "B", "exp": "3*4=12, 12+2=14"},
]

# Java (15 questions)
java_qs = [
    {"q": "Entry point of Java program?", "a": "main()", "b": "Main()", "c": "public static void main(String[] args)", "d": "start()", "ans": "C", "exp": "main method signature"},
    {"q": "Which keyword creates a class?", "a": "class", "b": "Class", "c": "struct", "d": "interface", "ans": "A", "exp": "'class' keyword"},
    {"q": "Size of int in Java?", "a": "2 bytes", "b": "4 bytes", "c": "8 bytes", "d": "1 byte", "ans": "B", "exp": "int is 4 bytes"},
    {"q": "Keyword for inheritance?", "a": "extend", "b": "extends", "c": "implements", "d": "inherits", "ans": "B", "exp": "'extends' keyword"},
    {"q": "What is JVM?", "a": "Java Virtual Machine", "b": "Java Variable Machine", "c": "Java Version Machine", "d": "Java Very Machine", "ans": "A", "exp": "JVM definition"},
    {"q": "Which is not a keyword?", "a": "static", "b": "void", "c": "main", "d": "class", "ans": "C", "exp": "main is method name"},
    {"q": "Default value of boolean?", "a": "true", "b": "false", "c": "0", "d": "null", "ans": "B", "exp": "boolean defaults false"},
    {"q": "Single-line comment symbol?", "a": "/*", "b": "//", "c": "#", "d": "<!--", "ans": "B", "exp": "// for comments"},
    {"q": "Output of 5 + 3 + 'Hello'?", "a": "53Hello", "b": "8Hello", "c": "Hello8", "d": "Hello53", "ans": "B", "exp": "5+3=8 then Hello"},
    {"q": "Which package is auto-imported?", "a": "java.io", "b": "java.util", "c": "java.lang", "d": "java.awt", "ans": "C", "exp": "java.lang automatic"},
    {"q": "What is polymorphism?", "a": "Many forms", "b": "Single form", "c": "No form", "d": "Fixed form", "ans": "A", "exp": "Poly=many, morphism=forms"},
    {"q": "What is inheritance?", "a": "Reusing code", "b": "Hiding data", "c": "Creating objects", "d": "Destroying objects", "ans": "A", "exp": "Inheritance reuses parent code"},
    {"q": "Which is a Java collection?", "a": "Array", "b": "ArrayList", "c": "String", "d": "Integer", "ans": "B", "exp": "ArrayList is collection"},
    {"q": "What is JDK?", "a": "Java Development Kit", "b": "Java Debug Kit", "c": "Java Deployment Kit", "d": "Java Design Kit", "ans": "A", "exp": "JDK = Java Development Kit"},
    {"q": "What is JRE?", "a": "Java Runtime Environment", "b": "Java Run Environment", "c": "Java Runtime Engine", "d": "Java Read Environment", "ans": "A", "exp": "JRE = Java Runtime Environment"},
]

# C/C++ (15 questions)
cpp_qs = [
    {"q": "Size of int in C (32-bit)?", "a": "2 bytes", "b": "4 bytes", "c": "6 bytes", "d": "8 bytes", "ans": "B", "exp": "int is 4 bytes"},
    {"q": "Header for printf()?", "a": "iostream", "b": "stdio.h", "c": "conio.h", "d": "math.h", "ans": "B", "exp": "stdio.h contains printf"},
    {"q": "How to declare a pointer?", "a": "int *ptr", "b": "int &ptr", "c": "int ptr*", "d": "*int ptr", "ans": "A", "exp": "* is pointer"},
    {"q": "Address-of operator?", "a": "*", "b": "&", "c": "->", "d": "::", "ans": "B", "exp": "& gives address"},
    {"q": "Output of printf('%d', 5/2)?", "a": "2.5", "b": "2", "c": "3", "d": "2.0", "ans": "B", "exp": "Integer division"},
    {"q": "C++ inheritance keyword?", "a": "extends", "b": "inherits", "c": ":", "d": "implements", "ans": "C", "exp": "Colon : for inheritance"},
    {"q": "Difference between struct and class?", "a": "No difference", "b": "struct public default", "c": "class public default", "d": "struct has no functions", "ans": "B", "exp": "struct members public by default"},
    {"q": "C++ memory allocation?", "a": "malloc()", "b": "new", "c": "alloc()", "d": "create()", "ans": "B", "exp": "'new' for dynamic memory"},
    {"q": "What is the output of sizeof(char) in C?", "a": "2", "b": "4", "c": "1", "d": "8", "ans": "C", "exp": "char is 1 byte"},
    {"q": "Which is a loop in C?", "a": "for", "b": "if", "c": "switch", "d": "break", "ans": "A", "exp": "for is loop"},
    {"q": "What is an array?", "a": "Different types", "b": "Same type collection", "c": "No type", "d": "Single element", "ans": "B", "exp": "Array stores same type"},
    {"q": "Which function copies string?", "a": "strcopy", "b": "strcpy", "c": "stringcpy", "d": "copy", "ans": "B", "exp": "strcpy copies string"},
    {"q": "What is NULL pointer?", "a": "Points to 0", "b": "Points to nothing", "c": "Error", "d": "Uninitialized", "ans": "A", "exp": "NULL points to address 0"},
    {"q": "What is stack?", "a": "LIFO", "b": "FIFO", "c": "Random", "d": "Ordered", "ans": "A", "exp": "Stack = Last In First Out"},
    {"q": "What is queue?", "a": "LIFO", "b": "FIFO", "c": "Random", "d": "Ordered", "ans": "B", "exp": "Queue = First In First Out"},
]

# DSA (20 questions)
dsa_qs = [
    {"q": "Time complexity of binary search?", "a": "O(n)", "b": "O(log n)", "c": "O(n²)", "d": "O(2ⁿ)", "ans": "B", "exp": "Binary search O(log n)"},
    {"q": "Which data structure uses LIFO?", "a": "Queue", "b": "Stack", "c": "List", "d": "Array", "ans": "B", "exp": "Stack = LIFO"},
    {"q": "Which uses FIFO?", "a": "Stack", "b": "Queue", "c": "Tree", "d": "Graph", "ans": "B", "exp": "Queue = FIFO"},
    {"q": "Worst case of bubble sort?", "a": "O(n)", "b": "O(log n)", "c": "O(n²)", "d": "O(n log n)", "ans": "C", "exp": "Bubble sort O(n²)"},
    {"q": "Best average case sorting?", "a": "Bubble", "b": "Selection", "c": "Quick", "d": "Insertion", "ans": "C", "exp": "Quick sort O(n log n)"},
    {"q": "What is a binary tree?", "a": "1 child", "b": "2 children max", "c": "3 children", "d": "Random", "ans": "B", "exp": "Binary tree has at most 2 children"},
    {"q": "Hash table used for?", "a": "Sorting", "b": "Fast lookup", "c": "Recursion", "d": "Memory", "ans": "B", "exp": "Hash tables give O(1) lookup"},
    {"q": "What is recursion?", "a": "Function calls itself", "b": "Loop", "c": "Condition", "d": "Variable", "ans": "A", "exp": "Recursion = function calls itself"},
    {"q": "DFS uses which data structure?", "a": "Queue", "b": "Stack", "c": "List", "d": "Array", "ans": "B", "exp": "DFS uses Stack"},
    {"q": "BFS uses which data structure?", "a": "Stack", "b": "Queue", "c": "List", "d": "Tree", "ans": "B", "exp": "BFS uses Queue"},
    {"q": "Space complexity of merge sort?", "a": "O(1)", "b": "O(log n)", "c": "O(n)", "d": "O(n²)", "ans": "C", "exp": "Merge sort O(n) space"},
    {"q": "Shortest path algorithm?", "a": "Dijkstra", "b": "Kruskal", "c": "Prim", "d": "Bellman", "ans": "A", "exp": "Dijkstra's algorithm"},
    {"q": "What is a linked list?", "a": "Contiguous memory", "b": "Non-contiguous", "c": "Fixed size", "d": "Random access", "ans": "B", "exp": "Linked list non-contiguous"},
    {"q": "What is dynamic programming?", "a": "Divide and conquer", "b": "Memoization", "c": "Greedy", "d": "Brute force", "ans": "B", "exp": "DP uses memoization"},
    {"q": "What is the complexity of binary search tree search?", "a": "O(n)", "b": "O(log n)", "c": "O(n log n)", "d": "O(n²)", "ans": "B", "exp": "BST search O(log n) average"},
    {"q": "What is a graph?", "a": "Nodes and edges", "b": "Tree", "c": "List", "d": "Array", "ans": "A", "exp": "Graph has nodes and edges"},
    {"q": "What is a tree?", "a": "Cyclic graph", "b": "Acyclic graph", "c": "List", "d": "Queue", "ans": "B", "exp": "Tree is acyclic graph"},
    {"q": "What is an algorithm?", "a": "Set of steps", "b": "Program", "c": "Code", "d": "Function", "ans": "A", "exp": "Algorithm is step-by-step"},
    {"q": "What is a stack overflow?", "a": "Memory error", "b": "Compile error", "c": "Runtime error", "d": "Logic error", "ans": "A", "exp": "Stack overflow is memory error"},
    {"q": "What is a hash map?", "a": "Key-value store", "b": "List", "c": "Queue", "d": "Stack", "ans": "A", "exp": "HashMap stores key-value pairs"},
]

# Web/JavaScript (15 questions)
web_qs = [
    {"q": "What does HTML stand for?", "a": "Hyper Text Markup Language", "b": "High Tech Modern Language", "c": "Hyper Transfer Markup", "d": "Home Tool Markup", "ans": "A", "exp": "HTML definition"},
    {"q": "Tag for heading in HTML?", "a": "<head>", "b": "<h1>", "c": "<title>", "d": "<div>", "ans": "B", "exp": "<h1> to <h6> for headings"},
    {"q": "What does CSS stand for?", "a": "Creative Style Sheets", "b": "Computer Style Sheets", "c": "Cascading Style Sheets", "d": "Colorful Style Sheets", "ans": "C", "exp": "CSS definition"},
    {"q": "JavaScript keyword for variable?", "a": "var", "b": "let", "c": "const", "d": "All", "ans": "D", "exp": "var, let, const all work"},
    {"q": "What is React?", "a": "JavaScript framework", "b": "Python library", "c": "Java framework", "d": "C++ library", "ans": "A", "exp": "React is JS library"},
    {"q": "What is Node.js?", "a": "Frontend framework", "b": "Backend JS runtime", "c": "Database", "d": "CSS preprocessor", "ans": "B", "exp": "Node.js runs JS on server"},
    {"q": "What is SQL used for?", "a": "Styling", "b": "Database queries", "c": "Server logic", "d": "Animation", "ans": "B", "exp": "SQL for databases"},
    {"q": "What does API stand for?", "a": "Application Program Interface", "b": "Application Programming Interface", "c": "Application Protocol Interface", "d": "Application Process Interface", "ans": "B", "exp": "API definition"},
    {"q": "What is Git used for?", "a": "Version control", "b": "Styling", "c": "Database", "d": "Testing", "ans": "A", "exp": "Git for version control"},
    {"q": "What is a REST API?", "a": "Architectural style", "b": "Database", "c": "Language", "d": "Framework", "ans": "A", "exp": "REST is architecture"},
    {"q": "What is JSON?", "a": "Data format", "b": "Database", "c": "Language", "d": "Framework", "ans": "A", "exp": "JSON = JavaScript Object Notation"},
    {"q": "What is AJAX?", "a": "Async requests", "b": "Database", "c": "Language", "d": "Framework", "ans": "A", "exp": "AJAX for async web requests"},
    {"q": "Which is a database query language?", "a": "Python", "b": "Java", "c": "SQL", "d": "HTML", "ans": "C", "exp": "SQL queries databases"},
    {"q": "What is MongoDB?", "a": "NoSQL database", "b": "SQL database", "c": "Language", "d": "Framework", "ans": "A", "exp": "MongoDB is NoSQL"},
    {"q": "What is Docker?", "a": "Containerization", "b": "Database", "c": "Language", "d": "Framework", "ans": "A", "exp": "Docker for containers"},
]

# Add all coding questions
all_coding_qs = python_qs + java_qs + cpp_qs + dsa_qs + web_qs
for q in all_coding_qs:
    coding_questions.append(q)
    MockTestQuestion.objects.create(
        mock_test=coding_test,
        question_text=q["q"],
        option_a=q["a"],
        option_b=q["b"],
        option_c=q["c"],
        option_d=q["d"],
        correct_answer=q["ans"],
        explanation=q["exp"],
        marks=1
    )

print(f"✅ Added {len(all_coding_qs)} questions to Coding MCQ Master Test")
print(f"   - Python: {len(python_qs)}")
print(f"   - Java: {len(java_qs)}")
print(f"   - C/C++: {len(cpp_qs)}")
print(f"   - DSA: {len(dsa_qs)}")
print(f"   - Web/JS: {len(web_qs)}")

# ============================================================
# 3. VERBAL ABILITY TEST - 100 QUESTIONS
# ============================================================
print("\n🗣️ Creating Verbal Ability Master Test...")

verbal_test = MockTest.objects.create(
    title="Verbal Ability Master Test",
    category="verbal",
    time_limit=60,
    passing_score=50
)

verbal_questions = []

# Synonyms (25 questions)
synonyms = [
    {"q": "Synonym of BEAUTIFUL", "a": "Ugly", "b": "Pretty", "c": "Dark", "d": "Bright", "ans": "B", "exp": "Pretty means same"},
    {"q": "Synonym of HAPPY", "a": "Sad", "b": "Joyful", "c": "Angry", "d": "Tired", "ans": "B", "exp": "Joyful means same"},
    {"q": "Synonym of BIG", "a": "Small", "b": "Large", "c": "Tiny", "d": "Little", "ans": "B", "exp": "Large means same"},
    {"q": "Synonym of QUICK", "a": "Slow", "b": "Fast", "c": "Lazy", "d": "Dull", "ans": "B", "exp": "Fast means same"},
    {"q": "Synonym of SMART", "a": "Dumb", "b": "Intelligent", "c": "Stupid", "d": "Foolish", "ans": "B", "exp": "Intelligent means same"},
    {"q": "Synonym of ANGRY", "a": "Calm", "b": "Furious", "c": "Peaceful", "d": "Happy", "ans": "B", "exp": "Furious means same"},
    {"q": "Synonym of DIFFICULT", "a": "Easy", "b": "Hard", "c": "Simple", "d": "Basic", "ans": "B", "exp": "Hard means same"},
    {"q": "Synonym of START", "a": "End", "b": "Begin", "c": "Finish", "d": "Stop", "ans": "B", "exp": "Begin means same"},
    {"q": "Synonym of HELP", "a": "Ignore", "b": "Assist", "c": "Neglect", "d": "Avoid", "ans": "B", "exp": "Assist means same"},
    {"q": "Synonym of FRIEND", "a": "Enemy", "b": "Buddy", "c": "Foe", "d": "Rival", "ans": "B", "exp": "Buddy means same"},
    {"q": "Synonym of RICH", "a": "Poor", "b": "Wealthy", "c": "Needy", "d": "Broke", "ans": "B", "exp": "Wealthy means same"},
    {"q": "Synonym of FAST", "a": "Slow", "b": "Rapid", "c": "Lazy", "d": "Dull", "ans": "B", "exp": "Rapid means same"},
    {"q": "Synonym of STRONG", "a": "Weak", "b": "Powerful", "c": "Frail", "d": "Soft", "ans": "B", "exp": "Powerful means same"},
    {"q": "Synonym of SMALL", "a": "Large", "b": "Tiny", "c": "Huge", "d": "Big", "ans": "B", "exp": "Tiny means same"},
    {"q": "Synonym of CLEAR", "a": "Unclear", "b": "Obvious", "c": "Vague", "d": "Uncertain", "ans": "B", "exp": "Obvious means same"},
    {"q": "Synonym of BRAVE", "a": "Cowardly", "b": "Courageous", "c": "Timid", "d": "Fearful", "ans": "B", "exp": "Courageous means same"},
    {"q": "Synonym of CALM", "a": "Agitated", "b": "Peaceful", "c": "Angry", "d": "Upset", "ans": "B", "exp": "Peaceful means same"},
    {"q": "Synonym of FAMOUS", "a": "Unknown", "b": "Renowned", "c": "Obscure", "d": "Unfamiliar", "ans": "B", "exp": "Renowned means same"},
    {"q": "Synonym of CHEAP", "a": "Expensive", "b": "Inexpensive", "c": "Costly", "d": "Pricey", "ans": "B", "exp": "Inexpensive means same"},
    {"q": "Synonym of LAZY", "a": "Active", "b": "Idle", "c": "Energetic", "d": "Industrious", "ans": "B", "exp": "Idle means same"},
    {"q": "Synonym of QUIET", "a": "Noisy", "b": "Silent", "c": "Loud", "d": "Boisterous", "ans": "B", "exp": "Silent means same"},
    {"q": "Synonym of OLD", "a": "New", "b": "Ancient", "c": "Young", "d": "Fresh", "ans": "B", "exp": "Ancient means same"},
    {"q": "Synonym of NEW", "a": "Old", "b": "Ancient", "c": "Modern", "d": "Aged", "ans": "C", "exp": "Modern means same"},
    {"q": "Synonym of SAD", "a": "Happy", "b": "Joyful", "c": "Unhappy", "d": "Cheerful", "ans": "C", "exp": "Unhappy means same"},
    {"q": "Synonym of TRUE", "a": "False", "b": "Correct", "c": "Wrong", "d": "Incorrect", "ans": "B", "exp": "Correct means same"},
]

# Antonyms (25 questions)
antonyms = [
    {"q": "Antonym of WET", "a": "Moist", "b": "Dry", "c": "Damp", "d": "Humid", "ans": "B", "exp": "Dry is opposite"},
    {"q": "Antonym of DARK", "a": "Black", "b": "Light", "c": "Night", "d": "Shadow", "ans": "B", "exp": "Light is opposite"},
    {"q": "Antonym of HOT", "a": "Warm", "b": "Cold", "c": "Heat", "d": "Temperature", "ans": "B", "exp": "Cold is opposite"},
    {"q": "Antonym of RICH", "a": "Wealthy", "b": "Poor", "c": "Affluent", "d": "Prosperous", "ans": "B", "exp": "Poor is opposite"},
    {"q": "Antonym of LOVE", "a": "Affection", "b": "Hate", "c": "Care", "d": "Like", "ans": "B", "exp": "Hate is opposite"},
    {"q": "Antonym of WIN", "a": "Victory", "b": "Lose", "c": "Success", "d": "Triumph", "ans": "B", "exp": "Lose is opposite"},
    {"q": "Antonym of FULL", "a": "Complete", "b": "Empty", "c": "Total", "d": "Whole", "ans": "B", "exp": "Empty is opposite"},
    {"q": "Antonym of FAST", "a": "Quick", "b": "Slow", "c": "Rapid", "d": "Swift", "ans": "B", "exp": "Slow is opposite"},
    {"q": "Antonym of NOISE", "a": "Sound", "b": "Silence", "c": "Volume", "d": "Music", "ans": "B", "exp": "Silence is opposite"},
    {"q": "Antonym of FRESH", "a": "New", "b": "Stale", "c": "Clean", "d": "Recent", "ans": "B", "exp": "Stale is opposite"},
    {"q": "Antonym of HARD", "a": "Difficult", "b": "Soft", "c": "Tough", "d": "Rigid", "ans": "B", "exp": "Soft is opposite"},
    {"q": "Antonym of HEAVY", "a": "Light", "b": "Massive", "c": "Weighty", "d": "Huge", "ans": "A", "exp": "Light is opposite"},
    {"q": "Antonym of CHEAP", "a": "Inexpensive", "b": "Expensive", "c": "Low-cost", "d": "Affordable", "ans": "B", "exp": "Expensive is opposite"},
    {"q": "Antonym of STRONG", "a": "Powerful", "b": "Weak", "c": "Mighty", "d": "Sturdy", "ans": "B", "exp": "Weak is opposite"},
    {"q": "Antonym of BRAVE", "a": "Courageous", "b": "Cowardly", "c": "Fearless", "d": "Valiant", "ans": "B", "exp": "Cowardly is opposite"},
    {"q": "Antonym of CLEVER", "a": "Smart", "b": "Stupid", "c": "Intelligent", "d": "Wise", "ans": "B", "exp": "Stupid is opposite"},
    {"q": "Antonym of KIND", "a": "Mean", "b": "Nice", "c": "Good", "d": "Gentle", "ans": "A", "exp": "Mean is opposite"},
    {"q": "Antonym of HAPPY", "a": "Joyful", "b": "Sad", "c": "Glad", "d": "Delighted", "ans": "B", "exp": "Sad is opposite"},
    {"q": "Antonym of GOOD", "a": "Excellent", "b": "Bad", "c": "Great", "d": "Wonderful", "ans": "B", "exp": "Bad is opposite"},
    {"q": "Antonym of HIGH", "a": "Low", "b": "Tall", "c": "Elevated", "d": "Lofty", "ans": "A", "exp": "Low is opposite"},
    {"q": "Antonym of WIDE", "a": "Broad", "b": "Narrow", "c": "Large", "d": "Spacious", "ans": "B", "exp": "Narrow is opposite"},
    {"q": "Antonym of DEEP", "a": "Shallow", "b": "Profound", "c": "Bottomless", "d": "Abyssal", "ans": "A", "exp": "Shallow is opposite"},
    {"q": "Antonym of YOUNG", "a": "Youthful", "b": "Old", "c": "Juvenile", "d": "New", "ans": "B", "exp": "Old is opposite"},
    {"q": "Antonym of OPEN", "a": "Shut", "b": "Ajar", "c": "Unlocked", "d": "Available", "ans": "A", "exp": "Shut is opposite"},
    {"q": "Antonym of START", "a": "Begin", "b": "End", "c": "Launch", "d": "Open", "ans": "B", "exp": "End is opposite"},
]

# Fill in the blanks (20 questions)
fill_blanks = [
    {"q": "She ___ to school every day.", "a": "go", "b": "goes", "c": "going", "d": "went", "ans": "B", "exp": "She goes (third person singular)"},
    {"q": "He ___ to the market yesterday.", "a": "go", "b": "goes", "c": "went", "d": "going", "ans": "C", "exp": "Past tense: went"},
    {"q": "I ___ a student.", "a": "is", "b": "are", "c": "am", "d": "be", "ans": "C", "exp": "I am a student"},
    {"q": "They ___ playing football.", "a": "is", "b": "am", "c": "are", "d": "be", "ans": "C", "exp": "They are playing"},
    {"q": "___ you like coffee?", "a": "Does", "b": "Do", "c": "Is", "d": "Are", "ans": "B", "exp": "Do you like coffee?"},
    {"q": "She doesn't ___ to work.", "a": "want", "b": "wants", "c": "wanting", "d": "wanted", "ans": "A", "exp": "After doesn't, use base form"},
    {"q": "We ___ waiting for you.", "a": "is", "b": "am", "c": "are", "d": "be", "ans": "C", "exp": "We are waiting"},
    {"q": "This is ___ apple.", "a": "a", "b": "an", "c": "the", "d": "none", "ans": "B", "exp": "'an' before vowel sound"},
    {"q": "He is ___ best student.", "a": "a", "b": "an", "c": "the", "d": "none", "ans": "C", "exp": "'the' for superlative"},
    {"q": "___ sun rises in the east.", "a": "A", "b": "An", "c": "The", "d": "None", "ans": "C", "exp": "'The' for unique things"},
    {"q": "I have ___ apple.", "a": "a", "b": "an", "c": "the", "d": "none", "ans": "B", "exp": "'an' before vowel"},
    {"q": "She is ___ engineer.", "a": "a", "b": "an", "c": "the", "d": "none", "ans": "B", "exp": "'an' before vowel sound"},
    {"q": "Let's go to ___ park.", "a": "a", "b": "an", "c": "the", "d": "none", "ans": "A", "exp": "a before consonant"},
    {"q": "I need ___ umbrella.", "a": "a", "b": "an", "c": "the", "d": "none", "ans": "B", "exp": "'an' before vowel"},
    {"q": "He is ___ honest man.", "a": "a", "b": "an", "c": "the", "d": "none", "ans": "B", "exp": "'an' before silent h"},
    {"q": "This is ___ useful tool.", "a": "a", "b": "an", "c": "the", "d": "none", "ans": "A", "exp": "yoo sound uses a"},
    {"q": "___ sun is shining.", "a": "A", "b": "An", "c": "The", "d": "None", "ans": "C", "exp": "The for unique"},
    {"q": "She is ___ best.", "a": "a", "b": "an", "c": "the", "d": "none", "ans": "C", "exp": "The for superlative"},
    {"q": "I want to become ___ doctor.", "a": "a", "b": "an", "c": "the", "d": "none", "ans": "A", "exp": "a before consonant"},
    {"q": "He has ___ one rupee note.", "a": "a", "b": "an", "c": "the", "d": "none", "ans": "A", "exp": "one starts with w sound"},
]

# Spot the error (15 questions)
errors = [
    {"q": "Find error: 'She don't like coffee'", "a": "She", "b": "don't", "c": "like", "d": "coffee", "ans": "B", "exp": "Correct is 'doesn't'"},
    {"q": "Find error: 'He go to school'", "a": "He", "b": "go", "c": "to", "d": "school", "ans": "B", "exp": "He goes to school"},
    {"q": "Find error: 'They was playing'", "a": "They", "b": "was", "c": "playing", "d": "None", "ans": "B", "exp": "They were playing"},
    {"q": "Find error: 'I have went there'", "a": "I", "b": "have", "c": "went", "d": "there", "ans": "C", "exp": "I have gone there"},
    {"q": "Find error: 'She don't know'", "a": "She", "b": "don't", "c": "know", "d": "None", "ans": "B", "exp": "She doesn't know"},
    {"q": "Find error: 'He can speaks English'", "a": "He", "b": "can", "c": "speaks", "d": "English", "ans": "C", "exp": "He can speak English"},
    {"q": "Find error: 'They has done it'", "a": "They", "b": "has", "c": "done", "d": "it", "ans": "B", "exp": "They have done it"},
    {"q": "Find error: 'Me and him went'", "a": "Me", "b": "and", "c": "him", "d": "went", "ans": "A", "exp": "He and I went"},
    {"q": "Find error: 'Your the best'", "a": "Your", "b": "the", "c": "best", "d": "None", "ans": "A", "exp": "You're the best"},
    {"q": "Find error: 'Its a beautiful day'", "a": "Its", "b": "a", "c": "beautiful", "d": "day", "ans": "A", "exp": "It's a beautiful day"},
    {"q": "Find error: 'Each of the boys are here'", "a": "Each", "b": "boys", "c": "are", "d": "here", "ans": "C", "exp": "Each is singular, use 'is'"},
    {"q": "Find error: 'Neither of them are coming'", "a": "Neither", "b": "them", "c": "are", "d": "coming", "ans": "C", "exp": "Neither is singular, use 'is'"},
    {"q": "Find error: 'The news are good'", "a": "The", "b": "news", "c": "are", "d": "good", "ans": "C", "exp": "News is singular, use 'is'"},
    {"q": "Find error: 'One of my friend is here'", "a": "One", "b": "my", "c": "friend", "d": "is", "ans": "C", "exp": "One of my friends"},
    {"q": "Find error: 'Everyone have done it'", "a": "Everyone", "b": "have", "c": "done", "d": "it", "ans": "B", "exp": "Everyone has done it"},
]

# Idioms (15 questions)
idioms = [
    {"q": "Meaning of 'Piece of cake'", "a": "Difficult", "b": "Easy", "c": "Expensive", "d": "Cheap", "ans": "B", "exp": "Piece of cake = easy"},
    {"q": "Meaning of 'Break the ice'", "a": "Start conversation", "b": "Break something", "c": "Stop talking", "d": "Get angry", "ans": "A", "exp": "Break the ice = start conversation"},
    {"q": "Meaning of 'Cost an arm and a leg'", "a": "Cheap", "b": "Expensive", "c": "Painful", "d": "Injury", "ans": "B", "exp": "Very expensive"},
    {"q": "Meaning of 'Under the weather'", "a": "Feeling ill", "b": "Feeling happy", "c": "Feeling excited", "d": "Feeling tired", "ans": "A", "exp": "Under the weather = sick"},
    {"q": "Meaning of 'Hit the books'", "a": "Throw books", "b": "Study", "c": "Read fast", "d": "Write", "ans": "B", "exp": "Hit the books = study"},
    {"q": "Meaning of 'Spill the beans'", "a": "Reveal secret", "b": "Drop food", "c": "Make mess", "d": "Eat", "ans": "A", "exp": "Spill the beans = reveal secret"},
    {"q": "Meaning of 'Bite the bullet'", "a": "Eat fast", "b": "Face difficulty", "c": "Run away", "d": "Hide", "ans": "B", "exp": "Bite the bullet = face hardship"},
    {"q": "Meaning of 'Let the cat out of the bag'", "a": "Release animal", "b": "Reveal secret", "c": "Run away", "d": "Hide", "ans": "B", "exp": "Reveal a secret"},
    {"q": "Meaning of 'Once in a blue moon'", "a": "Frequently", "b": "Rarely", "c": "Always", "d": "Never", "ans": "B", "exp": "Very rarely"},
    {"q": "Meaning of 'A blessing in disguise'", "a": "Bad luck", "b": "Good that seemed bad", "c": "Curse", "d": "Misfortune", "ans": "B", "exp": "Something good that seemed bad"},
    {"q": "Meaning of 'Burn the midnight oil'", "a": "Stay up late", "b": "Start a fire", "c": "Cook food", "d": "Sleep early", "ans": "A", "exp": "Work late at night"},
    {"q": "Meaning of 'Caught red-handed'", "a": "Hands red", "b": "Caught doing wrong", "c": "Painting", "d": "Injured", "ans": "B", "exp": "Caught in the act"},
    {"q": "Meaning of 'Go the extra mile'", "a": "Walk far", "b": "Do extra work", "c": "Run fast", "d": "Drive", "ans": "B", "exp": "Do more than expected"},
    {"q": "Meaning of 'Kill two birds with one stone'", "a": "Violent", "b": "Achieve two things at once", "c": "Hunt", "d": "Destroy", "ans": "B", "exp": "Accomplish two goals"},
    {"q": "Meaning of 'Put your cards on the table'", "a": "Play cards", "b": "Be honest", "c": "Hide", "d": "Cheat", "ans": "B", "exp": "Be open and honest"},
]

# Add all verbal questions
all_verbal_qs = synonyms + antonyms + fill_blanks + errors + idioms
for q in all_verbal_qs:
    verbal_questions.append(q)
    MockTestQuestion.objects.create(
        mock_test=verbal_test,
        question_text=q["q"],
        option_a=q["a"],
        option_b=q["b"],
        option_c=q["c"],
        option_d=q["d"],
        correct_answer=q["ans"],
        explanation=q["exp"],
        marks=1
    )

print(f"✅ Added {len(all_verbal_qs)} questions to Verbal Ability Master Test")
print(f"   - Synonyms: {len(synonyms)}")
print(f"   - Antonyms: {len(antonyms)}")
print(f"   - Fill in blanks: {len(fill_blanks)}")
print(f"   - Spot errors: {len(errors)}")
print(f"   - Idioms: {len(idioms)}")

# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "="*60)
print("🎉 ALL TESTS CREATED SUCCESSFULLY!")
print("="*60)
print(f"\n📊 Total Tests: {MockTest.objects.count()}")
print(f"📊 Total Questions: {MockTestQuestion.objects.count()}")

print("\n📋 Available Tests:")
for test in MockTest.objects.all():
    print(f"   • {test.title}: {test.questions.count()} questions ({test.time_limit} minutes)")

print("\n✅ You can now:")
print("   1. Go to http://127.0.0.1:8000/mock-tests/")
print("   2. Take any test")
print("   3. View your results")
print("="*60)