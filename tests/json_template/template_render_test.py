from unittest import TestCase
from mockserver.json_template import template_render
import logging

logger = logging.getLogger()


class TemplateRenderTest(TestCase):

    def test_replace(self):
        json_str = '{"name":"zy", "id":1, "create_time": "{%date%}", "last_modify":"{% datetime.now %}"}'
        res_line = template_render._replace(json_str, "{%datatime.now%}")
        self.assertTrue(res_line.find("{%datatime.now%}") == -1)
        res_line = template_render._replace(json_str, "{% datetime.now %}")
        self.assertTrue(res_line.find("{% datetime.now %}") == -1)

    def test_render(self):
        j_str = '{"pic":"http://{% server_host%}/hello", "date":"{%  datetime.now   %}"}'
        res = template_render.render(j_str)
        self.assertTrue(res.find('{%') == -1)
        nomorl_str = 'abcdefghijklmnopqrst'
        res = template_render.render(nomorl_str)
        self.assertEqual(nomorl_str, res)

