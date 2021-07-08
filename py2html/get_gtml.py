import os
import glob
import codecs
import lxml.html as lh

from lxml import etree
from io import StringIO

def copy_htmlfolder(folder,new_folder):
    for name in glob.glob(folder + '/*km'):
        htmls_path = os.path.join(name,'html')

        ev_name = os.path.basename(name)
        new_path = os.path.join(new_folder,ev_name)

        if os.path.isdir( new_path ) == False:
            os.makedirs(new_path)

        msg = f"cp -avf -r -R {htmls_path} {new_path}"
        print('\n')
        os.system(msg)
        # print(msg)
        # print(htmls_path,' --> ',new_path)
        # print(htmls_path,' --> ',new_path)

def mv_gif(folder):
    'escenario folder'
    for name in glob.glob(folder + '/*km'):
        htmls_path = os.path.join(name,'html')

        
        for f in glob.glob(htmls_path+'/2*'):
            date_folder = f
        for gif in glob.glob(htmls_path+'/*.gif'):
            msg = f"mv {gif} {date_folder}"
            print(msg)
            os.system(msg)

        # print('\n')
def mp42gif_text(html_path):
    'change mp4 path to gif path in the html file'
    f=codecs.open(html_path, 'r').read()
    html = lh.fromstring(f)

    for el in html.iter("iframe"):
        name = el.attrib['src'].split('.')[0]
        el.attrib['src'] = name +'.gif'
        el.attrib['width'] = '700'
        el.attrib['height'] = '800'
        # string = lh.tostring(html, pretty_print=True)

    for ol in html.iter("img"):
        ol.attrib['width'] = '800'
        ol.attrib['height'] = '800'

    string = lh.tostring(html, pretty_print=True)
    name = os.path.basename(html_path).split('.')[0]
    name= name + '_simulation.html'
    dirname = os.path.dirname(html_path)
    html_path = os.path.join(dirname,name)

    print(html_path)
    with open(html_path, 'wb') as f:
        f.write(string)

folder = "/mnt/escenarios"
new_folder = "/mnt/escenarios/web_page"

# html = "/mnt/escenarios/21192022202020_0.87787_80.27231_M7.5_10km/html/21192022202020/21192022202020_mts.html"
# mp42gif_text(html)

mv_gif(new_folder)


####################################################### MP4_text
# esc_path = "/mnt/escenarios/web_page"
# for name in glob.glob(esc_path + '/*km'):
#     htmls_path = os.path.join(name,'html')

#     ev = os.listdir(htmls_path)[0]
#     htmls_path = os.path.join(htmls_path,ev)
#     for html in glob.glob(htmls_path + '/*_mts.html'):
#         print(html)

#         mp42gif_text(html)

#     print('\n')