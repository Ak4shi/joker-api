from flask import Flask,render_template, request
import os
import json
amt = 0
app = Flask('app')
from io import BytesIO

from PIL import Image
from flask import send_file
from PIL import ImageDraw, ImageFont


@app.route("/redir/")
async def redir():
  w = request.args.get("w")
  q = request.args.get("q")
  if w == None:
    with open("../static/data.json","r") as x:
      z = json.load(x)
    return z[str(q)]
  if q == None:
    w.replace("%20"," ")
    w = w.split()
    url = w[0]
    sas = w[1]
    with open("../static/data.json","r") as x:
      z = json.load(x)
    z[sas] = url
    with open("../static/data.json","w") as x:
      json.dump(z,x)


    

@app.route('/api/getframe/')
def hello_world():
  data = request.args.get("data")
  data = data.replace("%20"," ")
  data = data.split()
  img = data[0]
  frame = data[1]
  file = data[2]
  name = data[3]
  name = name.replace("/"," ")
  series = data[4]
  series = series.replace("/"," ")
  #file2 = data[3]
  #print(file)
  #print(file2)
  os.system(f"cd static && curl {img} -o {file}")
  #os.system(f"cd static && curl {frame} -o {file2}")
  overlay = Image.open(f"static/frames/{frame}.bmp").resize((370, 526))
  base = Image.open(f"static/{file}").resize((370, 526))
  base.paste(overlay, (0, 0), overlay)
  font = ImageFont.truetype("static/fonts/Acme-Regular.ttf", 20)
  draw = ImageDraw.Draw(base)
  draw.text((185, 5),name,(255,255,255),font=font)
  draw.text((10, 490),series,(255,255,255),font=font)

  base = base.convert('RGBA')
  b = BytesIO()
  base.save(b, format='png')
  b.seek(0)
  os.system(f"rm -rf static/{file}")
  return send_file(b, mimetype='image/png')

@app.route("/api/getdrop/")
def getdrop():
  return render_template("getdrop.html",frame="frame.png",frame3="frame.png",frame5="frame.png",img="aka.jpg",img3="aka.jpg",img5="aka.jpg")

app.run(host='0.0.0.0', port=8080)