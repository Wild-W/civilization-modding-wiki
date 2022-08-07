---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_PREREQ
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_PREREQ
>
> * Class: `DISTRICTS`
> * Parameters:
>	* DistrictType `String`
>	* TechType `String`

## Samples
```SQL {title="TRAIT_CANAL_UNLOCK_MASONRY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_CANAL_UNLOCK_MASONRY",
		"MODIFIER_PLAYER_ADJUST_DISTRICT_UNLOCK"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CANAL_UNLOCK_MASONRY",
		"DistrictType",
		"DISTRICT_CANAL"
	),
	(
		"TRAIT_CANAL_UNLOCK_MASONRY",
		"TechType",
		"TECH_MASONRY"
	);
	
```

