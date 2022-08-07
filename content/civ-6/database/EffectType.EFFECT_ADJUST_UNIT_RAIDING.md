---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_RAIDING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_RAIDING
>
> * Class: `UNITS`
> * Parameters:
>	* Bonus `Integer`
>	* CanRaid `Boolean`

## Samples

```SQL {title="LOOT_GOLD_FROM_COASTAL_RAID"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"LOOT_GOLD_FROM_COASTAL_RAID",
		"MODIFIER_UNIT_ADJUST_RAIDING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"LOOT_GOLD_FROM_COASTAL_RAID",
		"Bonus",
		50
	),
	(
		"LOOT_GOLD_FROM_COASTAL_RAID",
		"CanRaid",
		1
	);
	
```


```SQL {title="UNIT_COASTAL_RAID"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"UNIT_COASTAL_RAID",
		"MODIFIER_UNIT_ADJUST_RAIDING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"UNIT_COASTAL_RAID",
		"CanRaid",
		1
	);
	
```

