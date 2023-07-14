def obtener_numero_cabalistico(nombre):
    asignacion_cabalistica = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 10, 'K': 20, 'L': 30, 'M': 40, 'N': 50, 'O': 60, 'P': 70, 'Q': 80,
        'R': 90, 'S': 100, 'T': 200, 'U': 300, 'V': 400, 'W': 500, 'X': 600,
        'Y': 700, 'Z': 800
    }

    nombre = nombre.upper()
    nombre_sin_repeticiones = ''.join(dict.fromkeys(nombre))
    numero_cabalistico = 0

    for letra in nombre_sin_repeticiones:
        if letra in asignacion_cabalistica:
            numero_cabalistico += asignacion_cabalistica[letra]

    return numero_cabalistico


def generar_explicacion(numero_cabalistico):
    explicaciones = {
        1: "El número 1 representa individualidad y liderazgo. Es un número que destaca la autosuficiencia y la confianza en uno mismo.",
        2: "El número 2 simboliza la dualidad y la cooperación. Representa la armonía y la necesidad de equilibrio y colaboración en la vida.",
        3: "El número 3 representa la creatividad y la expresión. Es un número asociado con la comunicación y el optimismo.",
        4: "El número 4 representa la estabilidad y la manifestación concreta. Es considerado un número de fundamento, simbolizando los cuatro elementos primarios y las cuatro direcciones cardinales, brindando estructura y equilibrio en el mundo material.",
        5: "El número 5 representa la libertad y la conexión con lo divino. Es considerado un número de expansión y espiritualidad, simbolizando la capacidad de trascender las limitaciones terrenales y alcanzar un nivel más elevado de conciencia y percepción espiritual.",
        6: "El número 6 representa la armonía y la integración. Es considerado un número de equilibrio y belleza, simbolizando la unión entre lo divino y lo humano, así como la integración de las polaridades para lograr la plenitud y la perfección espiritual.",
        7: "El número 7 representa la perfección y la totalidad. Es considerado un número sagrado y poderoso, simbolizando la conexión con lo divino y el cumplimiento espiritual. Representa la manifestación de la creación en su plenitud y el descanso divino después de la obra completada.",
        8: "El número 8 representa la trascendencia y la superación de los límites. Es considerado un número de plenitud y poder espiritual, simbolizando la expansión más allá de los confines terrenales hacia lo infinito y lo eterno. Representa la conexión con niveles superiores de conciencia y la capacidad de alcanzar estados elevados de iluminación.",
        9: "El número 9 representa la finalización y la culminación de un ciclo. Es considerado un número de realización y sabiduría, simbolizando la integridad espiritual y el logro de la plenitud. Representa el punto de culminación antes de comenzar un nuevo ciclo de transformación y crecimiento.",
        0: "El número 0 (cero) no tiene una representación específica en la Cábala judía. Sin embargo, en algunos enfoques modernos de la Cábala, el número 0 puede simbolizar el potencial infinito y la conexión con la Fuente Divina, representando el estado de unidad y trascendencia más allá de los límites numéricos convencionales."
    }

    explicaciones_individuales = []

    if numero_cabalistico < 10:
        if numero_cabalistico in explicaciones:
            explicaciones_individuales.append(explicaciones[numero_cabalistico])
    else:
        for digito in str(numero_cabalistico):
            digito = int(digito)
            if digito in explicaciones:
                explicaciones_individuales.append(explicaciones[digito])

    return explicaciones_individuales


print("\n--- Bienvenido al programa de Números Cabalísticos ---\n")

nombre = input("Ingresa un nombre: ")
print()

numero_cabalistico = obtener_numero_cabalistico(nombre)
explicaciones = generar_explicacion(numero_cabalistico)

print(f"El número cabalístico del nombre '{nombre}' es: {numero_cabalistico}\n")

equivalencia_yiddish = f"La equivalencia lingüística en yiddish del nombre '{nombre}' es: {nombre.lower()}"
print(equivalencia_yiddish)
print()

if explicaciones:
    print("Explicaciones:")
    explicaciones_combinadas = ' '.join(explicaciones)
    print(explicaciones_combinadas)
    print()
else:
    print("No se encontró una explicación para ese número.")
