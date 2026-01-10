# create & activate a virtual environment (optional but recommended)
uv venv
source .venv/bin/activate   # macOS/Linux

# install flet
pip install 'flet[all]==0.80.1' --upgrade

# Install the required packages
pip install flet keyboard

# install requirements.txt
pip install -r requirements.txt

# run the app
python -m flet_key_widget.main