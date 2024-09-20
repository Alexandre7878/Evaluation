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


