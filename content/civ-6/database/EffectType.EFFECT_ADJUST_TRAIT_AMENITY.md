---
tags:
- EffectType
title: EFFECT_ADJUST_TRAIT_AMENITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TRAIT_AMENITY
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_CAPTURED_AMENITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_CAPTURED_AMENITY",
		"MODIFIER_PLAYER_CITIES_ADJUST_TRAIT_AMENITY",
		"CITY_NOT_FOUNDED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CAPTURED_AMENITY",
		"Amount",
		1
	);
	
```

