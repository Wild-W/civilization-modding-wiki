---
tags:
- EffectType
title: EFFECT_ADJUST_EXTRA_UNIT_COPY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_EXTRA_UNIT_COPY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* UnitType `String`
>		* [Units.UnitType]

## Samples
```SQL {title="TRAIT_EXTRASAKAHORSEARCHER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_EXTRASAKAHORSEARCHER",
		"MODIFIER_PLAYER_UNITS_ADJUST_EXTRA_UNIT_COPY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_EXTRASAKAHORSEARCHER",
		"Amount",
		1
	),
	(
		"TRAIT_EXTRASAKAHORSEARCHER",
		"UnitType",
		"UNIT_SCYTHIAN_HORSE_ARCHER"
	);
	
```

