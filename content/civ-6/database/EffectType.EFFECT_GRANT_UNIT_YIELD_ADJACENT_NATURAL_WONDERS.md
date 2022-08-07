---
tags:
- EffectType
title: EFFECT_GRANT_UNIT_YIELD_ADJACENT_NATURAL_WONDERS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_UNIT_YIELD_ADJACENT_NATURAL_WONDERS
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="GREATPERSON_ADJACENT_NATURALWONDER_SCIENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_ADJACENT_NATURALWONDER_SCIENCE",
		"MODIFIER_PLAYER_UNIT_GRANT_ADJACENT_NATURAL_WONDER_YIELD",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Type,
		Value
	)
VALUES
	(
		"GREATPERSON_ADJACENT_NATURALWONDER_SCIENCE",
		"Amount",
		"ScaleByGameSpeed",
		500
	),
	(
		"GREATPERSON_ADJACENT_NATURALWONDER_SCIENCE",
		"YieldType",
		"ARGTYPE_IDENTITY",
		"YIELD_SCIENCE"
	);
	
```

