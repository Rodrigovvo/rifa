from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


User = get_user_model()


class Raffle(models.Model):
    name = models.CharField(max_length=257, verbose_name='Nome da Rifa')
    slug = models.SlugField(max_length=384, verbose_name='Slug', null=True)
    max_number = models.BigIntegerField(verbose_name='Quantidade Máxima de Ticktes')
    raffle_image = models.ImageField(verbose_name='Imagem', blank=True, null=True)
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)
    ticket_price = models.DecimalField(verbose_name='Preço por ticket', max_digits=6, decimal_places=2)
    start_date = models.DateTimeField(verbose_name='Data de início', auto_now_add=True)
    end_date = models.DateTimeField(verbose_name='Data do sorteio', blank=True, null=True)
    is_finished = models.BooleanField(verbose_name='Finalizado ?', default=False)
    winner = models.BigIntegerField(verbose_name='Ticket vencedor', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_tickets(self) -> list:
        """
        Retorna os tickets referentes à Rifa
        """
        return Ticket.objects.filter(raffle=self)

    def draw_prizes(self) -> int:
        """
        Sorteia um número ganhador da rifa
        """
        if self.winner:
            return self.winner
        else:
            prize_drawn = Ticket.objects.filter(
                raffle=self, is_active=True
            ).order_by('?').first().number
            self.winner = prize_drawn
            self.is_finished = True
            self.save()

            return prize_drawn

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Raffle, self).save(*args, **kwargs)


class Campaign(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='responsavel'
    )
    raffle = models.ForeignKey(
        Raffle, 
        on_delete=models.CASCADE, 
        related_name='raffle_campaign'
    )

    def __str__(self):
        return f'Campanha {self.raffle}'


class Ticket(models.Model):
    number = models.BigIntegerField(verbose_name='Número do Ticket')
    is_active = models.BooleanField(verbose_name='Ticket ativo?', default=False)

    raffle = models.ForeignKey(
        Raffle, 
        on_delete=models.CASCADE,
        verbose_name='Rifa', 
        related_name='raffle_ticket'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Usuário detentor', 
        related_name='participante'
    )

    class Meta:
        unique_together = ['raffle', 'number']

    def __str__(self):
        return f'Ticket: {number} da {self.raffle}'



class Prize(models.Model):
    prize_name = models.CharField(max_length=256, verbose_name='Nome do Prêmio')
    description = models.TextField(verbose_name='Descrição do prêmio', blank=True, null=True)
    prize_image = models.ImageField(verbose_name='Imagem do prêmio', blank=True, null=True)

    raffle = models.ForeignKey(Raffle, 
        on_delete=models.CASCADE, 
        verbose_name='Rifa', 
        related_name='raffle_prize'
    )

    def __str__(self):
        return self.prize_name
