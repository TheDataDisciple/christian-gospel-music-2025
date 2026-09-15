from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf/Christian_Gospel_Luminate_2025_Summary.pdf'
OUT.parent.mkdir(parents=True,exist_ok=True)
navy=colors.HexColor('#142C3A'); teal=colors.HexColor('#147D80'); gray=colors.HexColor('#52626A'); pale=colors.HexColor('#EDF5F5')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleX',fontName='Helvetica-Bold',fontSize=28,leading=32,textColor=navy,spaceAfter=12))
styles.add(ParagraphStyle(name='SubX',fontSize=11,leading=16,textColor=gray,spaceAfter=16))
styles.add(ParagraphStyle(name='HeadX',fontName='Helvetica-Bold',fontSize=14,leading=19,textColor=navy,spaceBefore=13,spaceAfter=7))
styles.add(ParagraphStyle(name='BodyX',fontSize=10,leading=14,textColor=navy,spaceAfter=8))
styles.add(ParagraphStyle(name='SmallX',fontSize=8.2,leading=11,textColor=gray,spaceAfter=7))
styles.add(ParagraphStyle(name='CellX',fontSize=9,leading=12,textColor=navy))
styles.add(ParagraphStyle(name='WhiteX',fontName='Helvetica-Bold',fontSize=9,leading=12,textColor=colors.white))
story=[]
def p(t,style='BodyX'): story.append(Paragraph(t,styles[style]))
def h(t): p(t,'HeadX')
def table(rows,widths):
    cells=[[Paragraph(str(x),styles['WhiteX' if i==0 else 'CellX']) for x in row] for i,row in enumerate(rows)]
    t=Table(cells,colWidths=widths,hAlign='LEFT',repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('ROWBACKGROUNDS',(0,1),(-1,-1),[pale,colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,-1),(-1,-1),0.5,colors.HexColor('#CCDADC'))]))
    story.append(t); story.append(Spacer(1,8))

p('CHRISTIAN / GOSPEL','SmallX')
p('A small share.<br/>A strong year.','TitleX')
p('A focused digest of Luminate\'s 2025 Year-End Music Report<br/>January 2026 edition | United States unless stated otherwise','SubX')
p('<b>Christian/Gospel generated 30.0 billion U.S. on-demand audio streams in 2025, representing 2.1% of the market.</b> Its total audio streaming grew 18.5% year over year, and its presence among the most-streamed songs expanded. [pp. 19-20, 22, 77]')
table([['2025 audio streams','Audio market share','Annual audio growth'],['<b>30.0 billion</b> [p. 19]','<b>2.1%</b> [p. 77]','<b>+18.5%</b> [p. 20]']],[166,166,167])
h('01 / Scale and momentum')
p('Christian/Gospel ranks <b>eighth</b> in the report\'s U.S. main-genre audio streaming table, just below World Music (31.3 billion). The introduction also highlights Christian/Gospel alongside Rock as a driver of U.S. genre growth. [pp. 4, 19]')
p('Its audio market share rose <b>0.25 percentage points in 2025</b>, following a gain of <b>0.12 points in 2024</b>. It ranks second in the 2025 share-gain chart, behind Rock (+0.30 points) and ahead of Latin (+0.04 points). These are changes in market share, distinct from the 18.5% increase in stream volume. [p. 20]')
h('02 / New releases are a particular strength')
p('Audio streaming of <b>Current Christian/Gospel music increased 37.9%</b> in 2025. Luminate defines Current as tracks 18 months old or newer. Across all genres, Current audio streaming declined <b>1.6%</b>, to 334.0 billion from 339.3 billion. The chart places Christian/Gospel first by absolute Current stream-volume gain; its percentage growth is not the highest on the chart. [p. 24]')
h('03 / More songs reach the upper streaming tiers')
table([['U.S. song tier','2024 count','2025 count','Change'],['Top 500','0','3','+3'],['Top 1,000','1','5','+4'],['Top 5,000','39','67','+28'],['Top 10,000','126','175','+49']],[200,95,95,109])
p('Counts of Christian/Gospel songs within all-genre rankings by U.S. on-demand audio streams. The tiers are nested and must not be added together. The report does not name the songs in these counts. [p. 22]','SmallX')
story.append(PageBreak())
p('CONSUMPTION & AUDIENCE','SmallX'); p('Where the genre stands','TitleX')
h('04 / Market share depends on the format')
p('Each percentage below is Christian/Gospel\'s share of the corresponding U.S. market, not the percentage of people who listen to the genre. [p. 77]')
table([['Market measure','Christian/Gospel share'],['Total album-equivalent consumption (Albums + TEA + SEA On-Demand)','2.1%'],['Total on-demand streams (audio + video)','2.2%'],['On-demand audio streams','2.1%'],['On-demand video streams','2.4%'],['Total album sales','1.3%'],['Physical album sales','1.0%'],['Digital album sales','3.5%'],['Digital song sales','4.6%']],[370,129])
h('05 / Streaming dominates consumption within the genre')
p('This second table uses a different denominator: <b>Christian/Gospel\'s own total album-equivalent consumption</b>. It shows how that consumption is distributed across formats. [p. 78]')
table([['Format within Christian/Gospel','Share'],['On-demand audio streams (SEA)','89.2%'],['On-demand video streams (SEA)','3.9%'],['Physical albums','3.1%'],['Digital albums','1.9%'],['Digital track sales (TEA)','1.9%']],[370,129])
p('<b>Derived total:</b> audio and video streaming together account for <b>93.1%</b> of the genre\'s album-equivalent consumption (89.2% + 3.9%). This is an equivalent-unit mix, not a revenue breakdown.','SmallX')
h('06 / Two audience and purchasing signals')
p('<b>Paid-streaming intent:</b> among monthly Christian/Gospel listeners who do not currently pay for a digital streaming service, <b>12% are somewhat likely</b> and <b>6% extremely likely</b> to subscribe within six months. These are rounded chart labels and stated intentions, not observed conversions. [p. 34]')
p('<b>Vinyl retail:</b> people buying vinyl exclusively from mass-market retailers over-index in Christian/Gospel, K-pop and Children\'s music. This indicates disproportionate representation in that buyer group; the report gives no Christian/Gospel-specific index or percentage. [p. 30]')
story.append(PageBreak())
p('ARTISTS & SOURCE GUIDE','SmallX'); p('What the report says<br/>about artists','TitleX')
h('07 / Brandon Lake is the featured Christian/Gospel artist')
p('<b>Brandon Lake</b> is pictured and named on the Christian/Gospel page accompanying the song-tier table. The image credit reads "courtesy image." The page presents genre-level song counts; it does <b>not</b> provide his personal stream total, album sales, song titles or artist ranking. [p. 22]')
p('The report does not supply a dedicated ranking of Christian/Gospel performers. No individual figures for Forrest Frank, Lauren Daigle, CeCe Winans, Elevation Worship, Phil Wickham, Josiah Queen or Lecrae were located in this PDF. Their popularity cannot be quantified from this source alone.')
p('Xania Monet appears in the report\'s AI discussion and artist comparisons. Those passages do not identify the project as Christian/Gospel, so its statistics are not treated here as evidence about the genre. [pp. 3, 5, 57, 59]','SmallX')
h('08 / Page-by-page reference map')
table([['Source PDF page(s)','Relevant content'],['4','Introduction: Christian/Gospel highlighted with Rock as a U.S. genre-growth driver.'],['19-20','Genre audio-stream volume, ranking, annual growth and market-share gains.'],['21, 23','Christian/Gospel appears in the shared heading/navigation; substantive data on these pages concern Rock and Latin.'],['22','Christian/Gospel song-tier counts and Brandon Lake image/caption.'],['24','Growth of Current music: Christian/Gospel +37.9%.'],['30, 34','Mass-market vinyl-buyer profile and paid-streaming subscription intent.'],['77-78','U.S. genre shares by format and within-genre consumption mix.']],[115,384])
h('Reading the figures correctly')
p('<b>Period:</b> the methodology aligns the consumption year-over-year comparison to 52 weeks: January 3, 2025-January 1, 2026 versus January 5, 2024-January 2, 2025. <b>Share points</b> mean percentage points. <b>TEA</b> and <b>SEA</b> mean track-equivalent and streaming-equivalent albums. [pp. 81-82; chart notes]')
p('Consumption figures are attributed to Luminate Music Consumption Data; audience findings use Luminate Insights Music 360 (U.S.). No subgroup sample size or confidence interval is shown on the two audience pages. These results measure recorded-music consumption and consumer responses, not changes in religious belief. [pp. 30, 34, 83]')
p('<b>Sole source:</b> Luminate, <i>2025 Year-End Music Report</i>, user-supplied file <i>2025-Year-End-Music-Report-1.2026.pdf</i> (85 pages). References use the 1-based PDF page order, including the cover. This digest paraphrases the source; explicitly marked calculations are derived from its published figures. No outside sources are used.','SmallX')

def footer(c,d):
    w,h=d.pagesize
    c.setStrokeColor(teal); c.setLineWidth(2); c.line(48,h-33,w-48,h-33)
    c.setFont('Helvetica',8); c.setFillColor(gray)
    c.drawString(48,25,'LUMINATE 2025 | CHRISTIAN / GOSPEL DIGEST')
    c.drawRightString(w-48,25,str(d.page))
doc=SimpleDocTemplate(str(OUT),pagesize=(595.28,841.89),rightMargin=48,leftMargin=48,topMargin=48,bottomMargin=46,title='Christian/Gospel: Luminate 2025 Report Digest',author='Research summary',pageCompression=1)
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
