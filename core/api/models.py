from django.db import models
from django.utils.text import slugify

from django.contrib.auth import get_user_model
User = get_user_model()


class Raffle(models.Model):
    name = models.CharField(max_length=257)
    slug = models.SlugField(max_length=384, verbose_name='Slug', null=True)
    max_number = models.BigIntegerField()
    raffle_image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_tickets(self) -> list:
        '''
                Retorna os tickets referentes à Rifa
        '''
        return Ticket.objects.filter(raffle=self)

    def draw_prizes(self) -> int:
        '''
                Sorteia um número ganhador da rifa
        '''
        pass

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Raffle, self).save(*args, **kwargs)



class Campaign(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='responsavel')
    raffle = models.ForeignKey(
        Raffle, on_delete=models.CASCADE, related_name='raffle_campaign')

    def __str__(self):
        return f'Campanha {self.raffle}'


class Ticket(models.Model):
    number = models.BigIntegerField()
    raffle = models.ForeignKey(
        Raffle, on_delete=models.CASCADE, related_name='raffle_ticket')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='participante')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'Ticket: {number} da {self.raffle}'


class Prize(models.Model):
    prize_name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    prize_image = models.ImageField(blank=True, null=True)
    raffle = models.ForeignKey(
        Raffle, on_delete=models.CASCADE, related_name='raffle_prize')

    def __str__(self):
        return self.prize_name
