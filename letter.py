from flask import Blueprint, render_template, send_file
import locale

from qrcodeutil import generate_qr_code
import parameters as pm

letter = Blueprint('letter', __name__)

locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')


@letter.route('/letter/<int:phrase>/<de>/<para>')
def get_score_nation(phrase, de, para):
    if phrase == 0:
        imagem_src = "/static/images/frase0.png"
    elif phrase == 1:
        imagem_src = "/static/images/frase1.png"
    elif phrase == 2:
        imagem_src = "/static/images/frase2.png"
    elif phrase == 3:
        imagem_src = "/static/images/frase3.png"
    elif phrase == 4:
        imagem_src = "/static/images/frase4.png"
    return render_template('letter.html', imagem_src=imagem_src, de=de, para=para)


@letter.route('/qr/<int:phrase>/<de>/<para>')
def get_qrcode_score(phrase, de, para):
    qr_image = generate_qr_code(pm.BASE_URL + '/letter/' + str(phrase) + '/' + de + '/' + para)
    return send_file(qr_image, mimetype='image/png')
