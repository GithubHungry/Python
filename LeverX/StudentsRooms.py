students = [
    {
        'id': 1,
        'name': 'Nikita #1',
        'room': 1
    },
    {
        'id': 2,
        'name': 'Nikita #2',
        'room': 1
    },
    {
        'id': 3,
        'name': 'Nikita #3',
        'room': 2
    },
    {
        'id': 4,
        'name': 'Nikita #4',
        'room': 2
    },
    {
        'id': 5,
        'name': 'Nikita #5',
        'room': 2
    },
    {
        'id': 6,
        'name': 'Nikita #6',
        'room': 2
    },
    {
        'id': 7,
        'name': 'Nikita #7',
        'room': 3
    }
]

rooms = [
    {
        'id': 1,
        'name': 'Room #1',
        'students': []
    },
    {
        'id': 2,
        'name': 'Room #2',
        'students': []
    },
    {
        'id': 42,
        'name': 'Room #42',
        'students': []
    }
]


def solution(students: list, rooms: list) -> list:
    """Complete field 'students' from students"""
    # Создание хеш-таблицы вида ('id(student)':'id(room)')
    dictst = {}
    for student in students:
        for k, v in student.items():
            if k == 'id':
                dictst[student[k]] = student['room']
    # Обход списка с комнатами
    for room in rooms:
        for k, v in room.items():
            if k == 'id':
                for key, val in dictst.items():
                    if v == val:
                        room['students'].append(key)
            break
    return rooms


print(solution(students, rooms))
