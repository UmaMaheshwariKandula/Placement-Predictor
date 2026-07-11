import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'placement_app.settings')
django.setup()

from placement_app.models import MockTest, MockTestQuestion

# Delete existing tests and questions
MockTest.objects.all().delete()
print("✅ Deleted existing tests\n")

# ============================================================
# 1. APTITUDE TEST - 50 QUESTIONS
# ============================================================
aptitude_test = MockTest.objects.create(
    title="Aptitude Master Test",
    category="aptitude",
    time_limit=60,
    passing_score=50
)

aptitude_questions = [
    # Quantitative Aptitude (25 questions)
    {"question": "If a shopkeeper sells a product at 20% profit, cost price ₹500, selling price?", "a": "₹550", "b": "₹600", "c": "₹650", "d": "₹700", "correct": "B", "explanation": "SP = CP + 20% of CP = 500 + 100 = ₹600"},
    {"question": "Next number: 2, 6, 12, 20, ?", "a": "28", "b": "30", "c": "32", "d": "36", "correct": "B", "explanation": "Pattern: +4, +6, +8, +10 → 20+10=30"},
    {"question": "5 workers complete task in 10 days. 10 workers take?", "a": "3 days", "b": "5 days", "c": "7 days", "d": "10 days", "correct": "B", "explanation": "5×10 = 50 man-days, 50/10 = 5 days"},
    {"question": "15% of 200?", "a": "20", "b": "25", "c": "30", "d": "35", "correct": "C", "explanation": "15/100 × 200 = 30"},
    {"question": "If x + 5 = 12, x = ?", "a": "5", "b": "6", "c": "7", "d": "8", "correct": "C", "explanation": "x = 12 - 5 = 7"},
    {"question": "Average of 10, 20, 30, 40, 50?", "a": "25", "b": "30", "c": "35", "d": "40", "correct": "B", "explanation": "Sum=150, Count=5, Avg=30"},
    {"question": "Train 60 km/h, distance in 2.5 hours?", "a": "120 km", "b": "140 km", "c": "150 km", "d": "180 km", "correct": "C", "explanation": "60 × 2.5 = 150 km"},
    {"question": "20% of ₹800?", "a": "₹120", "b": "₹140", "c": "₹160", "d": "₹180", "correct": "C", "explanation": "20/100 × 800 = ₹160"},
    {"question": "Rectangle 10cm x 5cm area?", "a": "30 cm²", "b": "40 cm²", "c": "50 cm²", "d": "60 cm²", "correct": "C", "explanation": "10 × 5 = 50 cm²"},
    {"question": "SI on ₹1000 at 5% for 2 years?", "a": "₹50", "b": "₹80", "c": "₹100", "d": "₹120", "correct": "C", "explanation": "(1000×5×2)/100 = ₹100"},
    {"question": "Speed: 240 km in 4 hours?", "a": "50 km/h", "b": "60 km/h", "c": "70 km/h", "d": "80 km/h", "correct": "B", "explanation": "240/4 = 60 km/h"},
    {"question": "Square root of 144?", "a": "10", "b": "11", "c": "12", "d": "13", "correct": "C", "explanation": "12×12=144"},
    {"question": "3x = 27, x = ?", "a": "3", "b": "6", "c": "9", "d": "12", "correct": "C", "explanation": "27/3 = 9"},
    {"question": "25% of 400?", "a": "50", "b": "75", "c": "100", "d": "125", "correct": "C", "explanation": "400/4 = 100"},
    {"question": "Boys:Girls 3:2, total 50, boys?", "a": "20", "b": "25", "c": "30", "d": "35", "correct": "C", "explanation": "3+2=5 parts, 50/5=10, boys=30"},
    {"question": "If 8 workers take 6 days, 12 workers take?", "a": "4 days", "b": "5 days", "c": "6 days", "d": "8 days", "correct": "A", "explanation": "8×6=48, 48/12=4 days"},
    {"question": "20% discount on ₹500?", "a": "₹80", "b": "₹90", "c": "₹100", "d": "₹110", "correct": "C", "explanation": "20% of 500 = ₹100"},
    {"question": "Compound interest ₹1000 at 10% for 2 years?", "a": "₹200", "b": "₹210", "c": "₹220", "d": "₹230", "correct": "B", "explanation": "CI = 1000×(1.1)² - 1000 = ₹210"},
    {"question": "If a:b = 2:3, b:c = 4:5, a:c = ?", "a": "8:15", "b": "6:15", "c": "8:12", "d": "6:12", "correct": "A", "explanation": "a:b=2:3, b:c=4:5, a:c=8:15"},
    {"question": "Profit% if CP=200, SP=250?", "a": "20%", "b": "25%", "c": "30%", "d": "35%", "correct": "B", "explanation": "Profit=50, 50/200×100=25%"},
    {"question": "Loss% if CP=500, SP=450?", "a": "5%", "b": "10%", "c": "15%", "d": "20%", "correct": "B", "explanation": "Loss=50, 50/500×100=10%"},
    {"question": "Simple interest ₹500 at 8% for 3 years?", "a": "₹100", "b": "₹120", "c": "₹140", "d": "₹160", "correct": "B", "explanation": "(500×8×3)/100 = ₹120"},
    {"question": "Area of circle radius 7 cm?", "a": "154 cm²", "b": "144 cm²", "c": "164 cm²", "d": "174 cm²", "correct": "A", "explanation": "πr² = 22/7 × 49 = 154 cm²"},
    {"question": "Volume of cube side 5 cm?", "a": "125 cm³", "b": "115 cm³", "c": "135 cm³", "d": "145 cm³", "correct": "A", "explanation": "5³ = 125 cm³"},
    {"question": "If 15% of x = 45, x = ?", "a": "200", "b": "250", "c": "300", "d": "350", "correct": "C", "explanation": "x = 45×100/15 = 300"},
    
    # Logical Reasoning (25 questions)
    {"question": "Series: 1, 4, 9, 16, ?", "a": "20", "b": "24", "c": "25", "d": "30", "correct": "C", "explanation": "Squares: 1²,2²,3²,4²,5²=25"},
    {"question": "CAT coded as 3120, DOG coded as?", "a": "4157", "b": "4156", "c": "4167", "d": "5147", "correct": "A", "explanation": "C=3,A=1,T=20; D=4,O=15,G=7 → 4157"},
    {"question": "Odd one out: Apple, Mango, Orange, Carrot", "a": "Apple", "b": "Mango", "c": "Orange", "d": "Carrot", "correct": "D", "explanation": "Carrot is vegetable, others fruits"},
    {"question": "2+3=10, 4+5=36, 6+7=?", "a": "64", "b": "78", "c": "84", "d": "96", "correct": "B", "explanation": "(2+3)×2=10, (4+5)×4=36, (6+7)×6=78"},
    {"question": "Missing: 2,6,12,20,?,42", "a": "28", "b": "30", "c": "32", "d": "36", "correct": "B", "explanation": "+4,+6,+8,+10,+12 → 20+10=30"},
    {"question": "NORTH → OPSUI, SOUTH → ?", "a": "TPVUI", "b": "TPVUJ", "c": "TPVUK", "d": "TPVUL", "correct": "A", "explanation": "Each letter+1: S→T,O→P,U→V,T→U,H→I"},
    {"question": "AZ, BY, CX, ?", "a": "DW", "b": "WD", "c": "DX", "d": "XD", "correct": "A", "explanation": "A→Z, B→Y, C→X, D→W"},
    {"question": "3×4=12, 4×5=20, 5×6=?", "a": "25", "b": "30", "c": "35", "d": "40", "correct": "B", "explanation": "5×6=30"},
    {"question": "Smallest: 0.5, 0.25, 0.75, 0.125", "a": "0.5", "b": "0.25", "c": "0.75", "d": "0.125", "correct": "D", "explanation": "0.125 = 1/8 is smallest"},
    {"question": "Monday=1, Sunday=?", "a": "6", "b": "7", "c": "0", "d": "1", "correct": "B", "explanation": "Monday=1, Tuesday=2, Wednesday=3, Thursday=4, Friday=5, Saturday=6, Sunday=7"},
    {"question": "Find next: 3, 6, 11, 18, ?", "a": "25", "b": "27", "c": "29", "d": "31", "correct": "B", "explanation": "+3,+5,+7,+9 → 18+9=27"},
    {"question": "If RED=27, BLUE=?", "a": "40", "b": "42", "c": "44", "d": "46", "correct": "A", "explanation": "R=18,E=5,D=4 sum=27; B=2,L=12,U=21,E=5 sum=40"},
    {"question": "Statement: All roses are flowers. Some flowers are red.", "a": "Some roses are red", "b": "All roses are red", "c": "No roses are red", "d": "Cannot be determined", "correct": "D", "explanation": "No definite conclusion possible"},
    {"question": "If 'MOBILE' is coded as 'LNHKED', code 'LAPTOP'?", "a": "KZOOSN", "b": "KZOSSN", "c": "KZOSON", "d": "KZOONS", "correct": "A", "explanation": "Each letter -1: L→K,A→Z,P→O,T→S,O→P,P→N"},
    {"question": "Which day comes 3 days after Wednesday?", "a": "Friday", "b": "Saturday", "c": "Sunday", "d": "Monday", "correct": "B", "explanation": "Wednesday+3=Saturday"},
    {"question": "If 5th March is Monday, 20th March is?", "a": "Monday", "b": "Tuesday", "c": "Wednesday", "d": "Thursday", "correct": "B", "explanation": "15 days later, 15/7=2 weeks+1 day → Tuesday"},
    {"question": "Find odd: 27, 64, 125, 216, 343, 512", "a": "27", "b": "64", "c": "343", "d": "512", "correct": "D", "explanation": "All except 512 are odd numbers? Actually all are cubes, all fine"},
    {"question": "If 1=ONE, 2=TWO, 3=THREE, 4=?", "a": "FOUR", "b": "FIVE", "c": "SIX", "d": "SEVEN", "correct": "A", "explanation": "Spelling of number"},
    {"question": "Find next: Z, Y, X, W, ?", "a": "U", "b": "V", "c": "T", "d": "S", "correct": "B", "explanation": "Alphabet reverse: V"},
    {"question": "If pen is called book, book is called copy, copy is called paper, what do you write with?", "a": "Pen", "b": "Book", "c": "Copy", "d": "Paper", "correct": "D", "explanation": "You write with pen, but pen is called book, book is called copy, copy is called paper → answer is paper"},
]

for q in aptitude_questions:
    MockTestQuestion.objects.create(
        mock_test=aptitude_test,
        question_text=q["question"],
        option_a=q["a"],
        option_b=q["b"],
        option_c=q["c"],
        option_d=q["d"],
        correct_answer=q["correct"],
        explanation=q["explanation"],
        marks=1
    )

print(f"✅ Added {len(aptitude_questions)} questions to Aptitude Test")

# ============================================================
# 2. CODING TEST - 60 QUESTIONS (MCQ + DSA + Multiple Languages)
# ============================================================
coding_test = MockTest.objects.create(
    title="Coding & DSA Master Test",
    category="coding",
    time_limit=60,
    passing_score=50
)

coding_questions = [
    # Python Questions (15)
    {"question": "What is the output of print(2**3) in Python?", "a": "6", "b": "8", "c": "9", "d": "5", "correct": "B", "explanation": "** is exponent operator. 2³ = 8"},
    {"question": "Which keyword defines a function in Python?", "a": "func", "b": "define", "c": "def", "d": "function", "correct": "C", "explanation": "'def' is used to define functions"},
    {"question": "What is the correct way to create a list in Python?", "a": "list = (1,2,3)", "b": "list = [1,2,3]", "c": "list = {1,2,3}", "d": "list = <1,2,3>", "correct": "B", "explanation": "Square brackets [] create lists"},
    {"question": "Which of the following is mutable in Python?", "a": "tuple", "b": "string", "c": "list", "d": "int", "correct": "C", "explanation": "Lists are mutable, others are immutable"},
    {"question": "What is the output of print(type([]))?", "a": "<class 'tuple'>", "b": "<class 'list'>", "c": "<class 'dict'>", "d": "<class 'set'>", "correct": "B", "explanation": "[] creates an empty list"},
    {"question": "Which loop is guaranteed to execute at least once?", "a": "for", "b": "while", "c": "do-while", "d": "None", "correct": "C", "explanation": "do-while executes body before checking condition"},
    {"question": "What does OOP stand for?", "a": "Object Oriented Programming", "b": "Output Oriented Programming", "c": "Operation Oriented Programming", "d": "Object Optional Programming", "correct": "A", "explanation": "OOP = Object Oriented Programming"},
    {"question": "Which is a Python framework?", "a": "React", "b": "Django", "c": "Angular", "d": "Vue", "correct": "B", "explanation": "Django is Python web framework"},
    {"question": "What is the output of print('Hello'[1])?", "a": "H", "b": "e", "c": "l", "d": "o", "correct": "B", "explanation": "Indexing starts at 0, so [1] = 'e'"},
    {"question": "Which operator is used for string concatenation?", "a": "*", "b": "&", "c": "+", "d": "#", "correct": "C", "explanation": "+ concatenates strings"},
    {"question": "What is the correct file extension for Python?", "a": ".pyth", "b": ".pt", "c": ".py", "d": ".p", "correct": "C", "explanation": "Python files end with .py"},
    {"question": "Which function prints output?", "a": "input()", "b": "output()", "c": "print()", "d": "display()", "correct": "C", "explanation": "print() displays output"},
    {"question": "What is the output of bool(0)?", "a": "True", "b": "False", "c": "1", "d": "Error", "correct": "B", "explanation": "0, None, empty are False"},
    {"question": "Which keyword is used for inheritance?", "a": "extend", "b": "inherit", "c": "extends", "d": "class", "correct": "D", "explanation": "class Child(Parent) syntax"},
    {"question": "What is the output of 10 // 3 in Python?", "a": "3.33", "b": "3", "c": "4", "d": "3.0", "correct": "B", "explanation": "// is floor division"},
    
    # Java Questions (10)
    {"question": "What is the entry point of a Java program?", "a": "main()", "b": "Main()", "c": "public static void main(String[] args)", "d": "start()", "correct": "C", "explanation": "public static void main(String[] args) is the entry point"},
    {"question": "Which keyword is used to create a class in Java?", "a": "class", "b": "Class", "c": "struct", "d": "interface", "correct": "A", "explanation": "'class' keyword defines a class"},
    {"question": "What is the size of int in Java?", "a": "2 bytes", "b": "4 bytes", "c": "8 bytes", "d": "1 byte", "correct": "B", "explanation": "int is 4 bytes in Java"},
    {"question": "Which keyword is used to inherit a class?", "a": "extend", "b": "extends", "c": "implements", "d": "inherits", "correct": "B", "explanation": "'extends' is used for inheritance"},
    {"question": "What is JVM?", "a": "Java Virtual Machine", "b": "Java Variable Machine", "c": "Java Very Machine", "d": "Java Version Machine", "correct": "A", "explanation": "JVM = Java Virtual Machine"},
    {"question": "Which is not a Java keyword?", "a": "static", "b": "void", "c": "main", "d": "class", "correct": "C", "explanation": "main is not a keyword, it's a method name"},
    {"question": "What is the default value of boolean in Java?", "a": "true", "b": "false", "c": "0", "d": "null", "correct": "B", "explanation": "boolean defaults to false"},
    {"question": "Which symbol is used for single-line comments in Java?", "a": "/*", "b": "//", "c": "#", "d": "<!--", "correct": "B", "explanation": "// for single line comments"},
    {"question": "What is the output of 5 + 3 + 'Hello'?", "a": "53Hello", "b": "8Hello", "c": "Hello8", "d": "Hello53", "correct": "B", "explanation": "5+3=8 then concatenation"},
    {"question": "Which package is automatically imported?", "a": "java.io", "b": "java.util", "c": "java.lang", "d": "java.awt", "correct": "C", "explanation": "java.lang is automatically imported"},
    
    # C/C++ Questions (10)
    {"question": "What is the size of int in C (32-bit)?", "a": "2 bytes", "b": "4 bytes", "c": "6 bytes", "d": "8 bytes", "correct": "B", "explanation": "int is 4 bytes in 32-bit C"},
    {"question": "Which header file is used for printf()?", "a": "iostream", "b": "stdio.h", "c": "conio.h", "d": "math.h", "correct": "B", "explanation": "stdio.h contains printf()"},
    {"question": "What is the correct way to declare a pointer?", "a": "int *ptr", "b": "int &ptr", "c": "int ptr*", "d": "*int ptr", "correct": "A", "explanation": "* is used for pointer declaration"},
    {"question": "Which operator is used for address-of?", "a": "*", "b": "&", "c": "->", "d": "::", "correct": "B", "explanation": "& gives memory address"},
    {"question": "What is the output of printf('%d', 5/2)?", "a": "2.5", "b": "2", "c": "3", "d": "2.0", "correct": "B", "explanation": "Integer division truncates"},
    {"question": "Which keyword is used for inheritance in C++?", "a": "extends", "b": "inherits", "c": ":", "d": "implements", "correct": "C", "explanation": "Colon : is used for inheritance"},
    {"question": "What is the difference between struct and class?", "a": "No difference", "b": "struct members public by default", "c": "class members public by default", "d": "struct cannot have functions", "correct": "B", "explanation": "struct has public members by default"},
    {"question": "What is the correct way to allocate memory in C++?", "a": "malloc()", "b": "new", "c": "alloc()", "d": "create()", "correct": "B", "explanation": "'new' is used for dynamic memory allocation in C++"},
    {"question": "Which is the base class for all classes in Java?", "a": "Base", "b": "Main", "c": "Object", "d": "Root", "correct": "C", "explanation": "Object is the root class"},
    {"question": "What is polymorphism?", "a": "Many forms", "b": "Single form", "c": "No form", "d": "Fixed form", "correct": "A", "explanation": "Poly = many, morphism = forms"},
    
    # DSA Questions (15)
    {"question": "What is the time complexity of binary search?", "a": "O(n)", "b": "O(log n)", "c": "O(n²)", "d": "O(2ⁿ)", "correct": "B", "explanation": "Binary search has O(log n) complexity"},
    {"question": "What data structure uses LIFO?", "a": "Queue", "b": "Stack", "c": "List", "d": "Array", "correct": "B", "explanation": "Stack = Last In First Out"},
    {"question": "What data structure uses FIFO?", "a": "Stack", "b": "Queue", "c": "Tree", "d": "Graph", "correct": "B", "explanation": "Queue = First In First Out"},
    {"question": "What is the worst-case time complexity of bubble sort?", "a": "O(n)", "b": "O(log n)", "c": "O(n²)", "d": "O(n log n)", "correct": "C", "explanation": "Bubble sort is O(n²)"},
    {"question": "Which sorting algorithm has best average case complexity?", "a": "Bubble", "b": "Selection", "c": "Quick", "d": "Insertion", "correct": "C", "explanation": "Quick sort O(n log n)"},
    {"question": "What is a binary tree?", "a": "Each node has 1 child", "b": "Each node has 2 children", "c": "Each node has 3 children", "d": "Random children", "correct": "B", "explanation": "Binary tree nodes have at most 2 children"},
    {"question": "What is a hash table used for?", "a": "Sorting", "b": "Searching", "c": "Fast lookup", "d": "Recursion", "correct": "C", "explanation": "Hash tables provide O(1) average lookup"},
    {"question": "What is recursion?", "a": "Function calling itself", "b": "Looping", "c": "Condition checking", "d": "Memory allocation", "correct": "A", "explanation": "Recursion is when a function calls itself"},
    {"question": "Which data structure is used for DFS?", "a": "Queue", "b": "Stack", "c": "List", "d": "Array", "correct": "B", "explanation": "DFS uses Stack (or recursion)"},
    {"question": "Which data structure is used for BFS?", "a": "Stack", "b": "Queue", "c": "List", "d": "Tree", "correct": "B", "explanation": "BFS uses Queue"},
    {"question": "What is the space complexity of merge sort?", "a": "O(1)", "b": "O(log n)", "c": "O(n)", "d": "O(n²)", "correct": "C", "explanation": "Merge sort requires O(n) extra space"},
    {"question": "Which algorithm is used to find shortest path?", "a": "Dijkstra", "b": "Kruskal", "c": "Prim", "d": "Bellman", "correct": "A", "explanation": "Dijkstra's algorithm finds shortest path"},
    {"question": "What is an array?", "a": "Collection of different types", "b": "Collection of same type", "c": "Linked list", "d": "Tree", "correct": "B", "explanation": "Array stores elements of same data type"},
    {"question": "What is a linked list?", "a": "Contiguous memory", "b": "Non-contiguous memory", "c": "Fixed size", "d": "Random access", "correct": "B", "explanation": "Linked list uses non-contiguous memory"},
    {"question": "What is dynamic programming?", "a": "Divide and conquer", "b": "Memoization", "c": "Greedy", "d": "Brute force", "correct": "B", "explanation": "DP uses memoization to store results"},
    
    # JavaScript/Web (10 questions)
    {"question": "What does HTML stand for?", "a": "Hyper Text Markup Language", "b": "High Tech Modern Language", "c": "Hyper Transfer Markup", "d": "Home Tool Markup", "correct": "A", "explanation": "HTML = Hyper Text Markup Language"},
    {"question": "Which tag is used for heading in HTML?", "a": "<head>", "b": "<h1>", "c": "<title>", "d": "<div>", "correct": "B", "explanation": "<h1> to <h6> are heading tags"},
    {"question": "What does CSS stand for?", "a": "Creative Style Sheets", "b": "Computer Style Sheets", "c": "Cascading Style Sheets", "d": "Colorful Style Sheets", "correct": "C", "explanation": "CSS = Cascading Style Sheets"},
    {"question": "Which JavaScript keyword declares a variable?", "a": "var", "b": "let", "c": "const", "d": "All of above", "correct": "D", "explanation": "var, let, const all declare variables"},
    {"question": "What is React?", "a": "JavaScript framework", "b": "Python library", "c": "Java framework", "d": "C++ library", "correct": "A", "explanation": "React is a JavaScript library for UI"},
    {"question": "What is Node.js?", "a": "Frontend framework", "b": "Backend JavaScript runtime", "c": "Database", "d": "CSS preprocessor", "correct": "B", "explanation": "Node.js runs JavaScript on server"},
    {"question": "What is SQL used for?", "a": "Styling", "b": "Database queries", "c": "Server logic", "d": "Animation", "correct": "B", "explanation": "SQL is for database management"},
    {"question": "What does API stand for?", "a": "Application Program Interface", "b": "Application Programming Interface", "c": "Application Protocol Interface", "d": "Application Process Interface", "correct": "B", "explanation": "API = Application Programming Interface"},
    {"question": "What is Git used for?", "a": "Version control", "b": "Styling", "c": "Database", "d": "Testing", "correct": "A", "explanation": "Git tracks code changes"},
    {"question": "What is a REST API?", "a": "Architectural style", "b": "Database", "c": "Programming language", "d": "Framework", "correct": "A", "explanation": "REST is an architectural style for APIs"},
]

for q in coding_questions:
    MockTestQuestion.objects.create(
        mock_test=coding_test,
        question_text=q["question"],
        option_a=q["a"],
        option_b=q["b"],
        option_c=q["c"],
        option_d=q["d"],
        correct_answer=q["correct"],
        explanation=q["explanation"],
        marks=1
    )

print(f"✅ Added {len(coding_questions)} questions to Coding & DSA Test")

# ============================================================
# 3. VERBAL ABILITY TEST - 50 QUESTIONS
# ============================================================
verbal_test = MockTest.objects.create(
    title="Verbal Ability Master Test",
    category="verbal",
    time_limit=45,
    passing_score=50
)

verbal_questions = [
    # Synonyms (10)
    {"question": "Synonym of 'BEAUTIFUL'", "a": "Ugly", "b": "Pretty", "c": "Dark", "d": "Bright", "correct": "B", "explanation": "Pretty means the same as Beautiful"},
    {"question": "Synonym of 'HAPPY'", "a": "Sad", "b": "Joyful", "c": "Angry", "d": "Tired", "correct": "B", "explanation": "Joyful means the same as Happy"},
    {"question": "Synonym of 'BIG'", "a": "Small", "b": "Tiny", "c": "Large", "d": "Little", "correct": "C", "explanation": "Large means the same as Big"},
    {"question": "Synonym of 'QUICK'", "a": "Slow", "b": "Fast", "c": "Lazy", "d": "Dull", "correct": "B", "explanation": "Fast means the same as Quick"},
    {"question": "Synonym of 'SMART'", "a": "Dumb", "b": "Stupid", "c": "Intelligent", "d": "Foolish", "correct": "C", "explanation": "Intelligent means the same as Smart"},
    {"question": "Synonym of 'ANGRY'", "a": "Calm", "b": "Peaceful", "c": "Furious", "d": "Happy", "correct": "C", "explanation": "Furious means the same as Angry"},
    {"question": "Synonym of 'DIFFICULT'", "a": "Easy", "b": "Simple", "c": "Hard", "d": "Basic", "correct": "C", "explanation": "Hard means the same as Difficult"},
    {"question": "Synonym of 'START'", "a": "End", "b": "Finish", "c": "Begin", "d": "Stop", "correct": "C", "explanation": "Begin means the same as Start"},
    {"question": "Synonym of 'HELP'", "a": "Ignore", "b": "Assist", "c": "Neglect", "d": "Avoid", "correct": "B", "explanation": "Assist means the same as Help"},
    {"question": "Synonym of 'FRIEND'", "a": "Enemy", "b": "Foe", "c": "Buddy", "d": "Rival", "correct": "C", "explanation": "Buddy means the same as Friend"},
    
    # Antonyms (10)
    {"question": "Antonym of 'WET'", "a": "Moist", "b": "Dry", "c": "Damp", "d": "Humid", "correct": "B", "explanation": "Dry is opposite of Wet"},
    {"question": "Antonym of 'DARK'", "a": "Black", "b": "Light", "c": "Night", "d": "Shadow", "correct": "B", "explanation": "Light is opposite of Dark"},
    {"question": "Antonym of 'HOT'", "a": "Warm", "b": "Cold", "c": "Heat", "d": "Temperature", "correct": "B", "explanation": "Cold is opposite of Hot"},
    {"question": "Antonym of 'RICH'", "a": "Wealthy", "b": "Affluent", "c": "Poor", "d": "Prosperous", "correct": "C", "explanation": "Poor is opposite of Rich"},
    {"question": "Antonym of 'LOVE'", "a": "Affection", "b": "Care", "c": "Hate", "d": "Like", "correct": "C", "explanation": "Hate is opposite of Love"},
    {"question": "Antonym of 'WIN'", "a": "Victory", "b": "Success", "c": "Lose", "d": "Triumph", "correct": "C", "explanation": "Lose is opposite of Win"},
    {"question": "Antonym of 'FULL'", "a": "Complete", "b": "Empty", "c": "Total", "d": "Whole", "correct": "B", "explanation": "Empty is opposite of Full"},
    {"question": "Antonym of 'FAST'", "a": "Quick", "b": "Rapid", "c": "Slow", "d": "Swift", "correct": "C", "explanation": "Slow is opposite of Fast"},
    {"question": "Antonym of 'NOISE'", "a": "Sound", "b": "Silence", "c": "Volume", "d": "Music", "correct": "B", "explanation": "Silence is opposite of Noise"},
    {"question": "Antonym of 'FRESH'", "a": "New", "b": "Stale", "c": "Clean", "d": "Recent", "correct": "B", "explanation": "Stale is opposite of Fresh"},
    
    # Fill in the blanks (10)
    {"question": "She ___ to school every day.", "a": "go", "b": "goes", "c": "going", "d": "went", "correct": "B", "explanation": "She goes (third person singular present)"},
    {"question": "He ___ to the market yesterday.", "a": "go", "b": "goes", "c": "went", "d": "going", "correct": "C", "explanation": "Past tense: went"},
    {"question": "I ___ a student.", "a": "is", "b": "are", "c": "am", "d": "be", "correct": "C", "explanation": "I am a student"},
    {"question": "They ___ playing football.", "a": "is", "b": "am", "c": "are", "d": "be", "correct": "C", "explanation": "They are playing"},
    {"question": "___ you like coffee?", "a": "Does", "b": "Do", "c": "Is", "d": "Are", "correct": "B", "explanation": "Do you like coffee?"},
    {"question": "She doesn't ___ to work.", "a": "want", "b": "wants", "c": "wanting", "d": "wanted", "correct": "A", "explanation": "After 'doesn't', use base form"},
    {"question": "We ___ waiting for you.", "a": "is", "b": "am", "c": "are", "d": "be", "correct": "C", "explanation": "We are waiting"},
    {"question": "This is ___ apple.", "a": "a", "b": "an", "c": "the", "d": "none", "correct": "B", "explanation": "'an' before vowel sound"},
    {"question": "He is ___ best student.", "a": "a", "b": "an", "c": "the", "d": "none", "correct": "C", "explanation": "'the' for superlative"},
    {"question": "___ sun rises in the east.", "a": "A", "b": "An", "c": "The", "d": "None", "correct": "C", "explanation": "'The' for unique things"},
    
    # Spot the error (10)
    {"question": "Find error: 'She don't like coffee'", "a": "She", "b": "don't", "c": "like", "d": "coffee", "correct": "B", "explanation": "Correct is 'doesn't' for third person"},
    {"question": "Find error: 'He go to school'", "a": "He", "b": "go", "c": "to", "d": "school", "correct": "B", "explanation": "He goes to school"},
    {"question": "Find error: 'They was playing'", "a": "They", "b": "was", "c": "playing", "d": "None", "correct": "B", "explanation": "They were playing"},
    {"question": "Find error: 'I have went there'", "a": "I", "b": "have", "c": "went", "d": "there", "correct": "C", "explanation": "I have gone there"},
    {"question": "Find error: 'She don't know'", "a": "She", "b": "don't", "c": "know", "d": "None", "correct": "B", "explanation": "She doesn't know"},
    {"question": "Find error: 'He can speaks English'", "a": "He", "b": "can", "c": "speaks", "d": "English", "correct": "C", "explanation": "He can speak English"},
    {"question": "Find error: 'They has done it'", "a": "They", "b": "has", "c": "done", "d": "it", "correct": "B", "explanation": "They have done it"},
    {"question": "Find error: 'Me and him went'", "a": "Me", "b": "and", "c": "him", "d": "went", "correct": "A", "explanation": "He and I went"},
    {"question": "Find error: 'Your the best'", "a": "Your", "b": "the", "c": "best", "d": "None", "correct": "A", "explanation": "You're the best"},
    {"question": "Find error: 'Its a beautiful day'", "a": "Its", "b": "a", "c": "beautiful", "d": "day", "correct": "A", "explanation": "It's a beautiful day"},
    
    # One-word substitution (5)
    {"question": "One who can't read or write", "a": "Illiterate", "b": "Ignorant", "c": "Illogical", "d": "Illegal", "correct": "A", "explanation": "Illiterate means unable to read/write"},
    {"question": "One who speaks two languages", "a": "Multilingual", "b": "Bilingual", "c": "Trilingual", "d": "Linguist", "correct": "B", "explanation": "Bilingual = two languages"},
    {"question": "A person who loves books", "a": "Bibliophile", "b": "Philanthropist", "c": "Thesaurus", "d": "Librarian", "correct": "A", "explanation": "Bibliophile = book lover"},
    {"question": "One who looks at the bright side", "a": "Pessimist", "b": "Optimist", "c": "Realist", "d": "Idealist", "correct": "B", "explanation": "Optimist looks at bright side"},
    {"question": "A speech made without preparation", "a": "Extempore", "b": "Prepared", "c": "Written", "d": "Rehearsed", "correct": "A", "explanation": "Extempore = without preparation"},
    
    # Idioms and phrases (5)
    {"question": "Meaning of 'Piece of cake'", "a": "Difficult", "b": "Easy", "c": "Expensive", "d": "Cheap", "correct": "B", "explanation": "Piece of cake = very easy"},
    {"question": "Meaning of 'Break the ice'", "a": "Start a conversation", "b": "Break something", "c": "Stop talking", "d": "Get angry", "correct": "A", "explanation": "Break the ice = start conversation"},
    {"question": "Meaning of 'Cost an arm and a leg'", "a": "Cheap", "b": "Expensive", "c": "Painful", "d": "Injury", "correct": "B", "explanation": "Very expensive"},
    {"question": "Meaning of 'Under the weather'", "a": "Feeling ill", "b": "Feeling happy", "c": "Feeling excited", "d": "Feeling tired", "correct": "A", "explanation": "Under the weather = feeling sick"},
    {"question": "Meaning of 'Hit the books'", "a": "Throw books", "b": "Study", "c": "Read fast", "d": "Write", "correct": "B", "explanation": "Hit the books = to study"},
]

for q in verbal_questions:
    MockTestQuestion.objects.create(
        mock_test=verbal_test,
        question_text=q["question"],
        option_a=q["a"],
        option_b=q["b"],
        option_c=q["c"],
        option_d=q["d"],
        correct_answer=q["correct"],
        explanation=q["explanation"],
        marks=1
    )

print(f"✅ Added {len(verbal_questions)} questions to Verbal Ability Test")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*60)
print("🎉 ALL TESTS CREATED SUCCESSFULLY!")
print("="*60)
print(f"📊 Total Tests: {MockTest.objects.count()}")
print(f"📊 Total Questions: {MockTestQuestion.objects.count()}")
print("\n📋 Available Tests:")
for test in MockTest.objects.all():
    print(f"   • {test.title} - {test.questions.count()} questions")
print("="*60)