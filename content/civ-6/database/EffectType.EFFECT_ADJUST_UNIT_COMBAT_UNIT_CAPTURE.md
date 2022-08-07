---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_COMBAT_UNIT_CAPTURE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_COMBAT_UNIT_CAPTURE
>
> * Class: `UNITS`
> * Parameters:
>	* CanCapture `Boolean`
>	* UnitType `String`
>		* [Units.UnitType]

## Samples

```SQL {title="CAPTURE_PRIZE_SHIPS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CAPTURE_PRIZE_SHIPS",
		"MODIFIER_UNIT_ADJUST_COMBAT_UNIT_CAPTURE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CAPTURE_PRIZE_SHIPS",
		"CanCapture",
		1
	);
	
```


```SQL {title="CAPTURE_COMBAT_UNITS_AS_WORKERS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CAPTURE_COMBAT_UNITS_AS_WORKERS",
		"MODIFIER_UNIT_ADJUST_COMBAT_UNIT_CAPTURE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CAPTURE_COMBAT_UNITS_AS_WORKERS",
		"CanCapture",
		1
	),
	(
		"CAPTURE_COMBAT_UNITS_AS_WORKERS",
		"UnitType",
		"UNIT_BUILDER"
	);
	
```

