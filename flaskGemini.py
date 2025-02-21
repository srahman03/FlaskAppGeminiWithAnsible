from flask import * 
import google.generativeai as genai
import os
import psutil
import time
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = "abc" 

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GENAI_API_KEY")
genai.configure(api_key=api_key)
prompt= """Write Recommendations to be followed by SRE when the production Server load is high. 
respond with 3 suggestions and order by priority and less than 100 lines. 
Respond in html, ignore header and body tags"""

def convert_bytes(size):
    """Convert bytes to a human-readable format (KB, MB, GB, etc.)."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:#1024B:1kb - 1024kb:1mb etc so when smaller, it is at the right unit so prints value.00 {unit}
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"  # Handles very large sizes

@app.route('/')
def Home():
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    session["text"] = response.text.strip("\n").strip("`").lstrip("html") # lstrip-leftside characters that start with html
    return render_template('index.html')

@app.route('/2')
def diskLoad():
    disk_usage = psutil.disk_usage('/')#returns tuple
    return jsonify({
        "Disk Usage"
        "total": convert_bytes(disk_usage.total),
        "used": convert_bytes(disk_usage.used),
        "free": convert_bytes(disk_usage.free),
        "percent": f"{disk_usage.percent:.2f}%"
    })

@app.route('/3')
def networkLoad():
    net1 = psutil.net_io_counters()  # Get initial network data # return tuples of bytes_sent,bytes_recv
    time.sleep(1)  # Wait 1 second
    net2 = psutil.net_io_counters()  # Get network data again

    # Calculate bytes per second # calculating average bytes
    bytes_sent_per_sec = net2.bytes_sent - net1.bytes_sent #Upload speed
    bytes_recv_per_sec = net2.bytes_recv - net1.bytes_recv #Download Speed

    return jsonify({
        "Network Load"
        "total_sent": convert_bytes(net2.bytes_sent),
        "total_received": convert_bytes(net2.bytes_recv),
        "upload_speed": convert_bytes(bytes_sent_per_sec) + "/s",
        "download_speed": convert_bytes(bytes_recv_per_sec) + "/s"
    })

@app.route('/4')
def memoryLoad():
    mem = psutil.virtual_memory()#tuple
    
    return jsonify({
        "Memory Load"
        "total": convert_bytes(mem.total),
        "used": convert_bytes(mem.used),
        "free": convert_bytes(mem.available),
        "percent": f"{mem.percent:.2f}%"
    })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
