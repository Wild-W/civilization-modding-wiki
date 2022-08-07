---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_EVICT_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_EVICT_PERCENT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="APOSTLE_EVICT_ALL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"APOSTLE_EVICT_ALL",
		"MODIFIER_PLAYER_UNIT_ADJUST_EVICT_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"APOSTLE_EVICT_ALL",
		"Amount",
		50
	);
	
```

