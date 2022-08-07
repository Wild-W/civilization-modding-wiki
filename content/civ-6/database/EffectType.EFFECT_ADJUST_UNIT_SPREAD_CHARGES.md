---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SPREAD_CHARGES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SPREAD_CHARGES
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="HAGIA_SOPHIA_ADJUST_RELIGIOUS_CHARGES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"HAGIA_SOPHIA_ADJUST_RELIGIOUS_CHARGES",
		"MODIFIER_PLAYER_UNITS_ADJUST_SPREAD_CHARGES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HAGIA_SOPHIA_ADJUST_RELIGIOUS_CHARGES",
		"Amount",
		1
	);
	
```

