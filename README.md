# Projet_Data_Football

## Installation et mise en service du Back-End 
## #Cloner le repo git 
Cloner le repo Git hub
### Création d'un environnement virtuel 
Pour garantir le bon fonctionnement du projet, créez un environnement virtuel. Utilisez les commandes suivantes en fonction de votre système d'exploitation :


Pour windows : 
        python -m venv venv
Pour Linux / Mac (Unix):
        python -m venv venv            

Une fois l'envuronnement virtuel crée, activez celui-ci 
Pour windows : 
        venv\Scripts\activate

Pour Linux / Max (Unix): 
        source venv/bin/activate

### Installation des dépendances 
Une fois l'environnement virtuel créé et activé, installez les dépendances nécessaires à l'aide de la commande suivante :
        pip install -r requirements.txt
Vérifiez que toutes les dépendances sont correctement installées avec la commande :
        pip freeze

### Import des données 
Pour importer les données dans la base de données, utilisez les commandes suivantes pour chaque type de données :


1. Competitions : 

        python manage.py importDataCompetitions
    
2. Clubs :

        python manage.py importDataClubs
    
3. Players :

        python manage.py importDataPlayers

4. Games :

        python manage.py importDataGames

5. ClubGames :

        python manage.py importDataClubGames

6. GameEvents :

        python manage.py importDataGameEvents

7. Appearances :

        python manage.py importDataAppearances

8. PlayersValuations :

        python manage.py importDataPlayersValuations

### Lancement du serveur 
Une fois les données importées dans la base de données, lancez le serveur en utilisant l'une des méthodes suivantes :


Commande Django : 
        python manage.py runserver
Docker 
        docker-compose up 

## Qu'est ce que le projet Data Foot 

Le projet Data Foot est un mini-projet permettant d'afficher diverses statistiques dans différents championnats en fonction des équipes sélectionnées. Il repose sur l'utilisation de l'API Kaggle 'Football Data from Transfermarkt', qui est régulièrement mise à jour.

## Contributeurs 

        https://github.com/Nocsyy

        https://github.com/BChelvi/

        https://github.com/Rmilla