from flask import Blueprint, render_template
from os import path

from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_bp = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)

films = [
    {
        "name": "Sound of Metal",
        "cover": "https://a.ltrbxd.com/resized/film-poster/4/3/2/0/0/4/432004-sound-of-metal-0-1000-0-1500-crop.jpg?v=289acd955b"
    },
    {
        "name": "Memento",
        "cover": "https://a.ltrbxd.com/resized/sm/upload/v1/3q/s4/aa/memento-0-1000-0-1500-crop.jpg?v=80f0732247"
    },
    {
        "name": "La Haine",
        "cover": "https://a.ltrbxd.com/resized/film-poster/5/1/6/8/4/51684-la-haine-0-1000-0-1500-crop.jpg?v=b6677cc136"
    },
    {
        "name": "The Social Network",
        "cover": "https://a.ltrbxd.com/resized/sm/upload/nw/cm/pa/ai/sGQv3ZMZBDBnl3z42Q0mEQ5uiDe-0-1000-0-1500-crop.jpg?v=54ee59f7cd"
    },
    {
        "name": "City of God",
        "cover": "https://a.ltrbxd.com/resized/film-poster/5/1/5/2/3/51523-city-of-god-0-1000-0-1500-crop.jpg?v=7517ea94ce"
    },
    {
        "name": "Do the Right Thing",
        "cover": "https://a.ltrbxd.com/resized/sm/upload/zm/fz/vn/ie/obNQLtdeJy3IiKnExWoWBJH8V67-0-1000-0-1500-crop.jpg?v=b4926532f8"
    },
    {
        "name": "Blade Runner",
        "cover": "https://a.ltrbxd.com/resized/sm/upload/85/io/38/dz/vfzE3pjE5G7G7kcZWrA3fnbZo7V-0-1000-0-1500-crop.jpg?v=0d5de70f0d"
    },
    {
        "name": "Pulp Fiction",
        "cover": "https://a.ltrbxd.com/resized/film-poster/5/1/4/4/4/51444-pulp-fiction-0-1000-0-1500-crop.jpg?v=dee19a8077"
    }
]


@main_bp.route('/')
@main_bp.route('/home')
def home():
    return render_template('home.html', films=films)


@main_bp.route("/about")
def about():
    return render_template('about.html')