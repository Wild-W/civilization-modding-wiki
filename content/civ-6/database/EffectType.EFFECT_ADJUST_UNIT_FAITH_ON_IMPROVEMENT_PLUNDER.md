---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_FAITH_ON_IMPROVEMENT_PLUNDER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_FAITH_ON_IMPROVEMENT_PLUNDER
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GOV_FAITH_PILLAGE_IMPROVEMENT_FAITH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOV_FAITH_PILLAGE_IMPROVEMENT_FAITH",
		"MODIFIER_PLAYER_UNITS_ADJUST_FAITH_ON_IMPROVEMENT_PILLAGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOV_FAITH_PILLAGE_IMPROVEMENT_FAITH",
		"Amount",
		15
	);
	
```

