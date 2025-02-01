from classes_professional.Mixins.Enumerable import Enumerable
from classes_professional.Mixins.Lesson import Lesson


class Course(Enumerable):
    def __init__(self, lessons):
        self.lessons = lessons

    def get_iterator(self):
        return self.lessons


lessons = [
    # Второй параметр это продолжительность урока в минутах
    Lesson('react start', 3),
    Lesson('react component', 9),
    Lesson('react lifecycle', 2),
    Lesson('redux', 4),
]


# Course() использует миксину Enumerable
course = Course(lessons)

lesson = course.max_by(lambda less: less.get_duration())
# print(lesson)  # ('react component', 9)
print(lesson.get_duration())