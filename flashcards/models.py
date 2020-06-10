from django.db import models

class FlashCards(models.Model):
    flash_title=models.CharField(max_length=40)
    flash_course=models.CharField(max_length=40)
    flash_body=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all_flash_cards(cls):
        flash_cards=FlashCards.objects.all()
        return flash_cards
    
    @classmethod
    def get_single_flash_card(cls, flash_id):
        flash_card=FlashCards.objects.get(id=flash_id)
        return flash_card
    
    def delete_flash_card(self):
        self.delete()
    
    def save_flash_card(self):
        self.save()

    def __str__(self):
        return self.flash_title

class Courses(models.Model):
    course_name=models.CharField(max_length=60)

    def __str__(self):
        return self.course_name