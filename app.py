import os
import subprocess
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Konfigurasi Folder di Mac kamu
DOWNLOAD_FOLDER = os.path.expanduser("~/Downloads")
UPLOAD_FOLDER = os.path.join(DOWNLOAD_FOLDER, "Clipper_Uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "Data tidak diterima."})

    url = data.get('url')
    start = data.get('start', '00:00:00')
    end = data.get('end', '00:00:10')
    mode = data.get('mode', 'landscape')
    custom_name = data.get('custom_name', '').strip()

    # Logika Penamaan
    if not custom_name:
        custom_name = f"clipping_{start.replace(':', '')}"
    if not custom_name.endswith(".mp4"):
        custom_name += ".mp4"
    
    filename = secure_filename(custom_name.replace(" ", "_"))
    output_path = os.path.join(DOWNLOAD_FOLDER, filename)

    try:
        # Proses Download & Potong
        subprocess.run([
            "/usr/local/bin/yt-dlp", "--no-playlist",
            "--downloader", "ffmpeg",
            "--downloader-args", f"ffmpeg_i:-ss {start} -to {end}",
            "-f", "bv[ext=mp4]+ba[ext=m4a]/b[ext=mp4]",
            "--merge-output-format", "mp4", "-o", output_path, url
        ], check=True)

        if mode == 'portrait':
            reels_path = os.path.join(DOWNLOAD_FOLDER, f"reels_{filename}")
            subprocess.run([
                "/usr/local/bin/ffmpeg", "-i", output_path,
                "-vf", "crop=ih*(9/16):ih", "-c:a", "copy", "-y", reels_path
            ], check=True)
            return jsonify({"status": "success", "message": f"Berhasil! File Reels: reels_{filename}"})

        return jsonify({"status": "success", "message": f"Berhasil! File: {filename}"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "File tidak ditemukan!"})
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(input_path)
    
    output_name = f"reels_{filename}"
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_name)
    
    try:
        subprocess.run([
            "/usr/local/bin/ffmpeg", "-i", input_path,
            "-vf", "crop=ih*(9/16):ih", "-c:a", "copy", "-y", output_path
        ], check=True)
        return jsonify({"status": "success", "message": f"Konversi Selesai: {output_name}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)