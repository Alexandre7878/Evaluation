# Evaluation
EXO 1 

Création compte GROQ + génération TOKEN : 

![image](https://github.com/user-attachments/assets/64ffe2ba-4832-41e0-9ee7-af96d32bfb1d)


Création fichier .env avec mon TOKEN dedans puis rajout du .env dans le .gitignore pour que GITHUB ne récup pas.

Modification du fichier mini_groq.py pour le .env et importer os

L'application démarre 
![image](https://github.com/user-attachments/assets/c367ab16-8e8e-4edb-a980-83b803ce79a2)



Exo 2 : Set up and Dockerize the FastAPI Application 

Création d'un dossier "app" et rangement du fichier .py dedans.

Création d'un Dockerfile et rajout de uvicorn dans les requirements.
![image](https://github.com/user-attachments/assets/d45bf0ef-dca4-495f-a063-8f5a27002dc3)
![image](https://github.com/user-attachments/assets/f7172536-96d5-4845-a3ee-fb185c1c26c2)

Build de l'image avec mes différentes paramètres : 

![image](https://github.com/user-attachments/assets/522a105d-11d3-42cf-ae51-78cb4140d5e6)

lancement de mon conteneur via l'image créé précédemment : 

![image](https://github.com/user-attachments/assets/ec0af669-8a4a-4871-8504-f2816aec77b7)


Conteneur Docker fonctionnel, FastAPI lancé : 

![image](https://github.com/user-attachments/assets/5f88b62b-23d2-45d5-a50e-3ab3aed60f93)

Ping du conteneur : 

![image](https://github.com/user-attachments/assets/babcf421-1fd7-4851-9743-4ea019bcbbc8)


Création du script test.sh 

![image](https://github.com/user-attachments/assets/6e84387c-05a7-4ccf-ad42-c46cf65f4161)

Mise en fonctionnement du script pendant que le conteneur FASTAPI est en route : 

![image](https://github.com/user-attachments/assets/85c751b7-5db0-4d9a-9947-3133eb2eb798)


exercice 3 : Create a development Branch and Implement testing 

Question 1 : 

Création de la branche dev : 

![image](https://github.com/user-attachments/assets/997b1f43-2533-4b4b-84fe-64b99e2a06e9)

Question 2 : création du fichier test_app.py pour tester mon fastapi:

![image](https://github.com/user-attachments/assets/b5092aa1-128a-4c4c-a6d7-7e46c6a6f30e)

Résultat du pytest : 

![image](https://github.com/user-attachments/assets/957775c0-373f-41d7-ba83-b94ab56eac3e)











