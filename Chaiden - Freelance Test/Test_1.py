import mysql.connector

koneksi = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "test_freelance"
)
kursor = koneksi.cursor()

kursor.execute("SELECT students.*,course_name FROM students INNER JOIN courses ON students.course_id = courses.course_id WHERE course_name = 'Computer Science'")
array = kursor.fetchall()
kursor.execute("SELECT COUNT(student_id) FROM students INNER JOIN courses ON students.course_id = courses.course_id WHERE course_name = 'Computer Science'")
arraycount = len(array)
for x in array:
    print(x)
print(arraycount)
# for y in arraycount:
#     print(y)