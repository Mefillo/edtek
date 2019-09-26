from django.db import models, connection



# model of course
class Course (models.Model):
    BOOL_CHOICES = ((True, 'Да'), (False, 'Нет'))

    # Url to Image of the course
    detail_image = models.URLField(null = True)

    # Url to Image of the course
    anons_image = models.URLField(null = True)

    # Unique id of the course
    mnemocode = models.CharField(max_length = 100, unique = True, null = True)

    #Type of description
    detail_text_type = models.CharField(max_length = 10, default = 'html')

    #Type of description
    preview_text_type = models.CharField(max_length = 10, default = 'html')

    # name of a course
    name = models.CharField(max_length = 70, default = 'Не указано название')

    # name of the course distributor
    distributor = models.CharField(max_length = 70, null = True)

    # name of discipline
    discipline = models.CharField(max_length = 70, null = True)
    
    # Short description of the course
    description = models.TextField(null = True, default='Не приведено краткого описания')

    #Long description of the course
    long_description = models.TextField(null = True)
 
    # the price for the whole course
    price = models.CharField(max_length = 20, default = 'Бесплатно')

    # currency of a price course
    currency = models.CharField(max_length = 10, null = True, default = 'null')

    # organization that provide this course
    organization = models.CharField(max_length = 40, default = 'Частный преподаватель')

    # key words of the course
    key_words = models.CharField(max_length = 200, default = 'auto')

    #key modules of the course
    modules = models.CharField(max_length = 200, default = 'auto')

    #number of modules
    modules_number = models.CharField(max_length = 10, null = True)

    #type of modules
    modules_type = models.CharField(max_length = 50, null = True)

    #Average seminar length
    avg_length = models.CharField(max_length = 200, null = True)

    #Events and special programms
    description = models.TextField(default = 'auto', null = True)

    #Schema of the courses
    schema = models.TextField(null = True)

    #Type of education
    education_type = models.CharField(max_length = 50, null = True)

    #Recommended age
    age = models.IntegerField(null = True,  default=0)

    #Course Code
    code = models.IntegerField(default = 0)

    #Terms of copyright
    terms = models.CharField(max_length = 200, null = True)

    #Entrance test
    test = models.CharField(choices=BOOL_CHOICES, default = 'Нет', max_length = 3)

    #Restriction of amount of perticipators
    amount_restrictions = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Groups formed by level of preparation
    level_counts = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')
    
    #Teachers present
    teachers_present = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Tutors present
    tutors_present = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Facilitators present
    facilitators_present = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Feedback through process of education
    feedback = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Co-education allowed
    co_ed = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Practice lesson
    practice = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Forums, discussions
    forums = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Possibility to individualize
    individualization = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #supports disabled 
    disabled = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Webinars, video-lessons
    webinars = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Education analytics
    analytics = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Deadlines provided
    deadlines = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    #Ability to start after beginning
    post_entrance = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    # The way of training materials
    training_materials = models.CharField(max_length = 200, null = True)

    #Supported browsers
    browsers = models.CharField(max_length = 200, null = True)

    #Supported technologies
    technologies = models.CharField(max_length = 200, null = True)

    #Requsites of speakers
    requsites = models.CharField(max_length = 200, null = True)

    #Payment options
    payment = models.CharField(max_length = 200, default = 'auto')

    #Operation System allowed
    os_list = models.CharField(max_length = 200, null = True)

    #Tools for education
    tools = models.CharField(max_length = 200, null = True)

    #Peripherals
    peripherals = models.CharField(max_length = 200, null = True)

    # authors that participated in creation of this course
    authors = models.CharField(max_length = 200, null = True, default = 'Не указан автор')

    #degree of an author
    author_degree = models.CharField(max_length = 200, null = True)

    #author`s awards
    author_awards = models.CharField(max_length = 200, null = True)

    #author`s position
    author_position = models.CharField(max_length = 200, null = True)

    #Amount of estimated work
    valued_work = models.CharField(max_length = 5, null = True)

    # True/False is certification provided after compliting the course
    certification = models.CharField(max_length = 3, choices=BOOL_CHOICES, null = True, default = 'Нет')

    # Language provided for education on the course
    language = models.CharField(max_length = 20, null = True, default = 'Не указан язык обучения')

    # Link to the course on host site
    org_link = models.URLField(null = True, default = 'AUTO', unique = True)

    # Start of enrollement date
    start_date = models.CharField(max_length = 30, null = True)

    # End of enrolement date
    end_date = models.CharField(max_length = 30, null = True)

    #Length of the whole course
    length = models.CharField(max_length = 100, default = 'auto')

    #Education type (sync)
    sync = models.CharField(max_length = 100, default = 'auto')

    #Type of assessment
    assessmet = models.CharField(max_length = 100, null = True)

    #LMS integration
    lms = models.CharField(max_length = 100, default = 'auto')

    # Unique id of the course
    course_id = models.CharField(max_length = 100, unique = True, null = True)

    #requarements to enroll
    prerequesetes = models.CharField(max_length = 100, default = 'auto')

    # Url to Video of the course
    video = models.URLField(null = True)

    #Interests satisfaction
    interests = models.CharField(max_length = 100, default = 'auto')

    #Skills provided
    skills = models.CharField(max_length = 100, default = 'auto')

    #Ways to intact
    ways = models.CharField(max_length = 100, default = 'auto')

