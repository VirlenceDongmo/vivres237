# Vivres237 🇨🇲

**Prédiction et analyse des prix des denrées alimentaires au Cameroun**

## Objectif

Les prix des produits vivriers (maïs, manioc, riz, huile de palme, etc.) varient
fortement au Cameroun selon les régions et les saisons, compliquant la
planification pour les ménages, les commerçants et les acteurs de la sécurité
alimentaire. Ce projet explore ces variations et construit des modèles pour
les comprendre et les prédire.

C'est un projet d'apprentissage progressif en data science, structuré en
étapes de complexité croissante : collecte de données, nettoyage, analyse
exploratoire, modélisation (séries temporelles puis machine learning), et
déploiement d'une application interactive.

## Roadmap du projet

- [ ] **Étape 1 — Collecte de données** : récupération des séries de prix
      (FAO FPMA, WFP VAM, HDX) et éventuel scraping complémentaire
- [ ] **Étape 2 — Nettoyage & EDA** : gestion des valeurs manquantes,
      visualisation des tendances par région/produit/saison
- [ ] **Étape 3 — Modélisation** : baseline (moyenne mobile, régression
      linéaire) → séries temporelles (SARIMA, Prophet) → ML (Random Forest,
      XGBoost) → deep learning (LSTM) en comparaison
- [ ] **Étape 4 — Évaluation critique** : comparaison des modèles par
      région/produit, analyse des erreurs
- [ ] **Étape 5 — Déploiement** : application Streamlit pour explorer et
      visualiser les prédictions

## Structure du dépôt

```
vivres237/
├── data/
│   ├── raw/            # Données brutes, non modifiées
│   └── processed/      # Données nettoyées, prêtes pour l'analyse
├── notebooks/          # Notebooks Jupyter (exploration, prototypage)
├── src/                # Code source réutilisable (nettoyage, features, modèles)
├── app/                # Application Streamlit de déploiement
├── reports/
│   └── figures/        # Graphiques et visualisations exportées
├── tests/               # Tests unitaires
├── requirements.txt
└── README.md
```

## Sources de données envisagées

- [FAO - Food Price Monitoring and Analysis (FPMA)](https://fpma.fao.org/)
- [WFP VAM Data (World Food Programme)](https://dataviz.vam.wfp.org/)
- [Humanitarian Data Exchange (HDX)](https://data.humdata.org/)

## Installation

```bash
git clone <url-du-depot>
cd vivres237
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
```

## État du projet

🚧 Projet en cours de développement — phase de collecte de données.

## Licence

MIT
