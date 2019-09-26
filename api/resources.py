from tastypie.resources import ModelResource
from tastypie.constants import ALL
from api.models import Course
class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'course'
        filtering = {
            "distributor": ALL,
            "name": ALL,
            "description": ALL,
            "organization": ALL,
            "org_link": ALL,
            "start_date": ALL,
            "end_date": ALL,
            "course_id": ALL,
            "image": ALL,
            "video": ALL,
            "modules_type": ALL, 
            "modules_number": ALL,
            "avg_length": ALL,
            "length": ALL,
            "code": ALL,
            "deadlines": ALL,
            "post_entrance": ALL,
            "sync": ALL,
            "payment": ALL,
        }