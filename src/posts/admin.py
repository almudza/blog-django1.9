from django.contrib import admin

# Register your models here.
from .models import Post # ini diambil atau import dari folder posts kemudian dari file models.py

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","updated","timestamp"] #untuk menampilkan daftar  untuk judul,update, dan waktu
	list_editable = ["title"]  # untuk menampilakandaftar untuk mengubah berdasarkan pada judul
	list_display_links = ["updated"]  #untuk menampilkan link display
	list_filter = ["updated","timestamp"] #untuk menampilkan filter waktu update post yang berada di pojok kanan
	search_fields = ["title","content"] #untuk membuat pencarian dengan berdasarkan pada judul dan konten
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)
