from django.contrib.auth.models import User
from django.db import models


class Proposal(models.Model):
    # TODO: Move choices to Presentation model
    TALK = 'talk'
    WORKSHOP = 'workshop'
    PANEL = 'panel'
    PRESENTATION_TYPE_CHOICES = (
        (TALK, 'Talk'),
        (WORKSHOP, 'Workshop'),
        (PANEL, 'Panel'),
    )

    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
    AUDIENCE_LEVEL_CHOICES = (
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    )

    speaker = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='proposals')
    # TODO
    # presentation = models.OneToOneField('schedule.Presentation',
    #                                     on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=100)
    description = models.TextField()
    abstract = models.TextField()

    presentation_type = models.CharField(max_length=30,
                                         choices=PRESENTATION_TYPE_CHOICES)
    audience_level = models.CharField(max_length=30,
                                      choices=AUDIENCE_LEVEL_CHOICES)
    # TODO
    # category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    duration = models.DurationField()
    is_accepted = models.NullBooleanField(null=True)

    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, editable=False)

    def __str__(self):
        return self.title

