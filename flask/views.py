from flask import Blueprint, request, jsonify, render_template
from pattern_generator import generate_pattern, create_dress_pattern_image, create_shirt_image, create_clothing_image
import base64

views = Blueprint("views", __name__)

@views.route('/')
def hello():
    yougakus = [
        {'title': 'adidas', 'price': 'Charlie Puth', 'arrival_day': '¥6,900', 'link': 'https://www.asos.jp/ja-jp/product/adidas-originals-adicolor-70-s-3-stripe-polo-shirt-in-beige/204175487?color=wondwr-white&size=xl'},
        {'title': 'adidas', 'price': 'The Kid LAROI', 'arrival_day': '¥9,700', 'link': 'https://www.asos.jp/ja-jp/product/adidas-originas-trefoil-monogram-tracktop-in-neutral/203402330?color=sand&size=xs'},
        # 他のエントリは省略
    ]
    return render_template('yougaku.html', yougakus=yougakus)

@views.route('/Logingpage.html')
def Longingpage():
    return render_template('Logingpage.html')

@views.route('/hougaku.html')
def hougaku():
    hougakus = [
        {'songname': 'クリスマスソング', 'artist': 'bucknumber', 'arrival_day': '2020月2月11日'},
        # 他のエントリは省略
    ]
    return render_template('hougaku.html', hougakus=hougakus)

@views.route('/k_pop.html')
def kpop():
    kpops = [
        {'artist': 'twice', 'songname': 'TT', 'arrival_day': '2020年2月11日', 'link': 'https://www.youtube.com/watch?v=rRzxEiBLQCA'},
        # 他のエントリは省略
    ]
    return render_template('k_pop.html', kpops=kpops)

@views.route('/generate_pattern', methods=['POST'])
def generate_pattern_route():
    pattern_type = request.form['patternType']
    size = request.form['size']
    pattern = generate_pattern(pattern_type, size)

    if 'error' in pattern:
        return jsonify({"error": pattern['error']})

    if pattern_type == 'dress':
        pattern_image = create_dress_pattern_image(size)
        clothing_image = create_clothing_image('dress', size)
    elif pattern_type == 'shirt':
        pattern_image = create_shirt_image()
        clothing_image = create_clothing_image('shirt', size)
    else:
        return jsonify({"error": "不明なパターンタイプ"})

    pattern_image_base64 = base64.b64encode(pattern_image).decode('utf-8')
    clothing_image_base64 = base64.b64encode(clothing_image).decode('utf-8')

    return jsonify({
        "pattern": pattern['pattern'],
        "size": pattern['size'],
        "pattern_image": pattern_image_base64,
        "clothing_image": clothing_image_base64
    })

@views.route('/generate_pattern.html')
def generate_pattern_html():
    return render_template('generate_pattern.html')
