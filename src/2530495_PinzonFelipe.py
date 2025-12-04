# Manejo de números y booleanos en Python

## Nombre: Felipe Pinzon Segura
## Marticula: 2530495
## Grupo: IM 1-2

# Resumen Ejecutivo
"""
Los tipos int y float en Python representan números enteros y de punto flotante respectivamente.
Los enteros (int) almacenan valores sin decimales, mientras que los flotantes (float) pueden 
representar números con parte decimal. Los booleanos (True/False) son el resultado de evaluar 
expresiones lógicas y comparaciones, siendo esenciales para la toma de decisiones. Validar 
rangos y evitar divisiones entre cero es crucial para prevenir errores y garantizar la 
corrección de los cálculos. Este documento cubre seis problemas que demuestran el uso de 
enteros, flotantes y booleanos en contextos como conversiones de temperatura, cálculos de 
nómina, elegibilidad para descuentos, estadísticas básicas, aprobación de préstamos y 
cálculo de IMC.
"""

# Principles & Good Practices (short list)
"""
- Usar tipos apropiados: int para valores discretos, float para mediciones continuas
- Evitar duplicar expresiones complejas almacenando resultados en variables
- Validar datos antes de operar para prevenir errores y garantizar consistencia
- Usar nombres descriptivos que indiquen claramente el propósito de cada variable
- Documentar el significado de los valores booleanos en cada contexto específico
"""


# Problem 1: Temperature converter and range flag
"""
Description: 
Converts temperature from Celsius to Fahrenheit and Kelvin, and determines
if the temperature is considered high (>= 30.0°C).

Inputs:
- temp_c (float): temperature in Celsius

Outputs:
- Fahrenheit: converted temperature
- Kelvin: converted temperature  
- High temperature: boolean flag

Validations:
- Input must be convertible to float
- Resulting Kelvin temperature must be >= 0.0 (absolute zero)

Test cases:
1) Normal: temp_c = 25.0 → F=77.0, K=298.15, High=false
2) Border: temp_c = 30.0 → F=86.0, K=303.15, High=true
3) Error: temp_c = "abc" → Error (invalid input)
"""

try:
    temp_c = float(input("Enter temperature in Celsius: "))
        
    # Validar posibilidad física
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: invalid temperature (below absolute zero)")
        
    # Conversiones
    temp_f = temp_c * 9 / 5 + 32
    is_high_temperature = temp_c >= 30.0
        
    # Salidas
    print(f"Fahrenheit: {temp_f:.2f}")
    print(f"Kelvin: {temp_k:.2f}")
    print(f"High temperature: {str(is_high_temperature).lower()}")
        
except ValueError:
    print("Error: invalid input")


# Problem 2: Work hours and overtime payment
"""
Description:
Calculates weekly pay including regular and overtime hours. Overtime hours
(> 40) are paid at 150% of normal rate.

Inputs:
- hours_worked (float): total hours worked in week
- hourly_rate (float): payment per hour

Outputs:
- Regular pay: payment for first 40 hours
- Overtime pay: payment for hours beyond 40
- Total pay: sum of regular and overtime pay
- Has overtime: boolean flag

Validations:
- hours_worked >= 0
- hourly_rate > 0

Test cases:
1) Normal: hours=45, rate=10 → regular=400, overtime=75, total=475, overtime=true
2) Border: hours=40, rate=15 → regular=600, overtime=0, total=600, overtime=false
3) Error: hours=-5, rate=10 → Error (invalid input)
"""

try:
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
        
    # Validaciones
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")

    # Cálculos
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)
        
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > 40
        
    # Salidas
    print(f"Regular pay: {regular_pay:.2f}")
    print(f"Overtime pay: {overtime_pay:.2f}")
    print(f"Total pay: {total_pay:.2f}")
    print(f"Has overtime: {str(has_overtime).lower()}")
        
except ValueError:
    print("Error: invalid input")


# Problem 3: Discount eligibility with booleans
"""
Description:
Determines discount eligibility based on student/senior status or purchase amount.
Applies 10% discount if eligible.

Inputs:
- purchase_total (float): total purchase amount
- is_student_text (str): "YES" or "NO" for student status
- is_senior_text (str): "YES" or "NO" for senior status

Outputs:
- Discount eligible: boolean flag
- Final total: purchase total after discount (if applicable)

Validations:
- purchase_total >= 0
- Input texts must be "YES" or "NO" (case insensitive)

Test cases:
1) Normal: total=800, student="YES", senior="NO" → eligible=true, final=720
2) Border: total=1000, student="NO", senior="NO" → eligible=true, final=900
3) Error: total=-100, student="YES", senior="NO" → Error (invalid input)
"""


try:
    purchase_total = float(input("Enter purchase total: "))
    is_student_text = input("Are you a student? (YES/NO): ").upper()
    is_senior_text = input("Are you a senior? (YES/NO): ").upper()
        
    # Validaciones
    if purchase_total < 0:
        print("Error: invalid input")
            
    if is_student_text not in ["YES", "NO"] or is_senior_text not in ["YES", "NO"]:
        print("Error: invalid input")
        
    # Convertir a booleano
    is_student = is_student_text == "YES"
    is_senior = is_senior_text == "YES"
        
    # Determinar elegibilidad
    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
        
    # Calcular total final
    if discount_eligible:
        final_total = purchase_total * 0.9
    else:
        final_total = purchase_total
        
    # Salidas
    print(f"Discount eligible: {str(discount_eligible).lower()}")
    print(f"Final total: {final_total:.2f}")
        
except ValueError:
    print("Error: invalid input")


# Problem 4: Basic statistics of three integers

"""
Description:
Calculates basic statistics (sum, average, max, min) and checks if all three
numbers are even.

Inputs:
- n1 (int): first integer
- n2 (int): second integer  
- n3 (int): third integer

Outputs:
- Sum: total of three numbers
- Average: mean value (float)
- Max: largest number
- Min: smallest number
- All even: boolean flag

Validations:
- All inputs must be convertible to integers

Test cases:
1) Normal: 4, 7, 2 → sum=13, avg=4.33, max=7, min=2, all_even=false
2) Border: 2, 4, 6 → sum=12, avg=4.0, max=6, min=2, all_even=true
3) Error: "abc", 5, 3 → Error (invalid input)
"""

try:
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))
    n3 = int(input("Enter third integer: "))
        
    # Cálculos
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
        
    # Salidas
    print(f"Sum: {sum_value}")
    print(f"Average: {average_value:.2f}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")
        
except ValueError:
    print("Error: invalid input")


# Problem 5: Loan eligibility (income and debt ratio)
"""
Description:
Determines loan eligibility based on income, debt ratio, and credit score.

Inputs:
- monthly_income (float): monthly income amount
- monthly_debt (float): monthly debt payments  
- credit_score (int): credit score value

Outputs:
- Debt ratio: monthly_debt / monthly_income
- Eligible: boolean flag for loan approval

Validations:
- monthly_income > 0 (avoid division by zero)
- monthly_debt >= 0
- credit_score >= 0

Test cases:
1) Normal: income=10000, debt=3000, score=700 → ratio=0.3, eligible=true
2) Border: income=8000, debt=3200, score=650 → ratio=0.4, eligible=true
3) Error: income=0, debt=1000, score=700 → Error (invalid input)
"""

try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))
        
    # Validaciones
    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
        
    # Cálculos
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0 and 
               debt_ratio <= 0.4 and 
               credit_score >= 650)
        
    # Salidas
    print(f"Debt ratio: {debt_ratio:.2f}")
    print(f"Eligible: {str(eligible).lower()}")
        
except ValueError:
    print("Error: invalid input")


# Problem 6: Body Mass Index (BMI) and category flag
"""
Description:
Calculates Body Mass Index and categorizes into underweight, normal, or overweight.

Inputs:
- weight_kg (float): weight in kilograms
- height_m (float): height in meters

Outputs:
- BMI: calculated body mass index
- Underweight: boolean flag for BMI < 18.5
- Normal: boolean flag for 18.5 <= BMI < 25.0  
- Overweight: boolean flag for BMI >= 25.0

Validations:
- weight_kg > 0
- height_m > 0

Test cases:
1) Normal: weight=70, height=1.75 → BMI=22.86, underweight=false, normal=true, overweight=false
2) Border: weight=60, height=1.80 → BMI=18.52, underweight=false, normal=true, overweight=false
3) Error: weight=0, height=1.70 → Error (invalid input)
"""


try:
    weight_kg = float(input("Enter weight in kg: "))
    height_m = float(input("Enter height in meters: "))
        
    # Validaciones
    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
        
    # Cálculo de IMC
    bmi = weight_kg / (height_m * height_m)
    bmi_rounded = round(bmi, 2)
        
    # Indicadores de categoría
    is_underweight = bmi < 18.5
    is_normal = 18.5 <= bmi < 25.0
    is_overweight = bmi >= 25.0
        
    # Salidas
    print(f"BMI: {bmi_rounded}")
    print(f"Underweight: {str(is_underweight).lower()}")
    print(f"Normal: {str(is_normal).lower()}")
    print(f"Overweight: {str(is_overweight).lower()}")
        
except ValueError:
    print("Error: invalid input")

        
# CONCLUSIONES
"""
    El trabajo con tipos numéricos y booleanos en Python demuestra su importancia fundamental
    en la resolución de problemas del mundo real. Los enteros son ideales para conteos y valores
    discretos, mientras que los flotantes permiten representar mediciones continuas con precisión.
    Las comparaciones entre estos tipos generan valores booleanos esenciales para la toma de
    decisiones mediante estructuras condicionales.

    La validación de rangos y la prevención de divisiones entre cero son prácticas críticas que
    evitan errores en tiempo de ejecución y garantizan la robustez del software. El diseño de
    condiciones combinadas con operadores lógicos (and, or, not) permite modelar reglas de negocio
    complejas de manera clara y eficiente.

    Estos patrones se repiten consistentemente en diversos dominios como nóminas, sistemas de
    descuentos, aprobación de préstamos y cálculos de salud, demostrando la versatilidad de estos
    conceptos básicos en la programación. La práctica de validar entradas antes de procesar datos
    es fundamental para crear aplicaciones confiables y seguras.
"""

# REFERENCIAS
"""
    1) GG - Python Numbers
       URL: https://www.geeksforgeeks.org/python/python-numbers/
    2) Python - Expresions
       URL: https://docs.python.org/3/reference/expressions.html
    3) Python - PEP 8 – Style Guide for Python Code
       URL: https://www.python.org/dev/peps/pep-0008/
    4) Python - Built-in Types
       URL: https://docs.python.org/3.11/library/stdtypes.html
    5) Python Programming MOOC 2024 - Conditional statements
       URL: https://programming-24.mooc.fi/part-1/5-conditional-statements?
"""

# REPOSITORIO DE GITHUB
"""
    URL: https://github.com/FelipePinzonS/Manejo_De_Numeros_Y_Booleanos.git
"""