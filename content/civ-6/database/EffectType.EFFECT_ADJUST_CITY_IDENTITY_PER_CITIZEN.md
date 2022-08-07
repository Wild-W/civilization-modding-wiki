---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_IDENTITY_PER_CITIZEN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_IDENTITY_PER_CITIZEN
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GOLDEN_AGE_CITY_IDENTITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"GOLDEN_AGE_CITY_IDENTITY",
		"MODIFIER_PLAYER_CITIES_ADJUST_IDENTITY_PER_CITIZEN",
		"PLAYER_HAS_GOLDEN_AGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOLDEN_AGE_CITY_IDENTITY",
		"Amount",
		"0.5"
	);
	
```

