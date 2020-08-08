from app.api.v2 import course


# from app.api.v2 import user, token, course, resource, answer, question, discussion, topic_answer, schedule, assignment

def create_api_v2(api):
    api.add_resource(course.CourseViews, '/v2/courses/<pk>', '/v2/courses')
