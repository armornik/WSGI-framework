# Use as in Django
from version_as_django.views_as_django import About, CategoryList, CreateCategory, CreateCourse, CoursesList, Index, StudyPrograms

# Set of bindings: path-controller
routes = {
    '/': Index(),
    '/about/': About(),
    '/category-list/': CategoryList(),
    '/create-category/': CreateCategory(),
    '/create-course/': CreateCourse(),
    '/courses-list/': CoursesList(),
    '/study_programs/': StudyPrograms(),
}
