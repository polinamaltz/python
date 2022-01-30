
import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Course Reviews", classes = "text-h4 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "Analysis of The Course Reviews", classes = "text-h5 q-pl-md")

    return wp


jp.justpy(app)