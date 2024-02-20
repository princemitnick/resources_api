import psutil


def obtenir_statistiques_processeur():
    # Obtenir les statistiques du processeur
    statistiques_processeur = psutil.cpu_times_percent(interval=1, percpu=True)

    # Afficher les statistiques du processeur
    for i, stats in enumerate(statistiques_processeur):
        print(f"Statistiques du processeur pour le coeur {i + 1}:")
        print(f"Utilisation utilisateur: {stats.user}%")
        print(f"Utilisation système: {stats.system}%")
        print(f"Utilisation idle: {stats.idle}%")
        print(f"Utilisation nice: {stats.nice}%")
        print(f"Utilisation softirq: {stats.softirq}%")
        print(f"Utilisation steal: {stats.steal}%")
        print(f"Utilisation guest: {stats.guest}%")
        print(f"Utilisation guest_nice: {stats.guest_nice}%")
        print("\n")


# Appel de la fonction pour obtenir les statistiques du processeur
obtenir_statistiques_processeur()
