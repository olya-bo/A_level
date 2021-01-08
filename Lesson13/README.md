select course.name as course_name, coach.name as coach_name 
from course 
inner join coach on (course.id = coach.course_id);


select student.name as student_name, course.name as course_name, coach.name as coach_name from course_student inner join student on (student.id = course_student.student_id) inner join course on (course.id = course_student.course_id) inner join coach on (coach.course_id = course_student.course_id);


Добавила таблицу rating c полями value, student_id, coah_id.
В поле value указывается оценка, student_id свзывает оценку со студетом,
coah_id c преподавателем, который поставил эту оценку.

select student.id, student.name as student_name, rating.value as student_value from student full join rating on (student.id = rating.student_id);

select coach.name as coach_name, rating.value as coach_value, student.name as student_name from rating full join coach on (rating.coach_id = coach.id) inner join student on (rating.student_id = student.id);

select coach.name as coach_name, rating.value as coach_value, student.name as student_name from rating inner join coach on (rating.coach_id = coach.id) full join student on (rating.student_id = student.id);