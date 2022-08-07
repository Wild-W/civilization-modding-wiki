---
tags:
- EffectType
title: EFFECT_ADD_CULTURE_BOMB_TRIGGER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_CULTURE_BOMB_TRIGGER
>
> * Class: `PLAYERS`
> * Parameters:
>	* CaptureOwnedTerritory `Unknown`
>	* DistrictType `String`
>		* The DistrictType to act as the trigger
>		* [Districts.DistrictType]
>	* ImprovementType `String`
>		* The ImprovementType to act as the trigger
>		* [Improvements.ImprovementType]

## Samples

```SQL {title="GAUL_MINE_CULTURE_BOMB"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GAUL_MINE_CULTURE_BOMB",
		"MODIFIER_PLAYER_ADD_CULTURE_BOMB_TRIGGER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GAUL_MINE_CULTURE_BOMB",
		"CaptureOwnedTerritory",
		0
	),
	(
		"GAUL_MINE_CULTURE_BOMB",
		"ImprovementType",
		"IMPROVEMENT_MINE"
	);
	
```


```SQL {title="BURIAL_GROUNDS_CULTURE_BOMB_TRIGGER_HOLY_SITE_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BURIAL_GROUNDS_CULTURE_BOMB_TRIGGER_HOLY_SITE_MODIFIER",
		"MODIFIER_PLAYER_ADD_CULTURE_BOMB_TRIGGER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BURIAL_GROUNDS_CULTURE_BOMB_TRIGGER_HOLY_SITE_MODIFIER",
		"DistrictType",
		"DISTRICT_HOLY_SITE"
	);
	
```


```SQL {title="TRAIT_CULTURE_BOMB_TRIGGER_FORT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_CULTURE_BOMB_TRIGGER_FORT",
		"MODIFIER_PLAYER_ADD_CULTURE_BOMB_TRIGGER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CULTURE_BOMB_TRIGGER_FORT",
		"ImprovementType",
		"IMPROVEMENT_FORT"
	);
	
```

