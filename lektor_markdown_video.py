# -*- coding: utf-8 -*-
import re

from lektor.pluginsystem import Plugin
from extract_video_id import MdxVideo


class VideoMixin(object):

    def paragraph(self, text):        
        if not text.startswith('&!&'):
            return super(VideoMixin, self).paragraph(text)
        else:
            video_url = text[3:].strip()
            try:
                video = MdxVideo(url=video_url)
            except NotImplementedError:
                # incompatible
                return super(VideoMixin, self).paragraph(text)
            except ValueError:
                # invalid URL
                return super(VideoMixin, self).paragraph(text)
            else:
                return MdxVideo.get_embed_script()


class MarkdownVideoPlugin(Plugin):
    name = u'Markdown Video'
    description = u'Adds Embedded Videos to MarkDown files'

    def on_markdown_config(self, config, **extra):
        config.renderer_mixins.append(VideoMixin)
