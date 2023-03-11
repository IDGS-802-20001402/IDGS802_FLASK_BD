from db import get_connection

# try:
#     connection = get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute("call get_alumnos()")
#         resulset = cursor.fetchall()
#         for row in resulset:
#             print(row)
# except Exception as e:
#     print('ERROR')

# try:
#     connection = get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute("call get_alumno(%$)", (10,))
#         resulset = cursor.fetchall()
#         for row in resulset:
#             print(row)
# except Exception as e:
#     print('ERROR')



try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("call create_alumno(%s, %s, %s)", ('Laura', 'Marquez', 'laug@gmail.com'))
    connection.commit()
except Exception as e:
    print('ERROR')