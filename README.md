# Crontrab
Impletementation de Contrab dans Un project django

- cron est un programme qui permet aux utilisateurs des systèmes Unix d’exécuter automatiquement des scripts, des commandes ou des logiciels à une date et une heure spécifiée à l’avance, ou selon un cycle défini à l’avance

-  Installation de django crontab

```python
  pip install django-crontab
```

- Ajout du packagen dans le Projey Django
```python

    INSTALLED_APPS = (
    'django_crontab',
    ...
)
```

- ensuite Crée un ficher cron.py et cree le script ou la classe que l'on souhaite exceuter dans le fichier cron.py exemple Nous allons excuter un 
script qui enregistre test dans la bd chaque une minute
- dans notre cron.py on entre ele code suvant:
```
  def nanus ():
    req = models.Nan(nom='test')
    req.save()
  
```
- Ensuite on ajout le script cree dans notre setting.py de l'application
```python
CRONJOBS = [
    ('*/3 * * * *', 'myapp.cron.nanus')
]
```
