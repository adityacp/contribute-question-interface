from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


question_status_choice = (
        (1, "approved"),
        (0, "unseen"),
        (-1, "discarded"),
        )

level = (
        (1, "easy"),
        (2, "medium"),
        (3, "difficult"),
        )

rating_choice = (
        (1, "Poor"),
        (2, "Average"),
        (3, "Good"),
        (4, "Verygood"),
        (5, "Excellent"),
        )
types = (
        (1, "integer"),
        (2, "float"),
        (3, "string"),
        (4, "boolean"),
        )

originality = (
        ("original", "Original Question"),
        ("adapted", "Adapted Question"),
        )


class Question(models.Model):
    """Question for a quiz."""

    # A one-line summary of the question.
    summary = models.CharField(max_length=256)

    # The question text, should be valid HTML.
    description = models.TextField()

    # Number of points for the question.
    points = models.FloatField(default=1.0)

    # The language for question.
    language = models.CharField(max_length=24,
                                default="python")

    # The type of question.
    type = models.CharField(max_length=24, default="code")

    # user for particular question
    user = models.ForeignKey(User, related_name="user")

    # solution for question
    solution = models.TextField()

    # If the question is cited
    citation = models.TextField(blank=True)

    # originality of the question
    originality = models.CharField(max_length=24, choices=originality, default="original")

    def __str__(self):
        return  self.text
    
    def approve(self):
        self.status=1
    
    def disapprove(self):
        self.status=0


class TestCase(models.Model):
    question = models.ForeignKey(Question, blank=True, null=True)
    type = models.CharField(max_length=24, default="stdiobasedtestcase")

class StdIOBasedTestCase(TestCase):
    expected_input = models.TextField(default=None, blank=True, null=True)
    expected_output = models.TextField(default=None)
    weight = models.IntegerField(default=1.0)

    def get_field_value(self):
        return {"test_case_type": "stdiobasedtestcase",
                "expected_output": self.expected_output,
                "expected_input": self.expected_input,
                "weight": self.weight}

    def __str__(self):
        return u'StdIO Based Testcase | Exp. Output: {0} | Exp. Input: {1}'.\
            format(
                self.expected_output, self.expected_input
            )

    
    
    def __str__(self):
        return str(self.id)
    

class Rating(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    rate = models.IntegerField(default=3, choices=rating_choice)
    
    def __str__(self):  
        return str(self.user)
        
    class Meta:
        unique_together = ('user', 'question',) 

class Review(models.Model):
    reviewer = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    comments = models.CharField(max_length=24, choices=level)
    
    def __str__(self):  
        return str(self.reviewer)
    
    def update_review(self,new_comments):
        self.comments=new_comments
    #class Meta:
    #   unique_together = ('reviewer', 'question',) 
