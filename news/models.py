from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class News_post(models.Model):
	title = models.CharField('Название новости', max_length=50)
	short_description = models.CharField('Краткое описание новости', max_length=200)
	text = models.TextField('Новость')
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Автор')
	pub_date = models.DateTimeField('Дата публикации')




	def __str__(self):
		return self.title

	def __str__(self):
		return self.short_description

	def __str__(self):
		return self.text

	def __str__(self):
		return self.author

	def __int__(self):
		return self.pub_date





	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'