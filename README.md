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

- [x] **Étape 1 — Collecte de données** : dataset "Cameroon - Food Prices"
      récupéré depuis HDX (voir *Source des données* ci-dessous)
- [x] **Étape 2 — Nettoyage & EDA** :
      - Compréhension des 16 colonnes du dataset brut
      - Vérification qualité (aucune valeur manquante, aucun doublon)
      - Normalisation des unités hétérogènes (KG, 90 KG, L, 400 G...) en un
        prix par kg/litre comparable (`price_per_unit`)
      - Suppression de 1259 lignes aberrantes (1.64%) après normalisation
      - Exclusion des 2484 lignes en unités non normalisables (pièce, jour)
      - Dataset final : **73 064 lignes, 52 produits, 83 marchés**, sauvegardé
        dans `data/processed/prix_alimentaires_nettoyes.csv`
      - Analyse exploratoire complète (voir *Insights clés* ci-dessous)
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

## Source des données

**Dataset utilisé : [Cameroon - Food Prices](https://data.humdata.org/dataset/wfp-food-prices-for-cameroon)**
(Humanitarian Data Exchange, alimenté par le World Food Programme)

- Données mensuelles de prix par marché, région et produit, couvrant la
  période **janvier 2005 à juillet 2026**
- Sources primaires agrégées par le WFP : MINADER, MINCOMMERCE, DRADER,
  FEWSNET, Institut National de la Statistique (Cameroun), via FAO GIEWS
- 83 marchés, 52 produits (après nettoyage), 9 des 10 régions du Cameroun
- Couverture géographique croissante dans le temps : très partielle avant
  2010, stable et quasi complète (≥98%) pour les produits clés à partir de
  2019

Sources explorées mais non retenues pour l'instant (pistes pour un
enrichissement futur — pluviométrie, taux de change, indicateurs
économiques) :
- [FAO - Food Price Monitoring and Analysis (FPMA)](https://fpma.fao.org/)
- [WFP VAM Data (World Food Programme)](https://dataviz.vam.wfp.org/)

## Insights clés de l'analyse exploratoire

**Saisonnalité — dépend fortement du type de produit**
Amplitude saisonnière (écart max-min / moyenne, sur les prix mensuels
moyennés toutes années) :

| Produit | Amplitude saisonnière |
|---|---|
| Oignons | 65.6% |
| Arachides décortiquées | 17.3% |
| Maïs blanc | 17.0% |
| Huile de palme | 11.9% |
| Riz importé (long grain) | 6.4% |
| Bœuf | 4.6% |

Les produits locaux et périssables (oignons, maïs) sont beaucoup plus
sensibles au cycle récolte/soudure que les produits importés (riz) ou à
offre continue (bœuf).

**Instabilité régionale — l'Extrême-Nord se distingue structurellement**
En comparant le coefficient de variation des prix (écart-type / moyenne)
sur 6 produits clés, l'Extrême-Nord ressort systématiquement comme la
région la plus instable (moyenne 34.1%, vs 17-18% pour l'Ouest et le
Littoral), suivi de l'Est et l'Adamaoua. Ce résultat est cohérent sur
presque tous les produits testés, à l'exception du bœuf qui reste stable
partout (7-16%) — signe d'un marché de la viande moins dépendant des
récoltes locales.

Les régions urbaines/consommatrices (Centre, Littoral) ont des prix moyens
plus élevés (coût de transport et de distribution) mais restent plus
stables, tandis que les régions productrices du Nord ont des prix plus bas
mais une volatilité plus forte.

**Point de vigilance pour la modélisation**
La couverture du dataset varie fortement dans le temps (quasi nulle avant
2010, explosion après 2020). Toute comparaison ou modélisation sur longue
période doit en tenir compte, notamment pour les produits moins couverts
que le maïs.

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
