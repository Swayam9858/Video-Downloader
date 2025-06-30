from flask import Flask, request, render_template_string
import yt_dlp

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>Video Downloader</title>
<h2>Enter Video URL</h2>
<form method=post>
  <input type=text name=url placeholder="Paste video link here">
  <input type=submit value=Download>
</form>
{% if download_url %}
  <p><a href="{{ download_url }}">Click here to download video</a></p>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    download_url = None
    if request.method == 'POST':
        url = request.form['url']
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'skip_download': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            download_url = info['url']
    return render_template_string(TEMPLATE, download_url=download_url)

if __name__ == '__main__':
    app.run(debug=True)
