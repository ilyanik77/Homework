# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
	    этого абв текста все вабвс слова, содерабващие содержащие "абв"'
	
def Deletion(text):
	my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
	return " ".join(my_text)
	
my_text = Deletion(text)
print(my_text)