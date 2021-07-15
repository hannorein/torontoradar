from flask import Flask, send_from_directory
import glob

app = Flask(__name__)

@app.route('/')
def index():
    html = "<html><body><img id=\"radar\"></img><script>"
    html += """
    var radarImage = document.getElementById('radar');
    var pictures = ["""
    for f in sorted(glob.glob("/home/rein/torontoradar/*_PRECIPET_RAIN.gif")):
        f = f.split("/")[-1]
        html = html + "\""+f+"\", "
    
    html += """
    ];

    var i = 0;
    var l = pictures.length - 1;

    (function loop() {
      if (i > l){
        i = 0;
      }
      radarImage.src = pictures[i];
      loopTimer = setTimeout(loop, 120);
      ++i;
    })();
    </script>
    </body>
    </html>
    """
    return "" + html

@app.route('/<filename>.gif')
def serveimage(filename):
    return send_from_directory('/home/rein/torontoradar/',filename+".gif")

if __name__ == '__main__':
    app.run(debug = True)
