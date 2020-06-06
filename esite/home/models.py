from django.http import HttpResponse
from django.db import models
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.admin.edit_handlers import PageChooserPanel, TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from modelcluster.fields import ParentalKey

from esite.colorfield.fields import ColorField, ColorAlphaField
from esite.colorfield.blocks import ColorBlock, ColorAlphaBlock, GradientColorBlock

from esite.api.helpers import register_streamfield_block

from esite.api.models import (
    GraphQLForeignKey,
    GraphQLField,
    GraphQLStreamfield,
    GraphQLImage,
    GraphQLString,
    GraphQLCollection,
    GraphQLEmbed,
    GraphQLSnippet,
    GraphQLBoolean,
    GraphQLSnippet,
)

#from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
#)

# Create your homepage related models here.

@register_snippet
class Button(models.Model):
    button_title = models.CharField(null=True, blank=False, max_length=255)
    #button_id = models.CharField(null=True, blank=True, max_length=255)
    #button_class = models.CharField(null=True, blank=True, max_length=255)
    button_embed = models.CharField(null=True, blank=True, max_length=255)
    button_link = models.URLField(null=True, blank=True)
    button_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('button_title'),
        FieldPanel('button_embed'),
        FieldPanel('button_link'),
        PageChooserPanel('button_page')
    ]

    def __str__(self):
        return self.button_title


#> Header
@register_streamfield_block
class _H_BannerBlock(blocks.StructBlock):
    banner_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="The bold header text at the frontpage slider")
    banner_subhead = blocks.RichTextBlock(null=True, blank=False, help_text="The content of the frontpage slider element", classname="full")
    banner_image = ImageChooserBlock(null=True, blank=False, help_text="Big, high resolution slider image")

    graphql_fields = [GraphQLString("banner_head"),GraphQLString("banner_subhead"),GraphQLImage("banner_image"),]

#> Info Section

@register_streamfield_block
class _S_AboutBlock(blocks.StructBlock):
    info_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="The bold header text at the frontpage slider")
    info_subhead = blocks.RichTextBlock(null=True, blank=False, help_text="The content of the frontpage slider element", classname="full")
    info_image = ImageChooserBlock(null=True, blank=False, help_text="Big, high resolution slider image")
    info_image_position = blocks.ChoiceBlock(null=True, blank=False, choices=[
        ('left', 'left'),
        ('right', 'right'),
    ], icon='cup')

    graphql_fields = [GraphQLString("head"), GraphQLString("subhead"),]

@register_streamfield_block
class Box_CollumBlock(blocks.StructBlock):
    collum_image = ImageChooserBlock(null=True, blank=False, help_text="Icon representating the below content")
    collum_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="The bold header text at the frontpage slider")
    collum_subhead = blocks.RichTextBlock(null=True, blank=False, help_text="The content of the frontpage slider element", classname="full")
    collum_paragraph = blocks.RichTextBlock(null=True, blank=False, help_text="Formatted text", classname="full")

@register_streamfield_block
class _S_BoxesBlock(blocks.StructBlock):
    boxes_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    boxes_displayhead = blocks.BooleanBlock(null=True, blank=True, default=True, required=False, help_text="Whether or not to display the header")
    boxes_collums = blocks.StreamBlock([
        ('box_collum', Box_CollumBlock(null=True, blank=False, icon='cogs'))
    ], null=True, blank=False, max_num=3)

#> Homepage
class HomePage(Page):
    headers = StreamField([
        ('h_banner', _H_BannerBlock(null=True, blank=False, icon='title')),
        ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code')),
    ], null=True, blank=False)

    sections = StreamField([
        ('s_about', _S_AboutBlock(null=True, blank=False, icon='radio-empty')),
        ('s_boxes', _S_BoxesBlock(null=True, blank=False, icon='pilcrow')),
    ], null=True, blank=False, )

    main_content_panels = [
        StreamFieldPanel('headers'),
        StreamFieldPanel('sections')
    ]

    graphql_fields = [
        GraphQLStreamfield("headers"),
        GraphQLStreamfield("sections"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Main'),
        ObjectList(Page.promote_panels + Page.settings_panels, heading='Settings', classname="settings")
    ])
