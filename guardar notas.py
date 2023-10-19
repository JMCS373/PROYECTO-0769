#para instalar pip install xlsxwriter
import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook("demo.xlsx")
worksheet = workbook.add_worksheet()

# Ajusta el ancho de columna, no se en que medida jsjsjs
worksheet.set_column("A:A", 20)

# Para dar formato en negrita
bold = workbook.add_format({"bold": True})

# Mete texto oh si
worksheet.write("A1", "Hello")

# Mete texto negrito :/
worksheet.write("A2", "World", bold)

# Mete numeros con indice matricial (fila, columna, valor) inicia en 0 osea 0,0 = "A1"
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
#worksheet.insert_image("B5", "logo.png")

workbook.close()

#ejemplo del inge jsjsj
def guardar_notas():
    estudiantes = ['miguel', 'jorge', 'daniel', 'pedro', 'juan', 'diego', 'simon']
    notas = [99, 65, 76, 45, 76, 89, 90]
    workbook = xlsxwriter.Workbook("notas.xlsx")
    worksheet = workbook.add_worksheet() #sin esto no agrega nada jsjsjs
    bold = workbook.add_format({"bold": True})
    worksheet.set_column("A:A", 100)
    worksheet.write(0, 0, 'Introduccion a la Programacion', bold) #bold esta declarado arriba
    worksheet.write(1, 0, 'Estudiante', bold) #bold esta declarado arriba
    worksheet.write(1, 1, 'Nota')
    fila = 2
    for i in estudiantes:
        worksheet.write(fila, 0, i) #el el numero fila columna 0 se ingresa el valor de i
        worksheet.write(fila, 1, notas[estudiantes.index(i)])#con esto te moves en la otra lista con el indice (index) de la primera lista
        fila += 1 #pasa a la siguiente fila
        
    workbook.close()#sin este cerrar daria error de acceso al archivo al intentar de nuevo jsjsj
    
guardar_notas()
