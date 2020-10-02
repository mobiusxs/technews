from django.db import models
from django.db.models.expressions import RawSQL

from user.models import User


class ThreadManager(models.Manager):
    def get_queryset(self):
        """Combining multiple aggregations with annotate() will yield the
        wrong results because joins are used instead of subqueries:

        https://docs.djangoproject.com/en/3.1/topics/db/aggregation/#combining-multiple-aggregations

        https://docs.djangoproject.com/en/3.1/ref/models/expressions/#raw-sql-expressions

        Ultimately, the needed query is:

            SELECT
                *,
                (SELECT Sum(vote_threadvote.value) FROM vote_threadvote WHERE thread_thread.id = vote_threadvote.thread_id) AS karma,
                (SELECT Count(comment_comment.id) FROM comment_comment WHERE thread_thread.id = comment_comment.thread_id) AS comment_count
            FROM
                thread_thread
            GROUP BY
                thread_thread.id

        In order to get to this, the subqueries must be completely isolated because `subquery=True` doesn't work.
        Huge deficiency in Django's ORM.
        """

        qs = super().get_queryset()
        return qs.annotate(
            comment_count=RawSQL("""SELECT Count(id) FROM comment_comment WHERE thread_thread.id = comment_comment.thread_id""", ()),
            karma=RawSQL("""SELECT Sum(value) FROM vote_threadvote WHERE thread_thread.id = vote_threadvote.thread_id""", ()),
        )


class Thread(models.Model):
    """Simple temporary Thread model.
    Supports only links for now.
    """

    url = models.URLField()
    text = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = ThreadManager()

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return f'[{self.user.username}] {self.text}'
