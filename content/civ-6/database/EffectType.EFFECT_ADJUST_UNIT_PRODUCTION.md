---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_PRODUCTION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* UnitType `String`
>		* [Units.UnitType]

## Samples
```SQL {title="TRAIT_BUILDERPRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_BUILDERPRODUCTION",
		"MODIFIER_PLAYER_UNITS_ADJUST_UNIT_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_BUILDERPRODUCTION",
		"Amount",
		100
	),
	(
		"TRAIT_BUILDERPRODUCTION",
		"UnitType",
		"UNIT_BUILDER"
	);
	
```

