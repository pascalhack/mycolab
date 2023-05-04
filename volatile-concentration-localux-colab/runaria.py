import os, pickle, subprocess

if os.path.exists('/content/gdrive/MyDrive/dp/arialist.pkl'):
  with open('/content/gdrive/MyDrive/dp/arialist.pkl', 'rb') as f:
      arialines = pickle.load(f)

if arialines:
  for line in arialines:
    if not '4x-UltraSharp.pth' in line:
      ariaexecline = line[2:].replace('\\n",', '').replace('/content/gdrive/MyDrive/dp/stable-diffusion-webui', '/content/gdrive/MyDrive/dp/volatile-concentration-localux')
      try:
        subprocess.run(ariaexecline, shell=True, check=True)
      except Exception as e:
          print("Exception: " + str(e))