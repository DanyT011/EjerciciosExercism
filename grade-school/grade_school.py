class School:
    """
    Esta función crea una lista a partir de los nombres y grados
    Param
    students
    
    Return
    Lista de todos estudiantes inscritos en un grado
    """
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade

    def roster(self):
        lista = []
        for gr in list(set(self.students.values())):
            lista = lista + [student for student in self.grade(gr)]
        return lista
        
    def grade(self, grade_number):
        return sorted([student for student in self.students if self.students[student] == grade_number])