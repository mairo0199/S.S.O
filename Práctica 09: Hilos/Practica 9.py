import tkinter as tk
from tkinter import PhotoImage

def cargar_imagen(ruta, escala):
    try:
        imagen = PhotoImage(file=ruta)
        imagen = imagen.subsample(escala)
        return imagen
    except tk.TclError:
        print(f"Error al cargar la imagen: {ruta}")
        return None

root = tk.Tk()
root.title("Movimiento simultáneo de dos imágenes")
root.geometry("800x800")

canvas = tk.Canvas(root, width=800, height=800, bg="white")
canvas.pack()
image1 = cargar_imagen(r"C:\Users\Usuario\Desktop\Universidad\S.S.O\patricio.png", 2)
image2 = cargar_imagen(r"C:\Users\Usuario\Desktop\Universidad\S.S.O\bob.png", 2)

if image1 and image2:
    canvas.image1 = image1
    canvas.image2 = image2

    img1 = canvas.create_image(10, 10, anchor='nw', image=image1)
    img2 = canvas.create_image(10, 60, anchor='nw', image=image2)

    x1, y1 = 10, 10
    x2, y2 = 10, 60

    def mover_imagenes():
        global x1, y1, x2, y2

        x1 += 5  # Mover de izquierda a derecha
        if x1 > 400:  # Vuelve al inicio cuando alcanza el borde derecho
            x1 = 10
        canvas.coords(img1, x1, y1)

        y2 += 5  # Mover de arriba hacia abajo
        if y2 > 400:  # Vuelve al inicio cuando alcanza el borde inferior
            y2 = 60
        canvas.coords(img2, x2, y2)

        root.after(50, mover_imagenes)

    mover_imagenes()
else:
    print("Una o ambas imágenes no se pudieron cargar. Verifica las rutas.")

root.mainloop()

