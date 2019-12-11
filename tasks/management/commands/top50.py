# for u in User.objects.all():
# 	for t in u.tasks.all():
# 		print(u, t)

from django.contrib.auth.models import User

from django.core.management import BaseCommand

from tasks.models import TodoItem


def all_completed():
	completed_count = 0
	for u in User.objects.all():
		for t in u.tasks.all():
			if t.is_completed:
				completed_count += 1
	print("completed tasks:", completed_count)

def sorted_all():
	unsorted_dict = {}
	for t in User.objects.all():
		unsorted_dict[t.username] = len(t.tasks.all())
	print(sorted(unsorted_dict.items(), key = lambda kv:(kv[1], kv[0])))
	





class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		# print(dir(User))

		u = User.objects.get(pk='109')
		# print(dir(u))
		# print(u.username)
		# print(len(u.tasks.all()))

		# for t in u.tasks.all():
		# 	print(t.is_completed)

		# for u in User.objects.all():
			# for t in u.tasks.all():
			# 	print(u, t)

		# all_completed()
		sorted_all()

	