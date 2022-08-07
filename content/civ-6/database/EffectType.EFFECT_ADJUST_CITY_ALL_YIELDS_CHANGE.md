---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_ALL_YIELDS_CHANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_ALL_YIELDS_CHANGE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="AUTOCRACY_CAPITAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"AUTOCRACY_CAPITAL",
		"MODIFIER_PLAYER_CITIES_ADJUST_CITY_ALL_YIELDS_CHANGE",
		"BUILDING_IS_PALACE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AUTOCRACY_CAPITAL",
		"Amount",
		1
	);
	
```

