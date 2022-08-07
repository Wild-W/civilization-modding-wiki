---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_CULTURE_BORDER_EXPANSION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_CULTURE_BORDER_EXPANSION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="RELIGIOUS_SETTLEMENTS_CULTUREBORDER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"RELIGIOUS_SETTLEMENTS_CULTUREBORDER",
		"MODIFIER_ALL_CITIES_CULTURE_BORDER_EXPANSION",
		"CITY_FOLLOWS_PANTHEON_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RELIGIOUS_SETTLEMENTS_CULTUREBORDER",
		"Amount",
		15
	);
	
```

