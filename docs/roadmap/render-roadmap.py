"""Render the editable sibling Markdown to PDF. Requires reportlab; no plugin operations."""
from pathlib import Path
from xml.sax.saxutils import escape
import re, hashlib
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
base=Path(__file__).resolve().parent
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyRoad',fontName='Helvetica',fontSize=9,leading=13,spaceAfter=7,splitLongWords=True))
styles.add(ParagraphStyle(name='TitleRoad',fontName='Helvetica-Bold',fontSize=29,leading=34,textColor=colors.HexColor('#15364b'),spaceAfter=25))
styles.add(ParagraphStyle(name='SectionRoad',fontName='Helvetica-Bold',fontSize=20,leading=25,textColor=colors.HexColor('#15364b'),spaceAfter=15))
styles.add(ParagraphStyle(name='EntryRoad',fontName='Helvetica-Bold',fontSize=14,leading=19,textColor=colors.HexColor('#176978'),spaceAfter=12,keepWithNext=True))
class Doc(SimpleDocTemplate):
 def afterFlowable(self,f):
  if isinstance(f,Paragraph) and f.style.name in ['SectionRoad','EntryRoad']:
   text=f.getPlainText(); level=0 if f.style.name=='SectionRoad' else 1
   key='h'+hashlib.sha256(text.encode()).hexdigest()[:16];self.canv.bookmarkPage(key)
   self.canv.addOutlineEntry(text,key,level=level,closed=True)
   self.notify('TOCEntry',(level,text,self.page,key))
def footer(c,d):
 c.setStrokeColor(colors.HexColor('#b7c8d1'));c.line(44,39,551,39)
 c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#536674'))
 c.drawString(44,26,'DEMIR BOT | CURRENT SPECIFICATION & ROADMAP | 24 SEP 2026');c.drawRightString(551,26,str(d.page))
def clean(s):
 for a,b in [('—','-'),('–','-'),('‑','-'),('’',"'"),('“','"'),('”','"'),('→','to')]:s=s.replace(a,b)
 return escape(s)
story=[]
for block in (base/'demir-bot-master-roadmap.md').read_text().split('\n\n'):
 block=block.strip()
 if not block:continue
 if block.startswith('# '):
  lines=block.split('\n',1);story.append(Paragraph(clean(lines[0][2:]),styles['TitleRoad']))
  if len(lines)>1:story.append(Paragraph(clean(lines[1]),styles['BodyRoad']))
  story.append(Paragraph('Current capabilities. Future work in implementation order.',styles['BodyRoad']))
  story.append(PageBreak());story.append(Paragraph('Contents',styles['SectionRoad']))
  toc=TableOfContents();toc.levelStyles=[ParagraphStyle(name='toc0',fontName='Helvetica-Bold',fontSize=10,leading=15,spaceBefore=8),ParagraphStyle(name='toc1',fontName='Helvetica',fontSize=8,leading=11,leftIndent=12)]
  story.append(toc)
 elif block.startswith('## '):
  story.append(PageBreak());story.append(Paragraph(clean(block[3:]),styles['SectionRoad']))
 elif block.startswith('### '):
  if re.match(r'### \d{3}\.',block):story.append(PageBreak())
  else:story.append(Spacer(1,12))
  story.append(Paragraph(clean(block[4:]),styles['EntryRoad']))
 else:
  text=clean(block)
  if ':' in block and len(block.split(':',1)[0])<48:
   a,b=text.split(':',1);text='<b>'+a+':</b>'+b
  story.append(Paragraph(text,styles['BodyRoad']))
doc=Doc(str(base/'demir-bot-master-roadmap.pdf'),pagesize=(595.28,841.89),rightMargin=44,leftMargin=44,topMargin=44,bottomMargin=53,title='Demir Bot - Current Specification and Master Roadmap',author='Demir Bot documentation')
doc.multiBuild(story,onFirstPage=footer,onLaterPages=footer)
print('Rendered',base/'demir-bot-master-roadmap.pdf')
