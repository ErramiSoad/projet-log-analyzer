def analyser_logs(fichier_log, fichier_rapport):
    erreurs = {'ERROR': 0, 'WARNING': 0, 'INFO': 0}

    with open(fichier_log, 'r') as f:
        lignes = f.readlines()
        for ligne in lignes:
            for niveau in erreurs:
                if niveau in ligne:
                    erreurs[niveau] += 1

    with open(fichier_rapport, 'w') as f:
        f.write("Résumé des logs :\n")
        for niveau, compte in erreurs.items():
            f.write(f"{niveau} : {compte}\n")

if __name__ == "__main__":
    analyser_logs("log.txt", "rapport.txt")

print("Analyse terminée")
