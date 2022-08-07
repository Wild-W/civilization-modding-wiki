---
tags:
- EffectType
title: EFFECT_ADD_RELIGIOUS_BUILDING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_RELIGIOUS_BUILDING
>
> * Class: `PLAYERS`
> * Parameters:
>	* BuildingType `String`
>		* [Buildings.BuildingType]

## Samples
```SQL {title="ALLOW_CATHEDRAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ALLOW_CATHEDRAL",
		"MODIFIER_PLAYER_RELIGION_ADD_RELIGIOUS_BUILDING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ALLOW_CATHEDRAL",
		"BuildingType",
		"BUILDING_CATHEDRAL"
	);
	
```

