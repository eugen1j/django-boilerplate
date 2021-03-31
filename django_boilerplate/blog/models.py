from django.db import models
from django.utils.translation import gettext_lazy as _


class BlogTag(models.Model):
    class Meta:
        verbose_name = _("blog tag")
        verbose_name_plural = _("blog tags")

    name = models.CharField(_("Name"), max_length=255)
    color = models.CharField(_("Color"), max_length=255)

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    class Meta:
        verbose_name = _("blog category")
        verbose_name_plural = _("blog categories")

    name = models.CharField(_("Name"), max_length=255)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    class Meta:
        verbose_name = _("blog post")
        verbose_name_plural = _("blog posts")

    title = models.CharField(_("Title"), max_length=255)
    short_description = models.CharField(_("Short description"), max_length=255)
    content = models.TextField(_("Content"))
    category = models.ForeignKey(
        BlogCategory,
        models.PROTECT,
        null=True,
        related_name="posts",
        verbose_name=_("Blog category")
    )
    tags = models.ManyToManyField(
        BlogTag,
        related_name="posts",
        verbose_name=_("Tags"),
    )

    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(
        _("Updated at"), auto_now=True, editable=False)

    def __str__(self):
        return self.title


class BackgroundImage(models.Model):
    class Meta:
        verbose_name = _("background image")
        verbose_name_plural = _("background images")

    image = models.ImageField(
        _("Image"), width_field='image_width', height_field='image_height',
        upload_to="blog/background/")
    image_width = models.IntegerField(
        _("Image width"), editable=False)
    image_height = models.IntegerField(
        _("Image height"), editable=False)

    post = models.OneToOneField(
        BlogPost, models.CASCADE,
        related_name="background_image",
        verbose_name=_("Blog post"),
    )

    def __str__(self):
        return self.image.name
