import os, pickle, subprocess

arialines = None
colaboptions = None
downloadcnet = False

if os.path.exists('/content/gdrive/MyDrive/dp/arialist.pkl'):
  with open('/content/gdrive/MyDrive/dp/arialist.pkl', 'rb') as f:
      arialines = pickle.load(f)

if os.path.exists('/content/gdrive/MyDrive/dp/colaboptions.pkl'):
  with open('/content/gdrive/MyDrive/dp/colaboptions.pkl', 'rb') as f:
      colaboptions = pickle.load(f)
      downloadcnet = colaboptions["controlnet"]
      downloadmodels = colaboptions["download_model"]

def subprocessing(execline):
  try:
    print("[1;32m" + execline)
    print('[0m')
    subprocess.run(execline, shell=True, check=True)
  except Exception as e:
      print("Exception: " + str(e))

if arialines:
  for line in arialines:
    if not '4x-UltraSharp.pth' in line:
      ariaexecline = line[2:].replace('\\n",', '').replace('/content/gdrive/MyDrive/dp/stable-diffusion-webui', '/content/gdrive/MyDrive/dp/volatile-concentration-localux')
      if 'ControlNet' in ariaexecline:
         if downloadcnet:
            subprocessing(ariaexecline)
      else:
        if downloadmodels:
          subprocessing(ariaexecline)

