def listarCursos(cursos):
    print("Cursos : ")
    contador =1
    for cur in cursos :
        datos = "{0} . Codigo : {1} │ Nombre : {2} ({3} Crèditos)"
        print(datos.format(contador,cur[0] , cur[1] , cur[2]))
        contador = contador + 1
    print(" ")


def pedirDatosRegistro():
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = input("Ingrese codigo : ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else :
            print("Còdigo incorrecto debe tener 6 Dìgitos : ")

    nombre = input("Ingrese Nombre : ")

    creditosCorrecto = False
    while(not creditosCorrecto):
        creditos = input("Ingrese Creditos : ")
        if creditos.isnumeric():
            if (int(creditos) > 0) :
                creditosCorrecto = True
                creditos =  int(creditos)
            else :
                print("Los crèditos deben ser mayores a 0")
        else : 
            print("Crèditos incorrectos : debe ser un nùmero")

    curso = (codigo, nombre, creditos)
    return curso


def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEditar = int(input("Ingrese Còdigo de curso a Actualizar  ..."))
    for cur in cursos :
        if cur[0] == codigoEditar :
            existeCodigo = True
            break

    if existeCodigo :
        nombre = input("Ingrese Nombre a modificar : ")

        creditosCorrecto = False
        while(not creditosCorrecto):
            creditos = input("Ingrese Creditos a modificar : ")
            if creditos.isnumeric():
                if (int(creditos) > 0) :
                    creditosCorrecto = True
                    creditos =  int(creditos)
                else :
                    print("Los crèditos deben ser mayores a 0")
            else : 
                print("Crèditos incorrectos : debe ser un nùmero")

        curso = (codigoEditar, nombre, creditos)

    else:
        curso = None

    return curso


def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar = int(input("Ingrese Còdigo de curso a eliminar ..."))
    for cur in cursos :
        if cur[0] == codigoEliminar :
            existeCodigo = True
            break
    if not existeCodigo :
        codigoEliminar = ""

    return codigoEliminar