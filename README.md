<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
    integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g=="
    crossorigin="anonymous" referrerpolicy="no-referrer" />
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap" rel="stylesheet">

<div align="center" style="font-family: 'QuickSand';">
    <h2 style="font-family: 48px;">sakthyvells-api</h2>
    <p style="font-family: 24px;">DRF API used to serve my personal blog</p>
    <p align="center">
        <img src="https://img.shields.io/github/languages/count/sakthyvell/sakthyvells-api" alt="">
        <img src="https://img.shields.io/github/languages/top/sakthyvell/sakthyvells-api" alt="">
        <img src="https://img.shields.io/github/last-commit/sakthyvell/sakthyvells-api" alt="">
        <img src="https://img.shields.io/badge/development-ongoing-green" alt="">
    </p>
</div>

<hr>
<br>

### Installation
#### Recommended : Install virtualenv
```bash
$ pip install virtualenv
$ virtualenv venv
```
#### Install dependencies
```bash
$ pip install -r requirements.txt
```

### Running Django App
To run the django app
```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

### Environment Variables Setup
Certain environment variables are needed to setup and run the app. Create a `.env` file in the root folder with following configurations:
```
export DEBUG=True
export SECRET_KEY=SECRET_KEY
export DATABASE_URL=sqlite:///db.sqlite3
export AWS_ACCESS_KEY_ID =AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY
export AWS_STORAGE_BUCKET_NAME=AWS_STORAGE_BUCKET_NAME
export AWS_S3_FILE_OVERWRITE=False
export USE_S3=False
```
If `USE_S3` variable is set to `True`, kindly update the `.env` with AWS S3 configurations.
