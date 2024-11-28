import re

packages = """

absl-py==1.0.0
addict==2.4.0
albumentations==1.1.0
anyio==3.6.1
argon2-cffi==20.1.0
asttokens==2.0.5
astunparse==1.6.3
attrs==21.4.0
Babel==2.10.3
backcall==0.2.0
beautifulsoup4==4.11.1
bleach==4.1.0
brotlipy==0.7.0
cachetools==5.0.0
certifi==2022.6.15
cffi==1.15.0
charset-normalizer==2.1.0
click==8.1.3
colorama==0.4.5
commonmark==0.9.1
cryptography==35.0.0
cycler==0.11.0
debugpy==1.5.1
decorator==5.1.1
defusedxml==0.7.1
dill==0.3.5.1
efficientnet-pytorch==0.7.1
entrypoints==0.3
etils==0.7.1
executing==0.8.3
fastjsonschema==2.16.1
flatbuffers==1.12
fonttools==4.31.2
gast==0.4.0
google-auth==2.6.0
google-auth-oauthlib==0.4.6
google-pasta==0.2.0
grpcio==1.43.0
h5py==3.7.0
idna==3.3
imageio==2.16.1
importlib-metadata==4.11.4
importlib-resources==5.9.0
ipykernel==6.9.1
ipython==8.1.1
ipython-genutils==0.2.0
ipywidgets==7.6.5
jax==0.3.16
jedi==0.18.1
Jinja2==3.0.3
jmp==0.0.2
joblib==1.1.0
json5==0.9.5
jsonschema==3.2.0
jupyter==1.0.0
jupyter-client==7.1.2
jupyter-console==6.4.3
jupyter-core==4.9.2
jupyter-server==1.18.1
jupyterlab==3.4.5
jupyterlab-pygments==0.1.2
jupyterlab-server==2.15.0
jupyterlab-widgets==1.0.0
keras==2.9.0
Keras-Preprocessing==1.1.2
kiwisolver==1.4.0
libauc==1.1.8
libclang==14.0.1
Markdown==3.3.6
MarkupSafe==2.0.1
matplotlib==3.5.1
matplotlib-inline==0.1.2
MedPy==0.4.0
mistune==0.8.4
mkl-fft==1.3.1
mkl-random==1.2.2
mkl-service==2.4.0
mmcls==0.23.2
mmcv-full==1.6.1
model-index==0.1.11
munch==2.5.0
nb-conda==2.2.1
nb-conda-kernels==2.3.1
nbclassic==0.4.3
nbclient==0.5.11
nbconvert==6.4.5
nbformat==5.4.0
nest-asyncio==1.5.1
networkx==2.7.1
notebook==6.4.8
notebook-shim==0.1.0
numpy==1.21.2
oauthlib==3.2.0
olefile==0.46
opencv-python==4.6.0.66
opencv-python-headless==4.5.5.64
openmim==0.2.1
opt-einsum==3.3.0
ordered-set==4.1.0
packaging==21.3
pandas==1.4.2
pandocfilters==1.5.0
parso==0.8.3
pexpect==4.8.0
pickleshare==0.7.5
Pillow==8.4.0
pip==21.2.4
pretrainedmodels==0.7.4
prometheus-client==0.13.1
prompt-toolkit==3.0.20
protobuf==3.19.4
ptyprocess==0.7.0
pure-eval==0.2.2
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.21
Pygments==2.11.2
pyOpenSSL==22.0.0
pyparsing==3.0.4
pyrsistent==0.18.0
PySocks==1.7.1
python-dateutil==2.8.2
pytz==2022.2.1
PyWavelets==1.3.0
PyYAML==6.0
pyzmq==22.3.0
qtconsole==5.2.2
QtPy==1.11.2
qudida==0.0.4
requests==2.28.1
requests-oauthlib==1.3.1
rich==12.5.1
rsa==4.8
scikit-image==0.19.2
scikit-learn==1.0.2
scipy==1.8.0
segmentation-models-pytorch==0.3.0
Send2Trash==1.8.0
setuptools==58.0.4
SimpleITK==2.1.1.2
sip==4.19.13
six==1.16.0
sniffio==1.2.0
soupsieve==2.3.2.post1
stack-data==0.2.0
tabulate==0.8.10
tensorboard==2.9.1
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.1
tensorflow==2.9.1
tensorflow-estimator==2.9.0
tensorflow-io-gcs-filesystem==0.26.0
termcolor==1.1.0
terminado==0.13.1
testpath==0.5.0
threadpoolctl==3.1.0
tifffile==2022.3.25
timm==0.4.12
torch==1.8.1
torchaudio==0.8.0a0+e4e171a
torchvision==0.9.1
tornado==6.1
tqdm==4.64.0
traitlets==5.1.1
typing_extensions==4.3.0
urllib3==1.26.11
wcwidth==0.2.5
webencodings==0.5.1
websocket-client==1.3.3
Werkzeug==2.0.3
wheel==0.37.1
widgetsnbextension==3.5.2
wrapt==1.14.1
yapf==0.32.0
zipp==3.7.0
"""

packages_no_version = re.sub(r'==[\d\.]+', '', packages)

# Loại bỏ các dòng trống và in ra danh sách package
cleaned_packages = "\n".join([pkg.strip() for pkg in packages_no_version.strip().splitlines() if pkg.strip()])

print(cleaned_packages)