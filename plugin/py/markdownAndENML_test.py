# encoding: utf-8
# vim: sts=4 sw=4 fdm=marker
# Author: kakkyz <kakkyz81@gmail.com>
# License: MIT
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))
from . import markdownAndENML
import unittest
from xml.dom import minidom


class TestMarkdownAndENML(unittest.TestCase):
    """ doc """

    def setUp(self):  # {{{
        pass
    #}}}

    def testParseENML(self):  # {{{
        sampleXML = '<?xml version="1.0" encoding="utf-8"?>'
        sampleXML += '<!DOCTYPE en-note'
        sampleXML += '  SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
        sampleXML += '<en-note style="word-wrap: break-word;">'
        sampleXML += '   <h1 style="color: rgb(0, 0, 0); font-weight: normal;">'
        sampleXML += '       <font size="3">'
        sampleXML += '           らき☆すた'
        sampleXML += '       </font>'
        sampleXML += '   </h1>'
        sampleXML += '   <div style="margin-top: 5px;">'
        sampleXML += '       <a href="http://www.google.com" style="color: blue !important;">'
        sampleXML += '           <font size="3">'
        sampleXML += '               <img src="http://www.google.co.jp/images/nav_logo101.png" alt="hope-echoes" />'
        sampleXML += '               泉こなた'
        sampleXML += '           </font>'
        sampleXML += '       </a>'
        sampleXML += '   </div>'
        sampleXML += '   <en-media hash="xxxxx" style="cursor: default; vertical-align: middle;" type="image/jpeg"/>'
        sampleXML += '   <ul>'
        sampleXML += '       <li>リスト１</li>'
        sampleXML += '       <li>りすと２</li>'
        sampleXML += '       <li>リスト３</li>'
        sampleXML += '   </ul>'
        sampleXML += '   <en-todo checked="false"/>チェックボックス<br/>'
        sampleXML += '   <en-todo checked="true"/>チェック済み'
        sampleXML += '   <ol>'
        sampleXML += '       <li> 数字付１</li>'
        sampleXML += '       <li> 同じく２</li>'
        sampleXML += '       <li> おまけに３</li>'
        sampleXML += '   </ol>'
        sampleXML += '   <ol>'
        sampleXML += '       <li> list2-1</li>'
        sampleXML += '       <li> list2-2</li>'
        sampleXML += '   </ol>'
        sampleXML += '       <blockquote style="margin: 0 0 0 40px; border: none; padding: 0px;">'
        sampleXML += '           <div> インデント</div>'
        sampleXML += '           <div> インデント２</div>'
        sampleXML += '       </blockquote>'
        sampleXML += '   <blockquote style="margin: 0 0 0 40px; border: none; padding: 0px;">'
        sampleXML += '       <blockquote style="margin: 0 0 0 40px; border: none; padding: 0px;">'
        sampleXML += '           <p> ２重インデント'
        sampleXML += '            ２重インデント２</p>'
        sampleXML += '       </blockquote>'
        sampleXML += '   </blockquote>'
        sampleXML += '   <p>normal line</p>'
        sampleXML += '   <pre><code>def haruhi(self):\n'
        sampleXML += '    pass<a href="hoge"> test </a>\n'
        sampleXML += '    > >'
        sampleXML += '   </code></pre>'
        sampleXML += '   <h3>asuka.langley</h3>'
        sampleXML += '   test backtick<code>import markdown</code>test'
        sampleXML += '</en-note>'
        dom = minidom.parseString(sampleXML)
        lines = markdownAndENML.parseENML(dom.documentElement).splitlines()
#       print "\n".join(lines)
        self.assertEqual(lines[0], '# らき☆すた')
        self.assertEqual(lines[1] , '[{<img alt="hope-echoes" src="http://www.google.co.jp/images/nav_logo101.png"/>')
        self.assertEqual(lines[2] , '泉こなた}]({http://www.google.com})')
        self.assertEqual(lines[3] , '<en-media hash="xxxxx" style="cursor: default; vertical-align: middle;" type="image/jpeg"/>')
        self.assertEqual(lines[4] , '* リスト１')
        self.assertEqual(lines[5] , '* りすと２')
        self.assertEqual(lines[6] , '* リスト３')
        self.assertEqual(lines[7] , '')
        self.assertEqual(lines[8] , '<en-todo checked="false"/>')
        self.assertEqual(lines[9], 'チェックボックス')
        self.assertEqual(lines[10], '<en-todo checked="true"/>')
        self.assertEqual(lines[11], 'チェック済み')
        self.assertEqual(lines[12], '1. 数字付１')
        self.assertEqual(lines[13], '2. 同じく２')
        self.assertEqual(lines[14], '3. おまけに３')
        self.assertEqual(lines[15], '')
        self.assertEqual(lines[16], '1. list2-1')
        self.assertEqual(lines[17], '2. list2-2')
        self.assertEqual(lines[18], '')
        self.assertEqual(lines[19], '> インデント')
        self.assertEqual(lines[20], '> インデント２')
        self.assertEqual(lines[21], '')
        self.assertEqual(lines[22], '> > ２重インデント            ２重インデント２')
        self.assertEqual(lines[23], '')
        self.assertEqual(lines[24], '')
        self.assertEqual(lines[25], '')
        self.assertEqual(lines[26], 'normal line')
        self.assertEqual(lines[27], '')
        self.assertEqual(lines[28], '    def haruhi(self):')
        self.assertEqual(lines[29], '        pass<a href="hoge"> test </a>')
        self.assertEqual(lines[30], '        > >')
        self.assertEqual(lines[31], '')
        self.assertEqual(lines[32], '### asuka.langley')
        self.assertEqual(lines[33], 'test backtick')
        self.assertEqual(lines[34], '`import markdown`test')
    # }}}

if __name__ == '__main__':
    from time import localtime, strftime
    print('\n**' + strftime("%a, %d %b %Y %H:%M:%S", localtime()) + '**\n')
# profileを取るとき
#   import test.pystone
#   import cProfile
#   import pstats
#   prof = cProfile.run("unittest.main()", 'cprof.prof')
#   p = pstats.Stats('cprof.prof')
#   p.strip_dirs()
#   p.sort_stats('cumulative')
#   p.print_stats()
#
# 全て流す時
    unittest.main()
#
# 個別でテストするとき
#   suite = unittest.TestSuite()
#   suite.addTest(TestMarkdownAndENML('testParseENML'))
#   unittest.TextTestRunner().run(suite)
