from django.db import models
from django.utils.translation import gettext_lazy as _


class BlogImage(models.Model):
    class Meta:
        verbose_name = _("blog image")
        verbose_name_plural = _("blog images")

    image = models.ImageField(
        _("Image"),
        width_field="image_width",
        height_field="image_height",
        upload_to="blog/",
    )
    image_width = models.IntegerField(_("Image width"), editable=False)
    image_height = models.IntegerField(_("Image height"), editable=False)
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True, editable=False)

    def __str__(self):
        return self.image.name


class BlogTag(models.Model):
    class Meta:
        verbose_name = _("blog tag")
        verbose_name_plural = _("blog tags")

    name = models.CharField(_("Name"), max_length=255)
    color = models.CharField(_("Color"), max_length=255)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

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

    class Status(models.TextChoices):
        DRAFT = "DRAFT", _("Draft")
        EDITING = "EDITING", _("Editing")
        PUBLISHED = "PUBLISHED", _("Published")
        REJECTED = "REJECTED", _("Rejected")

    title = models.CharField(_("Title"), max_length=255)
    short_description = models.CharField(_("Short description"), max_length=255)
    content = models.TextField(_("Content"))
    category = models.ForeignKey(
        BlogCategory,
        models.PROTECT,
        null=True,
        related_name="posts",
        verbose_name=_("Blog category"),
    )
    tags = models.ManyToManyField(
        BlogTag,
        related_name="posts",
        verbose_name=_("Tags"),
    )
    status = models.TextField(_("Status"), choices=Status.choices, default=Status.DRAFT)
    background_image = models.ForeignKey(
        BlogImage,
        models.PROTECT,
        null=True,
        related_name="blog_post",
        verbose_name=_("Background Image"),
    )

    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True, editable=False)

    def __str__(self):
        return self.title
