from django.db import models
# from django.contrib.auth import us


class Articles(models.Model):
    title = models.CharField('Название', max_length=64)
    author = models.CharField('Автор', max_length=64)
    full_text = models.TextField('Статья')
    # liked = models.ManyToManyField(default=None, related_name='likes')

    def __str__(self):
        return self.title

    # def num_likes(self):
    #     return self.liked.all().count()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Like(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)

# LIKE_CHOICES = (
#     ('Like', 'Like'),
#     ('Unlike', 'Unlike')
# )
#
#
# class Like(models.Model):
#     article = models.ForeignKey(Articles, on_delete=models.CASCADE)
#     value = models.CharField(choices=LIKE_CHOICES, max_length=8)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.article}-{self.value}"
