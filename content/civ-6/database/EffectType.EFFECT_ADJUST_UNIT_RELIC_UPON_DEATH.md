---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_RELIC_UPON_DEATH
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_RELIC_UPON_DEATH
>
> * Class: `UNITS`
> * Parameters:
>	* RelicSource `Unknown`

## Samples
```SQL {title="APOSTLE_MARTYR"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		Permanent
	)
VALUES
	(
		"APOSTLE_MARTYR",
		"MODIFIER_PLAYER_UNIT_ADJUST_RELIC_UPON_DEATH",
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"APOSTLE_MARTYR",
		"RelicSource",
		"RELIC_SOURCE_RELIGIOUS_UNIT"
	);
	
```

