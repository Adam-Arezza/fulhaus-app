# fulhaus-app

clone the repo: git clone https://github.com/Adam-Arezza/fulhaus-app.git

install python packages: pip install -r requirements.txt

build the docker image: docker build --tag fulhaus-app -f ./Dockerfile .

Run the image in a docker container: docker run fulhaus-app

To test the API make a post request to http://127.0.0.1:5000/predict with a jpg file to make a prediction on.

The API will return 1 of Bed, Chair or Sofa.
