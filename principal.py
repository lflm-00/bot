from BD.conexion import DAO
import funciones
def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("============= Menù de administrador ============")
            print("1    Listar cursos :     ")
            print("2    Registrar curso :   ")
            print("3    Actualizar curso :  ")
            print("4    Eliminar curso :    ")
            print("5    test :              ")
            print("6 salir     :            ")
            print("================================================")
            opcion = int(input("Seleccione una opciòn : "))

            if opcion <1 or opcion > 6 :
                print("Seleccione una opciòn valida :   ")
            elif opcion == 6 :
                continuar = False
                print("Hàsta la pròxima luis , recuerda tomar awita :D")
                break
            else : 
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                funciones.listarCursos(cursos)
            else:
                print("No se encontraron cursos")
        except:
            print("Ocurrio un error")

    elif opcion == 2:
        curso = funciones.pedirDatosRegistro()
        try:
            dao.registrarCurso(curso)
        except :
            print("Ocurrio un error")
    elif opcion == 3:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0 :
                curso = funciones.pedirDatosActualizacion(cursos)
                if curso :
                    dao.actualizarCurso(curso)


                else :
                    print("Codigo de curso no encontrado ...\n")
            else :
                    print("Codigo de curso no encontrado ...\n")
        except :
            print("Ocurrio un error")
    elif opcion == 4:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0 :
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not(codigoEliminar == ""):
                    dao.eliminarCurso(codigoEliminar)
                else :
                    print("Codigo de curso no encontrado ...\n")
        except :
            print("Ocurrio un error")

    elif opcion == 5:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0 :
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not(codigoEliminar == ""):
                    dao.eliminarCurso(codigoEliminar)
                else :
                    print("Codigo de curso no encontrado ...\n")
        except :
            print("Ocurrio un error")

    else : 
        print("Opciòn no vàlida ...")
       



menuPrincipal()