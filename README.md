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

- Enfin, exécutez cette commande pour ajouter tous les travaux définis de CRONJOBS à crontab (de l'utilisateur avec lequel vous exécutez cette commande):
```python
python manage.py crontab add
```
- Apres avoir lancer le contrab vas generer genener un code
que l'on devra copier 
comme ceci:
```python
  adding cronjob: (964787d1407926910a1660d5aabdfa05) -> ('*/1 * * * *', 'myapp.cron.nanus')
```
- lancer cette commande pour le crontab 
```python
  python manage.py crontab run 964787d1407926910a1660d5aabdfa05
```
- nb a chaque modification du relancer la commande 
```python
  python manage.py crontab remove
```
- ensuite la commande add et lancer le run

