import justpy as jp
import justpy as jp
from pandas.core.dtypes.common import classes

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews', classes='text-h3 text-center q-pt-lg')
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analaysis', classes='text-body1 text-center q-pt-md')
    return wp

jp.justpy(app)