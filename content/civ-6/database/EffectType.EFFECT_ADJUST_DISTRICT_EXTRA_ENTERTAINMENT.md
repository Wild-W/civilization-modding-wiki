---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_EXTRA_ENTERTAINMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_EXTRA_ENTERTAINMENT
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_AQUEDUCT_AMENITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_AQUEDUCT_AMENITY",
		"MODIFIER_PLAYER_DISTRICTS_ADJUST_EXTRA_ENTERTAINMENT",
		"DISTRICT_IS_AQUEDUCT_AMENITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_AQUEDUCT_AMENITY",
		"Amount",
		1
	);
	
```

