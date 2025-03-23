from django.db import models
from django.urls import reverse
from django.utils import timezone

class BrieftDraft(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/", blank=True)
    author = models.CharField(max_length=255, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "ICO"
        verbose_name_plural = "ICO"
    



class Nature(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    content = models.TextField(blank=True, null=True, verbose_name="Текс статьи")
    photo = models.ImageField(upload_to="photos/nature/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    # def get_absolute_url(self):
    #     return reverse("single-nature", kwargs={"post_id": self.pk})
    
    class Meta:
        verbose_name = "Экология"
        verbose_name_plural = "Экология"
        # ordering = ['time_create', 'title']



class Contact(models.Model):
    crump_title_contact = models.CharField(max_length=255, blank=True, null=True)
    crump_subtitle_contact = models.CharField(max_length=255, blank=True, null=True)
    crump_photo_contact = models.ImageField(upload_to="photos/contact/%Y/%m/", blank=True)
    form_title_contact = models.CharField(max_length=255, blank=True, null=True)
    form_subtitle_contact = models.CharField(max_length=255, blank=True, null=True)
    address_contact = models.CharField(max_length=255, blank=True, null=True)
    worktime_contact = models.CharField(max_length=255, blank=True, null=True)
    cont_contact = models.CharField(max_length=255, blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.crump_title_contact
    
    class Meta:
        verbose_name = "Контакты 1"
        verbose_name_plural = "Контакты 1"
        ordering = ['time_create', 'crump_title_contact']




class Contact_1(models.Model):
    title_banner = models.CharField(max_length=255, blank=True, null=True)
    crump_subtitle_contact = models.CharField(max_length=255, blank=True, null=True)
    photo_banner = models.ImageField(upload_to="photos/contact/%Y/%m/", blank=True, null=True)
    form_title_contact = models.CharField(max_length=255, blank=True, null=True)
    form_subtitle_contact = models.CharField(max_length=255, blank=True, null=True)
    address_contact = models.TextField(max_length=255, blank=True, null=True)
    worktime_contact = models.TextField(max_length=255, blank=True, null=True)
    cont_contact = models.TextField(max_length=255, blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title_banner
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
    


class Video(models.Model):
    title_block = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок блока")
    subtitle_block = models.TextField(blank=True, null=True, verbose_name="Подзаголовок блока")
    title_video = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название видео")
    text_video = models.TextField(blank=True, null=True, verbose_name="Описание видео")
    author = models.CharField(max_length=255, blank=True, null=True, verbose_name="Автор")
    link_frame_video = models.TextField(blank=True, null=True, verbose_name="Ссылка на фрейм")
    link_service = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ссылка на сервис")
    width_video = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ширина видео")
    height_video = models.CharField(max_length=255, blank=True, null=True, verbose_name="Высота видео")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title_block
    
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        ordering = ['time_create', 'title_block']



class About(models.Model):
    title_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    subtitle_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок")
    photo_banner = models.ImageField(upload_to="photos/about/%Y/%m/", blank=True, null=True, verbose_name="Изображение баннера")
    title_block_left = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок левого блока")
    title_block_right = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок правого  блока")
    title_call = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок связь")
    text_call = models.TextField(blank=True, null=True, verbose_name="Текст связи")
    title_price = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок цены")
    text_price = models.TextField(blank=True, null=True, verbose_name="Текст текст цены")
    title_order = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок заказа")
    text_order = models.TextField(blank=True, null=True, verbose_name="Текст заказа")
    title_qly = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок кач-ва")
    text_qly = models.TextField(blank=True, null=True, verbose_name="Текст кач-ва")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    is_home = models.BooleanField(default=False, verbose_name="Публикация на главной")

    def __str__(self):
        return self.title_banner
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
        ordering = ['time_create', 'title_banner']



class Team(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    profession = models.CharField(max_length=255, blank=True, null=True, verbose_name="Профессия")
    photo = models.ImageField(upload_to="photos/%Y/%m/", blank=True, verbose_name="Фото")
    author = models.CharField(max_length=255, blank=True, verbose_name="Автор")
    telegram = models.CharField(max_length=255, blank=True, null=True, verbose_name="telegram")
    vk = models.CharField(max_length=255, blank=True, null=True, verbose_name="vk")
    whatsapp = models.CharField(max_length=255, blank=True, null=True, verbose_name="whatsapp")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команда"


class Diamond(models.Model):
    # title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок страницы")
    # subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок страницы")
    # image = models.ImageField(upload_to="photos/diamonds/%Y/%m/", blank=True, verbose_name="Фото страницы")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок")
    content = models.TextField(blank=True, null=True, verbose_name="Текст блока")
    photo = models.ImageField(upload_to="photos/diamonds/%Y/%m/", blank=True, verbose_name="Фото")
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name="Позиция блока справа")
    dop = models.TextField(blank=True, null=True, verbose_name="Дополнительно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    is_home = models.BooleanField(default=False, verbose_name="Вывод на главную страницу")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Бриллианты"
        verbose_name_plural = "Бриллианты"


class Clip(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок")
    content = models.TextField(blank=True, null=True, verbose_name="Текст блока")
    photo = models.ImageField(upload_to="photos/diamonds/%Y/%m/", blank=True, verbose_name="Фото")
    position = models.BooleanField(default=False, verbose_name="Позиция блока справа")
    dop = models.TextField(blank=True, null=True, verbose_name="Дополнительно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Запонки и зажимы"
        verbose_name_plural = "Запонки и зажимы"


class Weddingrings(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок")
    content = models.TextField(blank=True, null=True, verbose_name="Текст блока")
    photo = models.ImageField(upload_to="photos/weddingrings/%Y/%m/", blank=True, verbose_name="Фото")
    position = models.BooleanField(default=False, verbose_name="Позиция блока справа")
    dop = models.TextField(blank=True, null=True, verbose_name="Дополнительно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    is_home = models.BooleanField(default=False, verbose_name="Публикация на главной")
          
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Обручальные кольца"
        verbose_name_plural = "Обручальные кольца"


class Earring(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок")
    content = models.TextField(blank=True, null=True, verbose_name="Текст блока")
    photo = models.ImageField(upload_to="photos/earrings/%Y/%m/", blank=True, verbose_name="Фото")
    position = models.BooleanField(default=False, verbose_name="Позиция блока справа")
    dop = models.TextField(blank=True, null=True, verbose_name="Дополнительно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Серьги, подвески, кулоны"
        verbose_name_plural = "Серьги, подвески, кулоны"


class Amulets(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок")
    content = models.TextField(blank=True, null=True, verbose_name="Текст блока")
    photo = models.ImageField(upload_to="photos/earrings/%Y/%m/", blank=True, verbose_name="Фото")
    position = models.BooleanField(default=False, verbose_name="Позиция блока справа")
    dop = models.TextField(blank=True, null=True, verbose_name="Дополнительно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Украшения - обереги"
        verbose_name_plural = "Украшения - обереги"



class Ring(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок")
    content = models.TextField(blank=True, null=True, verbose_name="Текст блока")
    photo = models.ImageField(upload_to="photos/earrings/%Y/%m/", blank=True, verbose_name="Фото")
    man = models.BooleanField(default=False, verbose_name="Мужские")
    women = models.BooleanField(default=False, verbose_name="Женские")
    position = models.BooleanField(default=False, verbose_name="Позиция блока справа")
    dop = models.TextField(blank=True, null=True, verbose_name="Дополнительно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
    
    class Meta:
        verbose_name = "Кольца, перстни, печатки"
        verbose_name_plural = "Кольца, перстни, печатки"


class CallbackRequest(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", blank=True, max_length=20)
    email = models.EmailField("Email", max_length=100)
    message = models.TextField("Сообщение", max_length=2000)
    created_at = models.DateTimeField("Дата создания", default=timezone.now)
    processed = models.BooleanField("Обработано", default=False)

    def __str__(self):
        return f"{self.name} ({self.email})"
    
    class Meta:
        verbose_name = "Сообщения пользователей"
        verbose_name_plural = "Сообщения пользователей"


class Badge(models.Model):
    title_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок баннера")
    subtitle_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок баннера")
    photo_banner = models.ImageField(upload_to="photos/badges/%Y/%m/", blank=True, verbose_name="Фото баннера")
    title_list = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок описаний")
    list1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание 1")
    list2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание 2")
    list3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание 3")
    list4 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание 4")
    dop = models.TextField(blank=True, null=True, verbose_name="Дополнительно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title_banner
    
    class Meta:
        verbose_name = "Нагрудныe знаки"
        verbose_name_plural = "Нагрудныe знаки"


class BadgeFoto(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="photos/badgesfoto/%Y/%m/", blank=True, verbose_name="Фото баннера")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фото для нагрудных знаков"
        verbose_name_plural = "Фото для нагрудных знаков"


class Price(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Наименование")
    au = models.CharField(max_length=255, blank=True, null=True, verbose_name="au")
    ag = models.CharField(max_length=255, blank=True, null=True, verbose_name="ag")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Прейскурант"
        verbose_name_plural = "Прейскурант"


class Cast(models.Model):
    title_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок баннера")
    subtitle_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок баннера")
    photo_banner = models.ImageField(upload_to="photos/cast/%Y/%m/", blank=True, verbose_name="Фото баннера")
    title_list1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок описаний")
    title_list2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок прейскуранта")
    list1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 1")
    list2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 2")
    list3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 3")
    list4 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 4")
    list5 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 5")
    dop = models.TextField(blank=True, null=True, verbose_name="Дополнительно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title_banner
    
    class Meta:
        verbose_name = "Литье"
        verbose_name_plural = "Литье"


class CastFoto(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="photos/cast/%Y/%m/", blank=True, verbose_name="Фото баннера")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фото литья"
        verbose_name_plural = "Фото литья"


class Electroplating(models.Model):
    title_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок баннера")
    subtitle_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок баннера")
    photo_banner = models.ImageField(upload_to="photos/cast/%Y/%m/", blank=True, verbose_name="Фото баннера")
    title_list1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок 1")
    title_list2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок 2")
    list1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 1")
    list2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 2")
    list3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 3")
    list4 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 4")
    list5 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 5")
    dop = models.TextField(blank=True, null=True, verbose_name="Дополнительно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title_banner
    
    class Meta:
        verbose_name = "Гальваника"
        verbose_name_plural = "Гальваника"


class ElectroplatingFoto(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="photos/cast/%Y/%m/", blank=True, verbose_name="Фото баннера")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фото гальваника"
        verbose_name_plural = "Фото гальваника"


class Sketch(models.Model):
    title_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок баннера")
    subtitle_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок баннера")
    photo_banner = models.ImageField(upload_to="photos/sketches/%Y/%m/", blank=True, verbose_name="Фото баннера")
    title_list1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок 1")
    title_list2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок 2")
    list1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 1")
    list2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 2")
    list3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 3")
    list4 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 4")
    list5 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 5")
    desc = models.TextField(blank=True, null=True, verbose_name="Описание")
    dop = models.TextField(blank=True, null=True, verbose_name="Дополнительно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title_banner
    
    class Meta:
        verbose_name = "Эскизы"
        verbose_name_plural = "Эскизы"


class SketchFoto(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="photos/cast/%Y/%m/", blank=True, verbose_name="Фото баннера")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    is_home = models.BooleanField(default=False, verbose_name="Публикация на главной")
          
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фото эскизы"
        verbose_name_plural = "Фото эскизы"


class Modeled(models.Model):
    title_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок баннера")
    subtitle_banner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подзаголовок баннера")
    photo_banner = models.ImageField(upload_to="photos/models/%Y/%m/", blank=True, verbose_name="Фото баннера")
    title_list1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок 1")
    title_list2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок 2")
    list1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 1")
    list2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 2")
    list3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 3")
    list4 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 4")
    list5 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Прейскурант 5")
    desc = models.TextField(blank=True, null=True, verbose_name="Описание")
    dop = models.TextField(blank=True, null=True, verbose_name="Дополнительно")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
          
    def __str__(self):
        return self.title_banner
    
    class Meta:
        verbose_name = "3D модели"
        verbose_name_plural = "3D модели"


class ModeledFoto(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="photos/models/%Y/%m/", blank=True, verbose_name="Фото баннера")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    is_home = models.BooleanField(default=False, verbose_name="Публикация на главной")
          
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фото 3D модели"
        verbose_name_plural = "Фото 3D модели"


class ModeledVideo(models.Model):
    title_block = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок блока")
    subtitle_block = models.TextField(blank=True, null=True, verbose_name="Подзаголовок блока")
    title_video = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название видео")
    text_video = models.TextField(blank=True, null=True, verbose_name="Описание видео")
    author = models.CharField(max_length=255, blank=True, null=True, verbose_name="Автор")
    link_frame_video = models.TextField(blank=True, null=True, verbose_name="Ссылка на фрейм")
    link_service = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ссылка на сервис")
    width_video = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ширина видео")
    height_video = models.CharField(max_length=255, blank=True, null=True, verbose_name="Высота видео")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title_block
    
    class Meta:
        verbose_name = "Видео 3D Модели"
        verbose_name_plural = "Видео 3D Модели"
        ordering = ['time_create', 'title_video']
