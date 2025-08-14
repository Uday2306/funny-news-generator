from flask import Flask, jsonify,render_template, request
from news_generation import generate_news
import sqlite3
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import textwrap
from generate_poster import create_poster

app = Flask(__name__)

@app.route("/")
def index():
    headline = generate_news()
    print(f"Genetrated Headline: {headline}")
    return render_template("index.html",headline = headline)


# For getting votes through flask and adding it to our database
@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    headline = data.get('headline')
    vote_type = data.get('vote_type')

    if headline and vote_type in ['funny', 'notfunny']:
        conn = sqlite3.connect('votes.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO votes (headline, vote_type) VALUES (?, ?)', (headline, vote_type))
        conn.commit()
        conn.close()
        return {'message': 'Vote recorded successfully!'}, 200
    else:
        return {'message': 'Invalid vote data'}, 400
    

# This will select the top funny headlines based on the votes
@app.route('/top')
def top_headlines():
    conn = sqlite3.connect('votes.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT headline, COUNT(*) as funny_votes 
        FROM votes 
        WHERE vote_type = 'funny' 
        GROUP BY headline 
        ORDER BY funny_votes DESC 
        LIMIT 10
    ''')

    top_votes = cursor.fetchall()
    conn.close()

    return render_template('top.html', top_votes=top_votes)

# This will used to create a posters based on headlines
@app.route("/poster/<headline>")
def generate_poster(headline):
    # Create a blank image
    img = Image.new('RGB', (1080, 720), color=(24, 24, 24))  # dark background

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 48)  # use custom font path if needed

    wrapped_text = textwrap.fill(headline, width=25)
    draw.text((50, 300), wrapped_text, font=font, fill=(255, 255, 255))

    # Save poster
    img_path = "static/poster.png"
    img.save(img_path)

    return render_template("poster.html", poster_url=img_path)


# POster route
@app.route('/poster')
def poster():
    '''
    headline = request.args.get('headline', 'No Headline Provided')
    # Render poster template or call your poster generation logic
    return render_template('poster.html', headline=headline)
    '''
    headline = request.args.get('headline', 'No Headline Provided')
    poster_filename = create_poster(headline)
    return render_template("poster.html", headline=headline, poster_image=poster_filename)
    

if __name__ == '__main__':

    app.run(debug=True)








